#initlizing part
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from api_key import key, projectId

cred = credentials.Certificate("./serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
  'projectId': projectId,
})

db = firestore.client()

corona = db.collection(u'pandemic').document(u'corona')
corona_faqs = corona.collection(u'FAQs')

data1 = {
    u'keyword': [u'covid-19', u'what'],
    u'answer': u'A novel coronavirus is a new coronavirus that has not been previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold.'
}
corona_faqs.document(u'001').set(data1)

data2 = {
    u'keyword': [u'why', u'called', u'covid-19'],
    u'answer': u'On February 11, 2020 the World Health Organization announced an official name for the disease that is causing the 2019 novel coronavirus outbreak, first identified in Wuhan China. The new name of this disease is coronavirus disease 2019, abbreviated as COVID-19. In COVID-19, ‘CO’ stands for ‘corona,’ ‘VI’ for ‘virus,’ and ‘D’ for disease. Formerly, this disease was referred to as “2019 novel coronavirus” or “2019-nCoV”.\nThere are many types of human coronaviruses including some that commonly cause mild upper-respiratory tract illnesses. COVID-19 is a new disease, caused by a novel (or new) coronavirus that has not previously been seen in humans.'
}
corona_faqs.document(u'002').set(data2)

data3 = {
    u'keyword': [u'how', u'covid-19', u'spread'],
    u'answer': u'The virus that causes COVID-19 is thought to spread mainly from person to person, mainly through respiratory droplets produced when an infected person coughs, sneezes, or talks. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs. Spread is more likely when people are in close contact with one another (within about 6 feet).\nCOVID-19 seems to be spreading easily and sustainably in the community (“community spread”) in many affected geographic areas. Community spread means people have been infected with the virus in an area, including some who are not sure how or where they became infected.'
}
corona_faqs.document(u'003').set(data3)

data4 = {
    u'keyword': [u'covid-19', u'how', u'prevent', u'santizer', u'soap'],
    u'answer': u'The best way to prevent illness is to avoid being exposed to the virus. It is recommended to wash your hands often with soap and water for at least 20 seconds especially after you have been in a public place, or after blowing your nose, coughing, or sneezing. If soap and water are not available, it is recommended  to use an alcohol-based hand sanitizer that contains at least 60 percent alcohol.'
}
corona_faqs.document(u'004').set(data4)

data5 = {
    u'keyword': [u'covid-19', u'wear', u'masks', u'public', u'outdoors'],
    u'answer': u'It is recommended to wear masks in public when other social distancing measures are difficult to maintain (e.g., grocery stores and pharmacies) especially in areas of significant community-based transmission of the coronavirus. The purpose of wearing a mask in public is to slow the spread of the virus and help people who may have the virus and do not know it from transmitting it to others.'
}
corona_faqs.document(u'005').set(data5)

data6 = {
    u'keyword': [u'treatment', u'covid-19'],
    u'answer': u'Currently there are no approved medicines specifically for COVID-19. However, the health department has granted emergency use authorizations for some medicines to be used for certain patients hospitalized with COVID-19. \nPeople with COVID-19 should receive supportive care to help relieve symptoms. People with mild symptoms are able to recover at home. If you experience a medical emergency such as trouble breathing, call 1166 and let the operator know you may have COVID-19. Never take a prescription medicine or drug if it is not prescribed for you by your doctor for your health condition.'
}
corona_faqs.document(u'006').set(data6)

data7 = {
    u'keyword': [u'disinfectant', u'spray', u'mists', u'wipes', u'liquid', u'skin', u'treat', u'inhale', u'ingest', u'covid-19'],
    u'answer': u' No. Disinfectant products such as sprays, mists, wipes, or liquids are only to be used on hard, non-porous surfaces (materials that do not absorb liquids easily) such as floors and countertops, or on soft surfaces such as mattresses, sofas, and beds.\nDisinfectants should not be used on human or animal skin. Disinfectants may cause serious skin and eye irritation.\nDisinfectants are dangerous for people to inject, inhale, or ingest. If you breathe, inject, or swallow disinfectants you may be seriously hurt or die. If someone near you swallows, injects, or breathes a disinfectant, call poison control or a medical professional immediately.'
}
corona_faqs.document(u'007').set(data7)

data8 = {
    u'keyword': [u'Disinfectant', u'spraying', u'people', u'covid-19', u'lower', u'spread'],
    u'answer': u'Currently there are no data showing that spraying people with aerosolized disinfectants, or having people walk through tunnels or rooms where disinfectant is in the air, can treat, prevent, or lower the spread of COVID-19.\nSurface disinfectants should not be used on people or animals. Disinfectant products, such as sprays, mists, wipes, or liquids are only to be used on hard, non-porous surfaces (materials that do not absorb liquids easily) such as floors and countertops, or on soft surfaces such as mattresses, sofas, and beds.'
}
corona_faqs.document(u'008').set(data8)

data9 = {
    u'keyword': [u'rash', u'reaction', u'sanitizer', u'covid-19'],
    u'answer': u'Call your doctor if you experience a serious reaction to hand sanitizer. '
}
corona_faqs.document(u'009').set(data9)

data10 = {
    u'keyword': [u'increased', u'risk', u'smoking', u'cigarettes', u'covid-19'],
    u'answer': u'Smoking cigarettes can leave you more vulnerable to respiratory illnesses, such as COVID-19. For example, smoking is known to cause lung disease and people with underlying lung problems may have increased risk for serious complications from COVID-19, a disease that primarily attacks the lungs. Smoking cigarettes can also cause inflammation and cell damage throughout the body, and can weaken your immune system, making it less able to fight off disease.'
}
corona_faqs.document(u'010').set(data10)

