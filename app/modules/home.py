import webapp2
import logging
import os
import geocoder
from google.appengine.ext.webapp import template
from google.appengine.api import users

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("HomeHandler get()")

        logging.info(self.request.remote_addr)

        g = geocoder.ip(self.request.remote_addr)
        

        if not g.latlng:
            lat = 30.0355
            lng = 31.223
        else:
            lat = g.latlng[0]
            lng = g.latlng[1]
            
        logging.info(lat)
        logging.info(lng)
        
        # get logged in user
        user = users.get_current_user()

        template_path = os.path.join(os.path.dirname(__file__), 'home.html')
        
        self.response.write(template.render(template_path, {'user_name' : user.nickname() , 'lat' : lat , 'lng' : lng}))
