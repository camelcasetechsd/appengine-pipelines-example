import webapp2
import logging
import os
import pipeline
from google.appengine.ext.webapp import template

class PipelineExampleHandler(webapp2.RequestHandler):
    def get(self, number=10):
        logging.info("PipelineExampleHandler get(%s)" % number)

        if number == "":
            number = 10
        else:
            number = int(number)

        square_stage = SquarePipeline(number)
        square_stage.start()

        template_path = os.path.join(os.path.dirname(__file__), 'pipeline_example.html')
        self.response.write(template.render(template_path, {
            'number': number,
        }))

class SquarePipeline(pipeline.Pipeline):

    output_names = ['square']

    def run(self, number):
        logging.info("SquarePipeline run()")
        self.fill(self.outputs.square, number * number)

    def finalized(self):
        logging.info("SquarePipeline finalized()")
        logging.info('All done! Square is %s', self.outputs.square.value)
