import requests
from requests.exceptions import HTTPError
import os

KEY = os.environ.get('EventfulKey')
URL = 'http://api.eventful.com/json/events/search'

class EventfulAPI():

    #a function to query the api for concert dates
    def get_events(self, search_term):
        #setup parameters for the api query q=keywords, c=category and set to music to enforce
        # that we are always searching for music
        parameters = {'q': {search_term}, 'c': 'music', 'app_key': KEY}

        #request data from eventful.com
        try:
            response = requests.get(URL, params=parameters)
            #only raise error is certain response codes are returned
            #got this idea from https://realpython.com/python-requests/
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error: {http_err}')
        except Exception as ex:
            print(f'Other error: {ex}')
        else:
            #if no error send back top 3 concert dates
            events = response['event']
            #list of dictionary to hold concert dates
            concerts = []
            count = 0
            while count < 4:
                #dictionary to hold event data
                event_data = {'event_name': '','venue': '', 'date': ''}
                for event in events:
                    event_data{'event_name'} =

                    count += 1

            #return the top three concert dates
            return concerts