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


3. **datastore_training**
Using `app/modules/examples/datastore_example.py` as your example, create a new
`app/modules/training/datastore_training.py` file, with a handler accessible
at `/training/datastore`.

In your training Datastore page, implement a listing of all `entities` existing
for the *Example* `kind`. See more info:
https://cloud.google.com/appengine/docs/standard/python/ndb/

For the output, simply create a `<dl>` element with a `<dt>`  containing each
entity *key* and a `<dd>` containing each entity *value*:
https://www.w3schools.com/tags/tag_dl.asp


## Full Pipeline "CityInfo" Task

After the training tasks are complete, please work on this task to create a
fully working set of pipelines to achieve a non-trivial aim.

The aim of the task is to process weather information and Wikipedia extract 
for a set of locations defined in a YAML config file. Once this information has 
been retrieved from the relevant APIs, it should be persisted to the Datastore.
The Datastore shall contained the latest version of this information. A webpage 
shall be created to display this data to the end user.

### Modules
* `cityinfo` - A new Python module to contain all functionality related to this task.

### Endpoints
* `GET /cityinfo/build` - This endpoint shall trigger the pipelines to build 
the information from the APIs.
* `GET /cityinfo/view` - This endpoint shall display the latest information 
retrieved from the Datastore. This should take the form of a listing, showing all 
...

### Entities (Kinds)
* `CityInfo` - Fields: `Location` (City name), `Info` (Extract from Wikipedia), 
`Temp` (Temperature from Weather API), `LastUpdated` (Time of last build to 
update this info). Use `Location` (City name) also as the `key` of the entity 
(to make it easy to update existing entities rather than creating new entities 
when a Location already exists in `CityInfo`).

### Config
* `cityinfo.yaml` - This shall list the cities and their lat/lon coordinates 
(take the content from `yaml_example.yaml` and use it for this).

### Pipelines
* `CityInfoRootPipeline` - Fetch the locations from YAML config and loop through 
them, `yield`ing a `CityInfoFetchPipeline` for each location. At the end of 
this pipeline, `yield` `CityInfoPersistPipeline` to save the data.
* `CityInfoFetchPipeline` - A pipeline to control fetching all the data needed 
for a location. `yield` `CityInfoInfoPipeline` & `CityInfoWeatherPipeline` for 
this location.
* `CityInfoInfoPipeline` - Retrieve information on this location from the 
Wikipedia API.
* `CityInfoWeatherPipeline` - Retrieve information on this location from a 
weather API.
* `CityInfoPersistPipeline` - Save all the fields to the `CityInfo` Datastore 
entities for each location. If a `CityInfo` entity already exists for the 
Location then update the existing entity rather than creating a new one.

### Scheduled Tasks (Crons)
* `GET /cityinfo/build` - Hourly
Note: Check this documentation to declare cron jobs in AppEngine:
https://cloud.google.com/appengine/docs/standard/python/config/cron
