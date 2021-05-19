# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from api_key import key, projectId, algorthimia_api, algorthimia_key
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

cred = credentials.Certificate("./serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'projectId': projectId,
})

db = firestore.client()
corona = db.collection(u'pandemic').document(u'corona')
corona_faqs = corona.collection(u'FAQs - Scrapper')

stop_words = stopwords.words('english')
stop_words.append('Q')
stop_words.append('q:')


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
        distype = "None"
        location = "None"
        condition = "None"
        distype = tracker.get_slot("disaster_type")
        location = tracker.get_slot("location")
        condition = tracker.get_slot("patient_condition")

        if condition == "infected" or condition == "infect" or condition == "infection":
            response = "Currently the number of "+distype+" victims in your location is "

        elif condition == "died" or condition == "death" or condition == "dying" or condition == "deaths":
            response = "Currently the number of "+distype+" victims in your location is "

        elif condition == "recovered" or condition == "recoveries" or condition == "recover":
            response = "Currently the number of "+distype+" recoveries in your location is "

        elif condition == "None":
            response = "Currently, in your location the cases of the following are:\nDeaths: Balaj pls add API\nRecovered Patients: Balaj pls add API\nInfected Patients: Balaj pls add API\nCritical Condition: Balaj pls add API"

        dispatcher.utter_message(text=response)

        return []


class ActionCheckSymptom(Action):

    def name(self) -> Text:
        return "action_checksymptom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        checksymp = "None"
        distype = tracker.get_slot("disaster_type")
        checksymp = tracker.get_slot("symptom")
        getsymptomsfromdatabase = ["fever", "fatigue", "cough"]
        if checksymp in getsymptomsfromdatabase:
            response = "Yes, " + checksymp + " is a symptom of " + distype + \
                "\nOther symtoms include blah blah\nIf you have more of these symptoms, please consult a doctor to recieve a certain diagnosis. \nWould you like me to find a hospital for you?"
        else:
            response = "According to my database, this isn't a verified or listed symptom of " + \
                distype + " but i recommend you consult a doctor to be certain.\nWould you like me to find a hospital for you?"

        dispatcher.utter_message(text=response)
        facility = "hospital"
        return [SlotSet("facility_search", facility)]


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

# ML model query


class ActionML(Action):
    def name(self) -> Text:
        return "action_ml"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = tracker.get_slot('query')  # obtain location

        client = Algorithmia.client(algorthimia_key)
        algo = client.algo(algorthimia_api)
        algo.set_options(timeout=300)  # optional
        res = algo.pipe(input).result
        response = "According to our ML model your query is " + res
        dispatcher.utter_message(text=response)

        return[]


# DB model query
class ActionDB(Action):

    def name(self) -> Text:
        return "action_db"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = tracker.get_slot('query')  # obtain location

        # breaking query
        query = query.lower()
        new_query = query.split()

        # removing stopwords
        filtered_query = [w for w in new_query if not w in stop_words]

        # if query is more than 10 values (limit by Google Firebase)
        if len(filtered_query) > 10:
            for i in range(0, len(filtered_query)-10):
                filtered_query.pop()

        # quering
        query_result = corona_faqs.where(
            u'keywords', u'array_contains_any', filtered_query).stream()

        # finding item whose keywords match the most
        ans = ""
        max_matches = 0

        for query in query_result:
            dict_ans = query.to_dict()
            matches = sum(
                [1 for i in dict_ans['keywords'] if i in filtered_query])
            if matches > max_matches:
                max_matches = matches
                ans = dict_ans['answer']

        dispatcher.utter_message(text=response)

        return[]
