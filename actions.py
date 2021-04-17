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
from api_key import key, projectId
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'projectId': projectId,
})

db = firestore.client()


class ActionFindFacility(Action):

    def name(self) -> Text:
        return "action_find_facility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot('location')  # obtain location

        # to get lattitude and longitude of the areas
        URL = "https://maps.googleapis.com/maps/api/geocode/json"

        PARAMS = {'address': loc,  'key': key}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format
        data = r.json()

        lat = data['results'][0]['geometry']['location']['lat']
        long = data['results'][0]['geometry']['location']['lng']
        location = str(lat) + "," + str(long)

        # to find the nearby facility
        URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

        radius = "1500"
        type = tracker.get_slot('facility_type')

        PARAMS = {'location': location, 'radius': radius,
                  'opennow': True, 'type': type, 'key': key}

        # sending get request and saving the response as response object
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format
        data = r.json()
        final_resp = ""  # format the final response in name, vicinity format
        i = 0
        for x in data:
            final_resp += "Name: " + \
                data['results'][i]['name'] + " Vicinity: " + \
                data['results'][i]['vicinity'] + "\n"
            i += 1

        dispatcher.utter_message(text=final_resp)

        return []


class ActionFindService(Action):

    def name(self) -> Text:
        return "action_find_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # since corona related also adding testing facilities.
        final_resp = "Pakistan COVID-19 Helpline: 1166\nEdhi Ambulance: 115\nRescue: 1122\nAman TeleHealth: 111-11-9123\nTesting Facilities list: http://covid.gov.pk/facilities/10%20June%202020%20Current%20Laboratory%20Testing%20Capacity%20for%20COVID.pdf"

        dispatcher.utter_message(text=final_resp)

        return []


class ActionFindCases(Action):

    def name(self) -> Text:
        return "action_findcases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        distype = tracker.get_slot("disaster_type")
        location = tracker.get_slot("location")

        return []


class ActionCheckSymptom(Action):

    def name(self) -> Text:
        return "action_checksymptom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        distype = tracker.get_slot("disaster_type")
        checksymp = tracker.get_slot("symptom")
        getsymptomsfromdatabase = "pain"
        if checksymp == getsymptomsfromdatabase:
            response = "Yes, " + checksymp + " is a symptom of " + distype + \
                "\nOther symtoms include blah blah\nIf you have more of these symptoms, please consult a doctor to recieve a diagnosis"
            dispatcher.utter_message(text=response)

        return[]


class ActionFindMed(Action):

    def name(self) -> Text:
        return "action_findmeds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        distype = tracker.get_slot("disaster_type")

        response = "There is currently no universal cure available for " + distype + \
            ", but you can look at the following links to read more about the medical developments related to this topic"
        dispatcher.utter_message(text=response)

        return[]


class ActionFindTest(Action):

    def name(self) -> Text:
        return "action_findtests"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        distype = tracker.get_slot("disaster_type")

        response = "If you want to get tested for "+distype + \
            " the following tests are available for you:"
        dispatcher.utter_message(text=response)

        return[]


class ActionFindAccuracy(Action):

    def name(self) -> Text:
        return "action_getacc"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        testtype = tracker.get_slot("test")

        response = "The accuracy of medical tests can vary depending upon the testing environment and equipment; but generally the accuracy of the " + testtype+" is: "
        dispatcher.utter_message(text=response)

        return[]


class ActionListPrevent(Action):

    def name(self) -> Text:
        return "action_prevent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        distype = tracker.get_slot("disaster_type")

        response = "The most updated and verifed methods to prevent " + distype + " are:"
        dispatcher.utter_message(text=response)

        return[]


class ActionConfirmCause(Action):

    def name(self) -> Text:
        return "action_confirm_cause"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        check_cause = "None"
        distype = tracker.get_slot("disaster_type")
        check_cause = tracker.get_slot("cause")
        if check_cause == "None":
            check_cause = tracker.latest_message['text']

        response = " According to blah blah " + \
            check_cause + " does/doesn't cause " + distype
        dispatcher.utter_message(text=response)

        return[]


class ActionAskCause(Action):

    def name(self) -> Text:
        return "action_ask_cause"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        distype = tracker.get_slot("disaster_type")
        response = "I'm a bit confused. Could you tell me the cause again?"
        dispatcher.utter_message(text=response)

        return[]
