import webapp2
import logging
import pipeline
import app.modules.cityinfo.city_extras as CityExtras
import app.modules.common.util as Utils

class CityInfoRootPipeline(pipeline.Pipeline):

    def run(self):
        logging.info("CityInfoRootPipeline")

        # Read cityinfo.yaml file
        data = Utils.ReadYamlFile('../cityinfo/cityinfo.yaml')
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
        
        CityExtras.StoreCitiesInfo(args)

class CityInfoReturn(pipeline.Pipeline):

    def run(self, cityname,cityInfo , cityTemp):
        logging.info("CityInfoReturn")
        
        return {'Location' : cityname ,'Info' : cityInfo , 'Temp' : cityTemp }
