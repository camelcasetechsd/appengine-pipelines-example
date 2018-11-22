import webapp2
import logging
import os
from google.appengine.ext.webapp import template
from app.modules.common.city_info import CityInfoRootPipeline
from app.modules.common.kinds import CityInfo

class CityInfoBuildHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("CityInfoBuildHandler")
        CitiesUpdate = CityInfoRootPipeline()
        CitiesUpdate.start()

class CityInfoViewHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("CityInfoViewHandler")
        
        # get cities
        cities = CityInfo.query().fetch(20)

        logging.info(cities)
        template_path = os.path.join(os.path.dirname(__file__), 'city_info.html')
        self.response.write(template.render(template_path, {
            'cities': cities,
        }))
