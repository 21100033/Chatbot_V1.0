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

## greet + facility search path 1
* greet
  - utter_greet
* facility_search{"facility_type": "hospital", "location": "Islamabad"}
  - action_find_facility



## greet + facility search + location path 1
* greet
  - utter_greet
* facility_search{"facility_type": "hospital"}
  - utter_ask_location
* provide_location{"location": "Islamabad"}
  - action_find_facility



## greet + emergency services
* emergency_service_search
  - action_find_service

## what_is_covid
* what_is_covid
  - action_ans_faq
## corona_spread
  - action_ans_faq
## corona_in_people
  - action_ans_faq
## corona_symptoms
  - action_ans_faq
## corona_test
  - action_ans_faq
## corona_quarantine
  - action_ans_faq

## goodbye path 1
* acknowledge 
  - utter_anything_else
* deny
  - utter_ack
  - utter_goodbye

## goodbye path 2
* thankyou
  - utter_welcome_response
  - utter_anything_else
* deny
  - utter_ack
  - utter_goodbye

## goodbye path 3
* goodbye
  - utter_goodbye

