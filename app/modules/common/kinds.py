import webapp2
import logging
from google.appengine.ext import ndb


class Example(ndb.Model):
    value = ndb.StringProperty()

class CityInfo(ndb.Model):
    Location = ndb.StringProperty()
    Info = ndb.TextProperty()
    Temp = ndb.FloatProperty()
    LastUpdated = ndb.DateTimeProperty(auto_now=True)