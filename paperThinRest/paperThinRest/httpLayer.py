from flask import request,jsonify
import json
import sys
from paperThinRest.apiError import ApiErrorException


registeredModules = {}

def getPostedJson():
    postedData = request.stream.read()
    return json.loads(postedData)

def respondWithJson(obj,status=200):
    if not isinstance(obj,dict):
        obj = obj.__dict__
        
    response = jsonify(**obj)
    response.status_code = status
    return response

def registerResource(path,moduleName):
    registeredModules[path] = sys.modules[moduleName]
    
def processRegisterResource(app,path,module):
    
    def getModuleMethod(name,defaultValue=None):
        return getattr(module,name,defaultValue)

    mapToResource = getModuleMethod('mapToResource')
    if mapToResource is None:
        mapToResource = lambda thing: thing  # a passthrough default implementation
        
    createItem = getModuleMethod('createItem')
    if createItem is not None:
        def httpCreateItem():
            item = createItem(itemData=getPostedJson())
            if item is None:
                raise ApiErrorException().notImplemented()
            
            return respondWithJson(mapToResource(item), 201)
        
        httpCreateItem.baseMethod = createItem
        app.add_url_rule(path,
            methods=['POST'],
            endpoint=module.__name__+':createItem',
            view_func=httpCreateItem)
        
        
    getItem = getModuleMethod('getItem')
    if getItem is not None:
        def httpGetItem(itemId):
            item = getItem(itemId)
            if item is None:
                raise ApiErrorException().resourceNotFound()
            
            return respondWithJson(mapToResource(item), 200)
        
        httpGetItem.baseMethod = getItem
        
        app.add_url_rule(path+'<itemId>',
            methods=['GET'],
            endpoint=module.__name__+':getItem',
            view_func=httpGetItem)
   
        
    editItem = getModuleMethod('editItem')
    if editItem is not None:
        def httpEditItem(itemId):
            editedItem = editItem(itemId=itemId,itemData=getPostedJson())
            if editedItem is None:
                return httpGetItem(itemId)
            return respondWithJson(mapToResource(editedItem),200)
        
        httpEditItem.baseMethod = editItem
        
        app.add_url_rule(path+'<itemId>',
            methods=['POST'],
            endpoint=module.__name__+':editItem',
            view_func=httpEditItem)
        
            
def registerRoutes(app):
    '''
    call this method on a flask app once done registering all API methods
    '''
    
    @app.errorhandler(ApiErrorException)
    def apiErrorHandler(err):
        return respondWithJson(err.responseObject(),status=err.status) 
    
    @app.errorhandler(Exception)
    @app.errorhandler(500)
    def catchAllErrorHandler(err):
        import traceback;traceback.print_exc();
        return apiErrorHandler(ApiErrorException(message="Internal Error",status=500))
    
    
    for path,module in registeredModules.items():
        processRegisterResource(app,path, module)
    
    
            
            
