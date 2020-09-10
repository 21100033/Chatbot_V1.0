## happy path 1 (/tmp/tmpg2x_bl_z/ad6b20250b9a44239fbca3cd71d41c70_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: action_default_ask_affirmation -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_cheer_up -->


## happy path 2 (/tmp/tmpg2x_bl_z/ad6b20250b9a44239fbca3cd71d41c70_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: action_default_ask_affirmation -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_cheer_up -->
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_locmessage -->


## sad path 1 (/tmp/tmpg2x_bl_z/ad6b20250b9a44239fbca3cd71d41c70_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_ask_affirmation -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: utter_greet -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_cheer_up -->


## sad path 2 (/tmp/tmpg2x_bl_z/ad6b20250b9a44239fbca3cd71d41c70_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: action_default_ask_affirmation -->
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: utter_greet -->
* deny: not really
    - utter_goodbye   <!-- predicted: action_default_ask_affirmation -->
    - action_listen   <!-- predicted: utter_locmessage -->


## sad path 3 (/tmp/tmpg2x_bl_z/ad6b20250b9a44239fbca3cd71d41c70_conversation_tests.md)
* greet: hi
    - utter_greet   <!-- predicted: action_default_ask_affirmation -->
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_greet -->
    - utter_did_that_help   <!-- predicted: utter_greet -->
* deny: no
    - utter_goodbye   <!-- predicted: action_default_ask_affirmation -->
    - action_listen   <!-- predicted: utter_locmessage -->


## say goodbye (/tmp/tmpg2x_bl_z/ad6b20250b9a44239fbca3cd71d41c70_conversation_tests.md)
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_locmessage -->


## bot challenge (/tmp/tmpg2x_bl_z/ad6b20250b9a44239fbca3cd71d41c70_conversation_tests.md)
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: utter_greet -->
    - action_listen   <!-- predicted: utter_locmessage -->


