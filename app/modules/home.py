import webapp2
import logging
import os
from google.appengine.ext.webapp import template

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("HomeHandler get()")
        template_path = os.path.join(os.path.dirname(__file__), 'home.html')
        self.response.write(template.render(template_path, {}))
