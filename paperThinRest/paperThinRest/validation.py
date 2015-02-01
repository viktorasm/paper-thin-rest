import inspect
from functools import wraps
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError
from paperThinRest.apiError import ApiErrorException
from collections import OrderedDict

class SchemaBuilder(object):
    def __init__(self):
        self.result = {}
    
    def object(self):
        self.result = {'type':'object','properties': OrderedDict()}
        return self
    
    def addProperty(self,title,type,required=False):
        self.result['properties'][title] = {'type':type}
        if required:
            if not 'required' in self.result:
                self.result['required'] = []
            self.result['required'].append(title)    
        return self
        
    
    
    def build(self):
        return self.result

def schema(itemSchema):
    '''
    validates json schema for argument 'itemData' against provided 'itemSchema'
    '''
    
    def schemaValidator(func):
        argSpec = inspect.getargspec(func)
        
        argIndex = argSpec.args.index('itemData')
        func.jsonSchema = itemSchema
        
        @wraps(func)
        def methodExecutor(*args,**kwargs):
            itemData = kwargs.get('itemData')
            if itemData is None:
                itemData = args[argIndex]
            
            try:
                validate(itemData,itemSchema);
            except ValidationError,err:
                raise ApiErrorException().jsonValidationFailed(err)
            
            
            return func(*args,**kwargs)
        return methodExecutor
    return schemaValidator
    