import webapp2
import logging
import os
import requests
from google.appengine.ext.webapp import template

class HttpExampleHandler(webapp2.RequestHandler):
    def get(self, lat=51.5, lon=-0.15):
        logging.info("HttpExampleHandler get(%s,%s)" % (lat, lon))

        API_HOST = "http://api.openweathermap.org"
        API_KEY = os.environ.get("HTTP_EXAMPLE_API_KEY")

        if API_KEY:
            apiUrl = "%s/data/2.5/forecast?appid=%s&mode=json&units=metric&lat=%s&lon=%s" % (API_HOST, API_KEY, lat, lon)
            request = requests.get(apiUrl)
            data = request.json()
            template_vars = {
                'has_api_key': True,
                'lat': lat,
                'lon': lon,
                'city': data['city']['name'],
                'temp': data['list'][0]['main']['temp'],
                'weather': data['list'][0]['weather'][0]['main'],
            }
        else:
            template_vars = {
                'has_api_key': False,
            }

        template_path = os.path.join(os.path.dirname(__file__), 'http_example.html')
        self.response.write(template.render(template_path, template_vars))
