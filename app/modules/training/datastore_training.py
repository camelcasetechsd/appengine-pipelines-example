import webapp2
import logging
import os
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from app.modules.common.kinds import Example

class DatastoreTrainingHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("DatastoreTrainingHandler")
        
        # get entities
        entities_for_example_kind = Example.query().fetch(20)

        # make a list of key value pairs
        entities = []
        for entity in entities_for_example_kind:
            entities.append({'key':entity.key.string_id() , 'value':entity.value})

        template_path = os.path.join(os.path.dirname(__file__), 'datastore_training.html')
        self.response.write(template.render(template_path, {
            'entities': entities,
        }))