data11 = {
    u'keyword': [u'vape', u'covid-19', u'nicotine', u'increased', u'risk'],
    u'answer': u'E-cigarette use can expose the lungs to toxic chemicals, but whether those exposures increase the risk of COVID-19 or the severity of COVID-19 outcomes is not known. However, many e-cigarette users are current or former smokers, and cigarette smoking increases the risk of respiratory infections, including pneumonia.'
}
corona_faqs.document(u'011').set(data11)

data12 = {
    u'keyword': [u'covid-19', u'blood', u'transmission'],
    u'answer': u'In general, respiratory viruses are not known to be transmitted by blood transfusion, and there have been no reported cases of transfusion-transmitted coronavirus.'
}
corona_faqs.document(u'012').set(data12)

data13 = {
    u'keyword': [u'Convalescent', u'plasma', u'covid-19', u'treatment'],
    u'answer': u' Convalescent refers to anyone recovering from a disease. Plasma is the yellow, liquid part of blood that contains antibodies. Antibodies are proteins made by the body in response to infections.  Convalescent plasma from patients who have already recovered from coronavirus disease 2019 (COVID-19) may contain antibodies against COVID-19. Based on scientific evidence available, the health department concluded this product may be effective in treating COVID-19 and that the known and potential benefits of the product outweigh the known and potential risks of the product for patients hospitalized with COVID-19.'
}
corona_faqs.document(u'013').set(data13)

data14 = {
    u'keyword': [u'donate', u'convalescent', u'plasma', u'covid-19'],
    u'answer': u'COVID-19 convalescent plasma must only be collected from recovered individuals if they are eligible to donate blood. Individuals must have had a prior diagnosis of COVID-19 documented by a laboratory test and meet other laboratory criteria. Individuals must have fully recovered from COVID-19, with complete resolution of symptoms for at least 14 days before donation of convalescent plasma.'
}
corona_faqs.document(u'014').set(data14)

data15 = {
    u'keyword': [u'test', u'covid-19'],
    u'answer': u'In general, for diagnostic tests, samples are collected from a person’s nose and/or throat using swabs or other collection devices by a healthcare provider in a health care setting. A health care professional swabbing the back of the nasal cavity through the nostril is the preferred way to collect a sample to test for COVID-19. Alternatively, a health care professional may swab the back of your throat or the inside of the front of the nose.'
}
corona_faqs.document(u'015').set(data15)

data16 = {
    u'keyword': [u'dignostic', u'antibody', u'test', u'difference', u'covid-19'],
    u'answer': u'There are two different types of tests – diagnostic tests and antibody tests.\nA diagnostic test can show if you have an active coronavirus infection and should take steps to quarantine or isolate yourself from others. Currently there are two types of diagnostic tests – molecular (RT-PCR) tests that detect the virus’s genetic material, and antigen tests that detect specific proteins on the surface of the virus. Samples are typically collected with a nasal or throat swab, or saliva collected by spitting into a tube.\nAn antibody test looks for antibodies that are made by the immune system in response to a threat, such as a specific virus. Antibodies can help fight infections. Antibodies can take several days or weeks to develop after you have an infection and may stay in your blood for several weeks after recovery. Because of this, antibody tests should not be used to diagnose an active coronavirus infection. At this time, researchers do not know if the presence of antibodies means that you are immune to the coronavirus in the future. While there is a lot of uncertainty with this new virus, it is also possible that, over time, broad use of antibody tests and clinical follow-up will provide the medical community with more information on whether or not, and how long, a person who has recovered from the virus is at lower risk of infection if they are exposed to the virus again. Samples are typically blood from a finger stick or blood draw.'
}
corona_faqs.document(u'016').set(data16)

data17 = {
    u'keyword': [u'food', u'packaging', u'transmission', u'covid-19'],
    u'answer': u'Currently, there is no evidence of food or food packaging being associated with transmission of COVID-19. However, the virus that causes COVID-19 is spreading from person-to-person in some communities. It is recommended that if you are sick, stay home until you are better and no longer pose a risk of infecting others. '
}
corona_faqs.document(u'017').set(data17)

data18 = {
    u'keyword': [u'pets', u'transmission', u'covid-19'],
    u'answer': u'There is a very small number of pets around the world reported to be infected with the virus that causes COVID-19 after having contact with a person with COVID-19. There is currently no evidence that animals are a source of COVID-19 infection.'
}
corona_faqs.document(u'018').set(data18)

data19 = {
    u'keyword': [u'covid-19', u'animals', u'pets'],
    u'answer': u'Yes. Coronaviruses are a large family of viruses. Some coronaviruses like COVID-19 cause cold-like illnesses in people, while others cause illness in certain types of animals, such as cattle, camels, and bats. Some coronaviruses, such as canine and feline coronaviruses, only infect animals and do not infect humans. For example, bovine coronavirus causes diarrhea in young calves, and pregnant cows are routinely vaccinated to help prevent infection in calves. This vaccine is only licensed for use in cattle for bovine coronavirus and is not licensed to prevent COVID-19 in cattle or other species, including humans.\nDogs can get a respiratory coronavirus, which is part of the complex of viruses and bacteria associated with canine infectious respiratory disease, commonly known as “kennel cough.” While this virus is highly contagious among both domestic and wild dogs, it is not transmitted to other animal species or humans.\nMost strains of feline enteric coronavirus, a gastrointestinal form, are fought off by a cat’s immune system without causing disease. However, in a small proportion of these cats, the virus can cause feline infectious peritonitis (FIP), a disease that is almost always fatal.\nOther species, like horses, turkeys, chickens, and swine, can contract their own species-specific strains of coronavirus but, like the other strains mentioned above, they are not known to be transmissible to humans. '
}
corona_faqs.document(u'019').set(data19)