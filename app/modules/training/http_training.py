import webapp2
import logging
import os
import requests
from google.appengine.ext.webapp import template
from requests_toolbelt.adapters import appengine


appengine.monkeypatch(validate_certificate=False)

class HttpTrainingHandler(webapp2.RequestHandler):
    def get(self, lat = None, lon = None):
        logging.info("HttpTrainingHandler get(%s,%s)" % (lat, lon))

        # wikipedia base api url
        API_HOST = "http://en.wikipedia.org/w/api.php?"
            
        # add given lat long to api url
        apiUrl = "%sformat=json&action=query&prop=extracts&exintro=1&explaintext=1&exlimit=20&generator=geosearch&ggsradius=10000&ggslimit=100&ggscoord=%s%s%s" % (API_HOST, lat,"|", lon)

        logging.info(apiUrl)

        template_vars = {}

        try:
            # make the api call
            request = requests.get(apiUrl)
            data = request.json()

            # check if there is data returned
            if 'query' in data :
                
                for idx , page in data['query']['pages'].items():
                    # get the 0 indexd page (first page data)
                    if page['index'] == 0:
                        template_vars = {
                            'title': page['title'],
                            'extract': page['extract'],
                        }

                        break
              
            else:
                # if there is no data returned show user
                template_vars = {
                    'error' : 'No pages found'
                }
        except requests.exceptions.RequestException as e:
            logging.error(e)
            template_vars = {
                'error' : e
            }
 
        template_path = os.path.join(os.path.dirname(__file__), 'http_training.html')
        self.response.write(template.render(template_path, template_vars ))
