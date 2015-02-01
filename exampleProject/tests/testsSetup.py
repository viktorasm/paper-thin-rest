'''
the file is imported first for all tests, so that one time setup is executed
for the suite
'''

from exampleApi import app
from paperThinRest.test import baseRestTestCase

baseRestTestCase.app = app