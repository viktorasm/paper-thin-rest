from flask import Flask
app = Flask(__name__)

from paperThinRest import httpLayer
import exampleApi.resources


httpLayer.registerRoutes(app)

