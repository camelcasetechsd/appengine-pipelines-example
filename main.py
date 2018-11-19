import sys
import os
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app

# add our libs folder to the path
sys.path.insert(1, os.path.abspath('./libs'))

# include pipeline handler
from pipeline.handlers import _APP as pipeline_app

# include application handlers
from app.handlers import handlers

# Retrieve our handlers
handlers = handlers()

# Config app with our handlers with debug mode enabled
app = webapp2.WSGIApplication(handlers, debug=True)

# Run the application
def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()
