#initlizing part
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
  'projectId': 'projectId',
})

db = firestore.client()

#using data from corona.assisted.pk for answers of our FAQs section

data = {
    u'keyword': [u'antibiotics', u'prevention', u'preventive'],
    u'disaster': u'covid-19',
    u'answer': u'No. Antibiotics do not work against viruses, they only work on bacterial infections. COVID-19 is caused by a virus, so antibiotics do not work. Antibiotics should not be used as a means of prevention or treatment of COVID-19. They should only be used as directed by a physician to treat a bacterial infection.'
}

db.collection(u'FAQs').document(u'001').set(data)

data2 = {
    u'keyword': [u'rural areas', u'rural', u'less risk'],
    u'disaster': u'covid-19',
    u'answer': u'No. Rural areas are at the same risk as any other area or country. The virus does not discriminate between people from urban and rural areas. Rural areas might even be at more risk if the virus is introduced in the area through an individual. Rural areas have less access to health care and also have people living closer together. The lack of proper testing and the ease of spread can be disastrous for rural areas. We have several examples of this in Pakistan in rural areas in all provinces.'
}

db.collection(u'FAQs').document(u'002').set(data2)

data3 = {
    u'keyword': [u'different symptoms in children', u'corona symptoms', u'child'],
    u'disaster': u'covid-19',
    u'answer': u'No. The symptoms of COVID-19 are similar in children and adults. However, children with confirmed COVID-19 have generally presented with mild symptoms. Reported symptoms in children include cold-like symptoms, such as fever, runny nose, and cough. Vomiting and diarrhea have also been reported. It’s not known yet whether some children may be at higher risk for severe illness, for example, children with underlying medical conditions and special healthcare needs. There is much more to be learned about how the disease impacts children.'
}

db.collection(u'FAQs').document(u'003').set(data3)

data4 = {
    u'keyword': [u'prevent', u'cure', u'medicines', u'therapy'],
    u'disaster': u'covid-19',
    u'answer': u'While some western, traditional or home remedies may provide comfort and alleviate symptoms of COVID-19, there is no evidence that current medicine can prevent or cure the disease. WHO does not recommend self-medication with any medicines, including antibiotics, as a prevention or cure for COVID-19. However, there are several ongoing clinical trials that include both western and traditional medicines.'
}

db.collection(u'FAQs').document(u'004').set(data4)

data5 = {
    u'keyword': [u'pregnancy', u'problems'],
    u'disaster': u'covid-19',
    u'answer': u'We do not know at this time if COVID-19 would cause problems during pregnancy or affect the health of the baby after birth.'
}

db.collection(u'FAQs').document(u'005').set(data5)

data6 = {
    u'keyword': [u'contradict virus', u'get corona', u'get COVID-19', u'pets', u'animals'],
    u'disaster': u'covid-19',
    u'answer': u'There is no reason at this time to think that any animals, including pets might be a source of infection with this new coronavirus that causes COVID-19.'
}

db.collection(u'FAQs').document(u'006').set(data6)

data7 = {
    u'keyword': [u'work', u'affects young', u'less risk for young', u'less risk', u'young'],
    u'disaster': u'covid-19',
    u'answer': u'No. Even though the virus affects older people more severely. Young people are still at risk of not only carrying the virus but also getting seriously ill from it. Young people have been hospitalised and even died all over the world and in Pakistan from Covid-19. Young people also have underlying conditions that put them at serious risk of getting very ill.'
}

db.collection(u'FAQs').document(u'007').set(data7)

data8 = {
    u'keyword': [u'young', u'adult', u'older', u'child', u'social distancing'],
    u'disaster': u'covid-19',
    u'answer': u'Yes, it is absolutely crucial to Pakistan beating the virus that everyone follows social distancing guidelines. Please look at information in the ‘Staying Safe’ section to understand why it is important that everyone follows guidelines given by the government to ensure that the virus is contained and normal life resumes as soon as possible with the least loss of lives.'
}

db.collection(u'FAQs').document(u'008').set(data8)

