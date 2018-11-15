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
