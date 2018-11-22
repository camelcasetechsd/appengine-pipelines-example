import webapp2
import logging
import pipeline
import os
import yaml
import app.modules.cityinfo.city_extras as CityExtras

class CityInfoRootPipeline(pipeline.Pipeline):

    def run(self):
        logging.info("CityInfoRootPipeline")

        # Read cityinfo.yaml file
        yaml_path = os.path.join(os.path.dirname(__file__), '../cityinfo/cityinfo.yaml')
        with open(yaml_path, 'r') as stream:
            data = yaml.load(stream)

        cities = []

        for city in data['cities'] :
            cityInfo = yield CityInfoFetchPipeline(city)
            cities.append(cityInfo)
        
        yield CityInfoPersistPipeline(*cities)
        
class CityInfoFetchPipeline(pipeline.Pipeline):

    def run(self, city):
        logging.info("CityInfoFetchPipeline")
        
        cityinfo = yield CityInfoInfoPipeline(city['lat'] , city['lon'] )
        citytemp = yield CityInfoWeatherPipeline(city['lat'] , city['lon'])

        yield CityInfoReturn(city['name'], cityinfo,citytemp)

class CityInfoInfoPipeline(pipeline.Pipeline):

    def run(self, lat , lon):
        logging.info("CityInfoInfoPipeline")
        return CityExtras.CityWikiInfo(lat , lon)

class CityInfoWeatherPipeline(pipeline.Pipeline):

    def run(self , lat , lon):
        logging.info("CityInfoWeatherPipeline")
        return CityExtras.CityWeatherTemp(lat , lon)

class CityInfoPersistPipeline(pipeline.Pipeline):
    
    def run(self, *args):
        logging.info("CityInfoPersistPipeline")
        
        CityExtras.StoreCitiesInto(args)

class CityInfoReturn(pipeline.Pipeline):

    def run(self, cityname,cityInfo , cityTemp):
        logging.info("CityInfoReturn")
        
        return {'Location' : cityname ,'Info' : cityInfo , 'Temp' : cityTemp }
        
