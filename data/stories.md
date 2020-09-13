<!-- ## happy path

- greet
  - utter_greet
- mood_great
  - utter_happy

## sad path 1

- greet
  - utter_greet
- mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
- affirm
  - utter_happy

## sad path 2

- greet
  - utter_greet
- mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
- deny
  - utter_goodbye

## say goodbye

- goodbye
  - utter_goodbye

## bot challenge

- bot_challenge
  - utter_iamabot --> -->

## greet + facility search + say goodbye path 1

* greet
  - utter_greet
* facility_search{"facility_type": "hospital", "location": "Islamabad"}
  - action_find_facility
* thankyou
  - utter_welcome_response
  - utter_goodbye

## greet + facility search + say goodbye path 2

* greet
  - utter_greet
* facility_search{"facility_type": "hospital", "location": "Islamabad"}
  - action_find_facility
* acknowledge
  - utter_goodbye

## greet + facility search + location + say goodbye path 1

* greet
  - utter_greet
* facility_search{"facility_type": "hospital"}
  - utter_ask_location
* provide_location{"location": "Islamabad"}
  - action_find_facility
* thankyou
  - utter_welcome_response
  - utter_goodbye

## greet + facility search + location + say goodbye path 2

* greet
  - utter_greet
* facility_search{"facility_type": "hospital"}
  - utter_ask_location
* provide_location{"location": "Islamabad"}
  - action_find_facility
* acknowledge
  - utter_goodbye

## greet + emergency services + location + say goodbye path 1
