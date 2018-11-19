import webapp2
import logging
import os
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

class DatastoreExampleHandler(webapp2.RequestHandler):
    def get(self, key="key", value=None):
        logging.info("DatastoreExampleHandler get(%s,%s)" % (key, value))

        entity_key = ndb.Key('Example', key)
        entity = entity_key.get()

        if entity is None:

            if value is None:
                value_result = "No value set!"

            else:
                entity = Example(
                    value=value,
                )
                entity.key = ndb.Key('Example', key)
                entity.put()
                value_result = entity.value

        else:

            if value is None:
                value_result = entity.value

            else:
                entity.value = value
                entity.put()
                value_result = entity.value

        template_path = os.path.join(os.path.dirname(__file__), 'datastore_example.html')
        self.response.write(template.render(template_path, {
            'key': key,
            'value': value_result,
        }))

class Example(ndb.Model):
    value = ndb.StringProperty()
