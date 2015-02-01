from paperThinRest.httpLayer import registerResource

registerResource('/operational-info/',__name__)


def getItem(itemId):
    if itemId=='ping':
        return {'pong':True}
    
    return None
