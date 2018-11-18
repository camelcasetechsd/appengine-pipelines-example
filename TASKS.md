# Tasks

## Training Tasks

Once you have the project setup, please verify you understand how each part of
the functionality works by running through these training tasks.

1. **pipeline_training**
Using `app/modules/examples/pipeline_example.py` as your example, create a new
`app/modules/training/pipeline_training.py` file, with a handler accessible
at `/training/pipeline`.

In your training pipeline, implement the `TwiceSquaredPipeline` and `LogResult`
shown here:
https://sookocheff.com/post/appengine/pipelines/connecting-pipelines/

This training shows how to implement connecting pipelines using the special
`yield` keyword.


2. **http_training**
Using `app/modules/examples/http_example.py` as your example, create a new
`app/modules/training/http_training.py` file, with a handler accessible
at `/training/http`.

In your training HTTP client, implement the `Wikipedia API` to find the
Wikipedia page(s) for particular locations. Like the `http_example`, accept
lat/lon coordinates as inputs from the URL. Then pass them into the call to
this API endpoint (where the `40` and `20` in `ggscoord=40%7C20` are replaced
with the `lat` and `lon` values):
https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=1&explaintext=1&exlimit=20&generator=geosearch&ggscoord=40%7C20&ggsradius=10000&ggslimit=100

Using the JSON provided in the result, print the `title` and `extract` property
from the first item in the `query` array.

Please note - not all lat/lon values will have Wikipedia pages matching their
coordinates. Add basic error handling and output "No pages found" if the
Wikipedia API returns no results.

No API key is required for the Wikipedia API.
