import webapp2
import logging
import pipeline

class SquarePipelineExample(pipeline.Pipeline):

    output_names = ['square']

    def run(self, number):
        logging.info("SquarePipelineExample run()")
        self.fill(self.outputs.square, number * number)

    def finalized(self):
        logging.info("SquarePipelineExample finalized()")
        logging.info('All done! Square is %s', self.outputs.square.value)


class SquarePipeline(pipeline.Pipeline):

    def run(self, number):
        return number * number


class TwiceSquaredPipeline(pipeline.Pipeline):

    def run(self, number):
        
        first_square = yield SquarePipeline(number)
        second_square = yield SquarePipeline(first_square)
        yield LogResult(second_square)


class LogResult(pipeline.Pipeline):

    def run(self, number):
        logging.info('All done! Value is %s', number)