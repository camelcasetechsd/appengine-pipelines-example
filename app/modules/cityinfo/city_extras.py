import requests
import logging
import os
from google.appengine.ext import ndb
from requests_toolbelt.adapters import appengine
from app.modules.common.kinds import CityInfo

# https://toolbelt.readthedocs.io/en/latest/adapters.html#appengineadapter
appengine.monkeypatch(validate_certificate=False)

def CityWikiInfo(lat , lon):
    # wikipedia base api url
    API_HOST = "https://en.wikipedia.org/w/api.php?"

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
                    return page['extract']
            
        else:
            # if there is no data returned show user
            logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)
        
    return None

def CityWeatherTemp(lat , lon):
    API_HOST = "http://api.openweathermap.org"
    API_KEY = os.environ.get("HTTP_EXAMPLE_API_KEY")

    if API_KEY:
        try:
            apiUrl = "%s/data/2.5/forecast?appid=%s&mode=json&units=metric&lat=%s&lon=%s" % (API_HOST, API_KEY, lat, lon)
            request = requests.get(apiUrl)
            data = request.json()
            return data['list'][0]['main']['temp']
        except requests.exceptions.RequestException as e:
            logging.error(e)
            
    return None

def StoreCitiesInfo(cities):
    for city in cities:
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
