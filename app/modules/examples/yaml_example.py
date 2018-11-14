import webapp2
import logging
import os
import yaml
from google.appengine.ext.webapp import template

class YamlExampleHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("YamlExampleHandler get()")

        yaml_path = os.path.join(os.path.dirname(__file__), 'yaml_example.yaml')
        with open(yaml_path, 'r') as stream:
            data = yaml.load(stream)

        template_path = os.path.join(os.path.dirname(__file__), 'yaml_example.html')
        self.response.write(template.render(template_path, {
            'data': data,
        }))
