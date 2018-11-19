import webapp2
import logging
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("HomeHandler get()")

        # get logiged in user
        user = users.get_current_user()

        template_path = os.path.join(os.path.dirname(__file__), 'home.html')
        
        self.response.write(template.render(template_path, {'user_name' : user.nickname() }))
