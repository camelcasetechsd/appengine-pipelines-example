import webapp2
import logging
import os

from google.appengine.ext.webapp import template
from app.modules.common.squares import TwiceSquaredPipeline

class PipelineTrainigHandler(webapp2.RequestHandler):
    def get(self, number=10):
        logging.info("PipelineTrainigHandler get(%s)" % number)

        if number == "":
            number = 10
        else:
            number = int(number)

        stage = TwiceSquaredPipeline(number)
        stage.start()

        #square_stage = SquarePipeline(number)
        #square_stage.start()

        template_path = os.path.join(os.path.dirname(__file__), 'pipeline_traning.html')
        self.response.write(template.render(template_path, {
            'number': number,
        }))

