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

key = "enter-your-api-key" # enter the API shared in group

class ActionFindFacility(Action):

    def name(self) -> Text:
        return "action_find_facility"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot('location') #obtain location

        # to get lattitude and longitude of the areas
        URL = "https://maps.googleapis.com/maps/api/geocode/json"

        PARAMS = {'address': loc,  'key': key} 
  
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params=PARAMS) 
        
        # extracting data in json format 
        data = r.json() 

        lat = data['results'][0]['geometry']['location']['lat']
        long = data['results'][0]['geometry']['location']['lng']
        location = str(lat) + "," + str(long)

        # to find the nearby facility
        URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        
        radius = "1500"
        type = tracker.get_slot('facility_type')
        
        PARAMS = {'location':location, 'radius' : radius, 'opennow' : True, 'type': type, 'key': key} 
        
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params=PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
        final_resp = "" #format the final response in name, vicinity format
        i = 0
        for x in data:
            final_resp += "Name: " + data['results'][i]['name'] + " Vicinity: " +  data['results'][i]['vicinity'] + "\n"
            i += 1
 
        dispatcher.utter_message(text = final_resp)
        
        return []
