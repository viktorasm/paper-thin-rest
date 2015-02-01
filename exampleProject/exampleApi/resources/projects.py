from paperThinRest.httpLayer import registerResource
from paperThinRest.validation import schema, SchemaBuilder
from paperThinRest.describe.generator import example

registerResource('/projects/',__name__)

projectSchema = SchemaBuilder().object() \
        .addProperty('title',type='string',required=True) \
        .addProperty('author',type='string') \
        .build()
        
def getList():
    '''
    this method will automatically bind to:
        GET /projects/
    '''
    pass

@schema(projectSchema)
def createItem(itemData):
    '''
    create a new project
    
    this method will automatically bind to:
        POST /projects/
    '''
    
    
    return {'created':itemData}

@schema(projectSchema)
def editItem(itemId, itemData):
    '''
    this method will automatically bind to:
        POST /projects/<itemId>
    '''
    return {'edited':itemData}

@example(projectSchema)
def getItem(itemId):
    '''
    this method will automatically bind to:
        GET /projects/<itemId>
    '''
    return {'id':itemId,'title':'something'}


