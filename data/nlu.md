## intent:greet

- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye

- bye
- goodbye
- see you around
- see you later

## intent:affirm

- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny

- no
- never
- I don't think so
- not at all
- no way
- not really
- nope
- no, thank you
- no, thanks
- no, i'm good
- nah
- no, i'm done
- no. i'm done

## intent:mood_great

- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy

- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge

- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:provide_location

- [Islamabad](location)
- [Lahore](location)
- [Karachi](location)
- [Rawalpindi](location)
- [Sialkot](location)
- [Quetta](location)

## intent:facility_search

- i need a [hospital](facility_type)
- i need a [hospital](facility_type) in [Islamabad](location)
- [hospital](facility_type)
- address of nearest [health center](facility_type)
- can you tell me where the nearest [covid-19 testing center](facility_type) is?
- [corona testing](facility_type) in [Islamabad](location)
- [hospital](facility_type) in [Rawalpindi](location)

## intent:thankyou

- great, thanks
- thank you
- thanks
- wow thanks
- great. thanks
- perfect. thank you
- thanks man!
- thankyou
- thnx

## intent:acknowledge

- ok
- Sounds great
- Got it
- Gotcha
- Okay, i understand
- Okay
- Alright
- Understood
- Right
- sounds good
- i get it
- yeah, okay
- yeah, i got it

## intent: emergency_service_search
- i need [covid-19 emergency service](emergency_service_type) [number](contact_info)
- it's an emergency, i need to call the [covid-19 helpline](emergency_service_type)
- i need to call an [ambulance](emergency_service_type)
- [ambulance](emergency_service_type) [number](contact_info)
- i need to contact [emergency covid-19 services](emergency_service_type)
- [corona emergency](emergency_service_type) [number](contact_info)
- i need to call [corona emergency services](emergency_service_type)


## intent: what_is_covid
- [what is](faq_type) [corona](subject)
- [what is](faq_type) [corona virus](subject)
- [what is](faq_type) covid
- can you [brief me about](faq_type) [corona](subject)
- can you [brief me about](faq_type) [covid](subject)
- can you [tell me about](faq_type) [covid](subject)
- [explain](faq_type) [corona](subject)

## intent: corona_spread
- [How does](faq_type) [corona virus](subject) [spread](verb)
- [How does](faq_type) [covid spread](subject)
- Does [corona](subject) [move](verb)
- Does [corona](subject) [spread](verb) by [rain]{"entity": "weather", "role":"cause"}
- [can someone](faq_type) [spread](verb) the [virus](subject) [without being sick](no_symptoms)
- Is [coronavirus](subject) [airborne](spread)
- [How long](faq_type) does [corona virus](subject) [stay](verb) in a place where a [corona victim](patient) [sneezed](symptom)
- Can [wind]{"entity":"weather", "role":"cause"} [move](verb) [corona](subject) from one place to another

## intent: corona_in_people
- Is [coronavirus](subject) only [dangerous](bad_intent) for [people](target) [below 20]{"entity": "age_text", "value": "below 20"} and [above 65 years]{"entity":"age_text", "value": "above 65 years"} of age
- Can a [newborn](target) [catch](verb) [corona](subject)
- 

## intent: corona_symptoms
- Is severe [body pain](symptom) one of [corona’s symptoms](subject)
- can we have [no symptoms](no_symptoms) and still [have corona](patient_condition)
- what are the [symptoms of corona](subject)
- What [symptoms](subject) should I be [on the lookout](verb) for
- [Is it](faq_type) [dangerous](bad_intent)
- [How](faq_type) [bad](bad_intent) is the [virus](subject)
- Can [corona](subject) [kill](verb) [me](target)
- [Can i](faq_type) [die](verb) from the [virus](subject)

## intent: corona_test
- [What are](faq_type) the [chances of](percentage_search) [false positive](result) of [corona test](subject)
- [what are](faq_type) the [chances of](percentage_search) [false negative](result) of [corona test](subject)

## intent: corona_quarantine
- [if](faq_type) someone is [infected](patient_condition) and [quarantined](patient condition) at home, is it [dangerous](bad_intent) for [other members](target)
- [can someone](faq_type) who has been [quarantined](patient_condition) for [COVID-19](subject) [spread](verb) the illness to [others](target)
- [is someone](faq_type) [after quarantined](patient_condition) still [contagious](can_spread)

## lookup: verb
- spread
- stay
- move
- infect
- injure
- kill
- destroy
- hurt
- remain
- cause 

## lookup: patient_condition
- quarantined
- in quarantine
- infected
- on life support
- on ventilator
- recovered
- recovered patient
- recovered covid-19 patient
- have corona

## lookup: target
- others
- another person
- me
- family members
- babies
- children
- pregant women
- newborn
- toddlers
- old people
- other people
- animals 

## lookup: percentage_search
- chances of
- percentage of
- percentage cases of
- chance of 
- odds of
- likelihood
- percent of 
- lookup percentage of
- search for percentage
- search chances of
<!-- - %age
- % -->

## lookup: patient
- virus victim
- covid-19 patient
- corona victim
- corona patient
- sick person
- sick child
- sick man
- sick woman
- victim
- infected person
- infected people
- someone infected by corona virus
- someone with covid-19 virus
- someone infected by corona virus

## lookup: can_spread
- contagious
- infectious
- spreading
- is able to spread
- can infect
- can spread virus
- can cause corona virus

## lookup: bad_intent
- dangerous
- is dangerous
- is injurious
- fatal
- painful
- severely painful
- very dangerous
- very harmful
- harmful

## lookup: weather
- rain
- rainy
- wind
- sunny
- cloudy
- windy
- cold weather
- winters
- summers
- fall
- spring
- spring time

## lookup: no_symptoms
- showing no signs of covid-19 virus
- asymptomatic
- no visible symptoms
- no fever
- no cough
- not sick
- not ill
- no symptoms
- without being sick
- without showing symptoms
- without fever
- without cough

## lookup: symptoms
- cough 
- fever
- sneezing
- body pain
- pain

## lookup: age_text
 - 65 years old
 - 50 year old
 - 5 years old
 - age is 35 years
 - 45 years of age
 - 12 months old
 - 5 month old
 - i'm 23
 - i'm 24 
 - i'm 25 years old








 
