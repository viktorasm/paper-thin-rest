from paperThinRest.httpLayer import registerResource
from paperThinRest.validation import schema, SchemaBuilder
from paperThinRest.describe.generator import example

registerResource('/projects/',__name__)

projectSchema = SchemaBuilder().object() \
        .addProperty('title',type='string',required=True) \
        .addProperty('author',type='string') \
        .build()
        
def getList():
    pass

@schema(projectSchema)
def createItem(itemData):
    '''
    create a new project
    '''
    return {'created':itemData}

@schema(projectSchema)
def editItem(itemId, itemData):
    return {'edited':itemData}

@example(projectSchema)
def getItem(itemId):
    return {'id':itemId,'title':'something'}


