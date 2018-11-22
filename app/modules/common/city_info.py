import webapp2
import logging
import pipeline
import os
import yaml
from pipeline import common
import requests
from requests_toolbelt.adapters import appengine
from app.modules.common.kinds import CityInfo
from google.appengine.ext import ndb

# https://toolbelt.readthedocs.io/en/latest/adapters.html#appengineadapter
appengine.monkeypatch(validate_certificate=False)

class CityInfoRootPipeline(pipeline.Pipeline):

    def run(self):
        logging.info("CityInfoRootPipeline")

        # Read cityinfo.yaml file
        yaml_path = os.path.join(os.path.dirname(__file__), '../cityinfo/cityinfo.yaml')
        with open(yaml_path, 'r') as stream:
            data = yaml.load(stream)

        logging.info(data)

        cities = []

        for city in data['cities'] :
            cityInfo = yield CityInfoFetchPipeline(city)
            #yield common.Log.info('SplitCount result = %s', cityData)

            cities.append(cityInfo)
            # yield common.List(cities)
            
            
        #logging.info(*cities)
        
        yield CityInfoPersistPipeline(*cities)
        
class CityInfoFetchPipeline(pipeline.Pipeline):

    def run(self, city):
        logging.info("CityInfoFetchPipeline")
        
        cityinfo = yield CityInfoInfoPipeline(city['lat'] , city['lon'] )
        citytemp = yield CityInfoWeatherPipeline(city['lat'] , city['lon'])

        yield TestReturn(city['name'], cityinfo,citytemp)
        


class CityInfoInfoPipeline(pipeline.Pipeline):

    def run(self, lat , lon):
        logging.info("CityInfoInfoPipeline")

        # wikipedia base api url
        API_HOST = "http://en.wikipedia.org/w/api.php?"

            
        # add given lat long to api url
        apiUrl = "%sformat=json&action=query&prop=extracts&exintro=1&explaintext=1&exlimit=20&generator=geosearch&ggsradius=10000&ggslimit=100&ggscoord=%s%s%s" % (API_HOST, lat,"|", lon)

        logging.info(apiUrl)

        template_vars = {}

        try:
            # make the api call
            request = requests.get(apiUrl)
            data = request.json()

            # check if there is data returned
            if 'query' in data :
                
                for idx , page in data['query']['pages'].items():
                    # get the 0 indexd page (first page data)
                    if page['index'] == 0:
                        # return page['extract']
                        return "good place"
              
            else:
                # if there is no data returned show user
                logging.error(e)
                return None
        except requests.exceptions.RequestException as e:
            logging.error(e)
            return None

class CityInfoWeatherPipeline(pipeline.Pipeline):

    def run(self , lat , lon):
        logging.info("CityInfoWeatherPipeline")
        
        API_HOST = "http://api.openweathermap.org"
        API_KEY = os.environ.get("HTTP_EXAMPLE_API_KEY")

        if API_KEY:
            apiUrl = "%s/data/2.5/forecast?appid=%s&mode=json&units=metric&lat=%s&lon=%s" % (API_HOST, API_KEY, lat, lon)
            request = requests.get(apiUrl)
            data = request.json()
            return data['list'][0]['main']['temp']
        else:
            return None


class CityInfoPersistPipeline(pipeline.Pipeline):
    
    def run(self, *args):
        logging.info("CityInfoPersistPipeline")
        logging.info(args)

        for city in args:
            logging.info(city)
            entity_key = ndb.Key('CityInfo', city['Location'])
            entity = entity_key.get()

            if entity is None:
                entity = CityInfo(
                    Location=city['Location'],
                    Info=city['Info'],
                    Temp=city['Temp']
                )
                entity.key = ndb.Key('CityInfo', city['Location'])
                entity.put()

            else:
                entity.Info = city['Info']
                entity.Temp = city['Temp']
                entity.put()

class TestReturn(pipeline.Pipeline):

    def run(self, cityname,cityInfo , cityTemp):
        logging.info("TestReturn")
        
        return {'Location' : cityname ,'Info' : cityInfo , 'Temp' : cityTemp }
        
