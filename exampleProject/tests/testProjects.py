from tests import testsSetup
testsSetup

from paperThinRest.test.baseRestTestCase import BaseRestTestCase
class Test(BaseRestTestCase):
    
    def testCrud(self):
        data = self.expect(status=201).post('/projects/',data={'title':'something'}).json
        self.assertNotEqual(data.get('created'), None)

        data2 = self.expect(status=200).get('/projects/id1').jsonObject
        self.assertEqual(data2.id,'id1')
        
        editedData = self.expect(status=200).post('/projects/id2',data={'title':'something'}).jsonObject
        self.assertEqual(editedData.edited.title,'something')
        
        
        
    def testValidateSchema(self):
        self.expect(status=400).post('/projects/',data={'title2':'something'})

        

        
        