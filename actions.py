# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionFindFacility(Action):

    def name(self) -> Text:
        return "action_find_facility"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        loc = tracker.get_slot('location') #obtain location
        loc = loc.lower() # to make it easier to compare

        location = ""

        # coded for 3 major cities as need longitude and latitude for search via API
        if loc == "karachi":
            location = "24.8607,67.0011"
        elif loc == "islamabad":
            location = "33.6844,73.0479"
        elif loc == "lahore":
            location = "31.5204, 74.3587"
        
        radius = "1500"
        type = "hospital"
        key = "enter-your-api" # enter the API shared in group
        
        PARAMS = {'location':location, 'radius' : radius, 'opennow' : True, 'type': type, 'key': key} 
        
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params=PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        names = []
        i = 0
        for x in data:
            names.append(data['results'][i]['name'])
            i += 1

        # using list comprehension 
        listToStr = ' '.join(map(str, names)) 
 
        dispatcher.utter_message(text = listToStr)
        
        return []