data9 = {
    u'keyword': [u'virus life', u'surface'],
    u'disaster': u'covid-19',
    u'answer': u'It is not certain how long the virus that causes COVID-19 survives on surfaces, but it seems to behave like other coronaviruses. Studies, including preliminary information on the COVID-19 virus, suggest that coronaviruses may persist on surfaces for a few hours or up to several days. This may vary under different conditions, e.g. type of surface, temperature or humidity of the environment. If you think a surface may be infected, clean it with simple disinfectant to kill the virus and protect yourself and others. Clean your hands with an alcohol-based hand rub or wash them with soap and water. Avoid touching your eyes, mouth, or nose. '
}

db.collection(u'FAQs').document(u'009').set(data9)

data10 = {
    u'keyword': [u'timeline', u'social distance', u'long', u'time', u'lockdown'],
    u'disaster': u'covid-19',
    u'answer': u'Lockdowns are a strict method of implementing social distancing to slow down the spread of the virus depending on the capacity of the health care system. As the spread of the virus slows down, restrictions will be eased and normal life will resume. The process will last a few months depending on the spread of the virus. Please keep up-to-date with the government guidelines and policies on covid.gov.pk.'
}

db.collection(u'FAQs').document(u'010').set(data10)

data11 = {
    u'keyword': [u'economy', u'outbreak', u'pandamic', u'economical effects'],
    u'disaster': u'covid-19',
    u'answer': u'Coronavirus lockdowns and shutting of businesses has negatively affected the economy of every country. Pakistan is a developing country that cannot afford a big loss in our economy. Large sections of our population live below or near the poverty line. The government is concerned greatly about the economy and several plans have been implemented to stabilize the economy during and after the lockdown. It is important to stay updated with the news and listen to government updates about the economic situation. The best way for Pakistanis to avoid major losses to our economy and jobs is to follow government guidelines now to stop the spread of the virus so businesses can open and people can begin going to their job as soon as possible.'
}

db.collection(u'FAQs').document(u'011').set(data11)

data12 = {
    u'keyword': [u'China', u'free'],
    u'disaster': u'covid-19',
    u'answer': u'No, China is not completely free of the virus. China has been exposed to the virus first and has been combatting the virus using social distancing for the longest time. They have finally started seeing some success, and several areas have been declared virus-free. People in these areas can go to work and leave their homes while still following strict distance and hygiene guidelines.'
}

db.collection(u'FAQs').document(u'012').set(data12)

data13 = {
    u'keyword': [u'recieve', u'package', u'parcel', u'China'],
    u'disaster': u'covid-19',
    u'answer': u'According to the World Health Organization, it is safe to receive a package from China. Coronaviruses do not survive long on objects such as letters and packages. For a virus to remain viable, it needs a combination of specific environmental conditions such as temperature, lack of UV exposure and humidity — a combination you won\'t get in packages shipped over a period of days or weeks. Currently, there is no evidence to support transmission of COVID-19 associated with imported goods from China or anywhere in the world.'
}

db.collection(u'FAQs').document(u'013').set(data13)

data14 = {
    u'keyword': [u'risk', u'Pakistan', u'Italy', u'China'],
    u'disaster': u'covid-19',
    u'answer': u'Yes, Pakistan is at the same risk as any other country in the world. The virus does not discriminate between borders and can transfer very quickly to other individuals. 80% of cases in South Korea happened from one person carrying the virus. This has happened in Pakistan in areas like Mardan and can happen in other areas of Pakistan as well.'
}

db.collection(u'FAQs').document(u'014').set(data14)

data15 = {
    u'keyword': [u'children', u'mask', u''],
    u'disaster': u'covid-19',
    u'answer': u'In general, children 2 years and older should wear a mask. However, wearing masks may not be possible in every situation or for some people. Appropriate and consistent use of masks may be challenging for some children, such as children with certain disabilities, including cognitive, intellectual, developmental, sensory and behavioral disorders.'
}

db.collection(u'FAQs').document(u'015').set(data15)

data16 = {
    u'keyword': [u'travel', u'spread', u'affect'],
    u'disaster': u'covid-19',
    u'answer': u'Yes. Just like the flu, coronavirus can be transmitted to people that have not traveled. It can affect everyone without discrimination.'
}

db.collection(u'FAQs').document(u'016').set(data16)

data17 = {
    u'keyword': [u'warm weather', u'change in weather', u'weather', u'change'],
    u'disaster': u'covid-19',
    u'answer': u'Weather has no effect on the spread of COVID-19'
}

db.collection(u'FAQs').document(u'017').set(data17)



