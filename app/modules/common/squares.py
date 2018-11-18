import webapp2
import logging
import pipeline

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