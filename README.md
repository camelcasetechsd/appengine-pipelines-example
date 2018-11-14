# AppEngine Pipelines Example

This project contains example code to get AppEngine up and running with its pipeline library.

It is built in **Python**, hosted on **Google App Engine** and makes use of **Pipelines** to process data and generate output.

Development can be done locally in Docker.


## Local Development

1. Clone the git repository locally:
```
git clone git@github.com:camelcasetechsd/appengine-pipelines-example.git
```

2. Start docker images with docker-compose:
```
docker-compose up
```

3. Access the homepage:
http://127.0.0.1:9080/  


## Environment

* **Home**  
http://127.0.0.1:9080/  

* **Pipeline Listing**  
http://localhost:9080/_ah/pipeline/list  

* **AppEngine Admin**  
http://127.0.0.1:9000/  


## Dependencies

All dependencies are installed automatically using the Docker image provided.

* **Python 2.7**  
https://www.python.org/download/releases/2.7/  
Python 2.7 is the version required by Google App Engine for "Standard" Python.

* **Google Cloud SDK**  
https://cloud.google.com/sdk/downloads  
Packages are available for common Linux distributions.

* **Google Cloud SDK - App Engine (Python) Component**  
https://cloud.google.com/appengine/docs/standard/python/download#python_linux  
The Standard Python App Engine component is required, both to run the local dev server and to deploy.
