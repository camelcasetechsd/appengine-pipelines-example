from app.modules.home import HomeHandler
from app.modules.examples.pipeline_example import PipelineExampleHandler
from app.modules.examples.http_example import HttpExampleHandler
from app.modules.examples.datastore_example import DatastoreExampleHandler

def handlers():
    return [
        (r'/', HomeHandler),
        (r'/examples/pipeline', PipelineExampleHandler),
        (r'/examples/pipeline/(\d+)', PipelineExampleHandler),
        (r'/examples/http', HttpExampleHandler),
        (r'/examples/http/([\d\.]+)/([\d\.]+)', HttpExampleHandler),
        (r'/examples/datastore', DatastoreExampleHandler),
        (r'/examples/datastore/([^\/]+)', DatastoreExampleHandler),
        (r'/examples/datastore/([^\/]+)/([^\/]+)', DatastoreExampleHandler),
    ]
