from app.modules.home import HomeHandler
from app.modules.examples.pipeline_example import PipelineExampleHandler

def handlers():
    return [
        (r'/', HomeHandler),
        (r'/examples/pipeline', PipelineExampleHandler),
        (r'/examples/pipeline/(\d+)', PipelineExampleHandler),
    ]
