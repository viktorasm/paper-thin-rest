import unittest
import json

app = None

class GenericObject(object):
    pass

def jsonToObject(jsonObject):
    if isinstance(jsonObject, (list,tuple)):
        return list(map(jsonToObject,jsonObject))

    if isinstance(jsonObject,dict):
        result =  GenericObject()
        result.__dict__ = dict((key,jsonToObject(value)) for (key,value) in jsonObject.items())
        return result
                               
    return jsonObject

class BaseRestTestCase(unittest.TestCase):

    def setUp(self):
        self.nextExpectedStatus = None
        self.client = app.test_client()

    def jsonBody(self,response):
        return json.loads(response.data)
    
    def processResponse(self,response):
        data = response.get_data()
        if response.mimetype=='application/json':
            response.json = json.loads(data)
            response.jsonObject = jsonToObject(response.json)

        if self.nextExpectedStatus is not None and self.nextExpectedStatus!=response.status_code:
            self.fail('Expected HTTP %d, Received HTTP %d: \n%s' % (self.nextExpectedStatus,response.status_code,data))
        return response
    
    def expect(self,status):
        self.nextExpectedStatus = status
        return self
    
    def get(self,*args,**kwargs):
        return self.processResponse(self.client.get(*args,**kwargs))
    
    def post(self,path,data):
        if not isinstance(data, dict):
            data = data.__dict__
        return self.processResponse(self.client.post(path,data=json.dumps(data),
                                                     content_type='application/json'))
