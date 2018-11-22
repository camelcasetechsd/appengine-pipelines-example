import webapp2
import logging
import os
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from app.modules.common.city_info import CityInfoRootPipeline
class CityInfoBuildHandler(webapp2.RequestHandler):
    def get(self):
        CitiesUpdate = CityInfoRootPipeline()
        CitiesUpdate.start()

