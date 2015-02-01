from tests import testsSetup
testsSetup

from paperThinRest.test.baseRestTestCase import BaseRestTestCase
class Test(BaseRestTestCase):
    
    def testPing(self):
        data = self.expect(status=200).get('/operational-info/ping').json
        self.assertEqual(data, {'pong':True})
