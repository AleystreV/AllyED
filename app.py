import joblib
import streamlit as st
import matplotlib.pyplot as plt

st.title("Project AllyED")
st.caption("Welcome to Project AllyED! We're here to help you foster an environment where your students can feel safe. Trained on the Youth Risk Behavior Survey (YRBS), our model uses the information you enter in the sidebar to predict whether a student might be at a higher risk for depression, suicidal thoughts, physical bullying, and cyberbullying. You can also generally toggle the options to see how different factors affect the probability of various student risks.")
st.caption("_The AllyED model isn't perfect and shouldn't be used as a diagnostic tool - it's just meant to give you an idea of whether your students might need more support, and what you can do to help them out._")

with st.sidebar:
    age = st.number_input("Age", min_value=0, max_value=100, value=17)
    gender = st.selectbox("Gender", ["Female", "Male"], index=1)
    grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th", "Other"], index=0)
    race = st.multiselect("Race", ["American Indian", "Asian", "Black", "Hispanic", "Pacific Islander", "White"], default=["White"])
    height = st.number_input("Height", min_value=0.0, max_value=3.0, value=1.68, step=0.1)
    weight = st.number_input("Weight", min_value=0, max_value=300, value=60, step=1)
    sexuality = st.selectbox("Sexuality", ["Straight", "Gay/Lesbian", "Bisexual", "Other", "Questioning", "Does not understand the question"], index=0)
    seatbeltRiding = st.selectbox("How often do you wear a seatbelt when riding in a car driven by someone else?", ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], index=4)
    weightDescription = st.selectbox("How would you describe your weight?", ["Very underweight", "Slightly underweight", "About the right weight", "Slightly overweight", "Very overweight"], index=2)
    weightPlan = st.selectbox("Which of the following are you trying to do about your weight?", ["Lose weight", "Gain weight", "Stay the same weight", "I'm not trying to do anything about my weight"], index = 0)
    juice = st.selectbox("How often did you drink fruit juice during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=0)
    fruit = st.selectbox("How often did you eat fruits during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=1)
    salad = st.selectbox("How often did you eat salad during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=0)
    potato = st.selectbox("How often did you eat potato during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=1)
    carrot = st.selectbox("How often did you eat carrots during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=0)
    otherVeg = st.selectbox("How often did you eat other vegetables during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=1)
    soda = st.selectbox("How often did you drink soda during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=1)
    milk = st.selectbox("How often did you drink milk during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=0)
    breakfastCount = st.selectbox("How many days did you have breakfast during the past 7 days?", ["None", "1 day", "2 days", "3 days", "4 days", "5 days", "6 days", "7 days"], index=7)
    physicalCount = st.selectbox("How many days were you physically active during the past 7 days? (at least 60 minutes per day)", ["None", "1 day", "2 days", "3 days", "4 days", "5 days", "6 days", "7 days"], index=7)
    screenTime = st.selectbox("What’s your average daily screen time in hours?", ["None", "1", "2", "3", "4", "5+"], index=5)
    peClassCount = st.selectbox("How many days did you attend PE class during the past 7 days?", ["None", "1 day", "2 days", "3 days", "4 days", "5 days", "6 days", "7 days"], index=0)
    sportsTeams = st.selectbox("How many sports teams did you play during the past 12 months?", ["None", "1 team", "2 teams", "3+ teams"], index=0)
    sleepHours = st.selectbox("On an average school night, how many hours of sleep do you get?", ["4 or less", "5", "6", "7", "8", "9", "10+"], index=3) 
    drankSportsDrink = st.selectbox("How many times did you drink a sport drink during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4/day"], index=0)
    drankWater = st.selectbox("How many times did you drink a glass of water during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=6)
    muscleExercise = st.selectbox("How many days did you train your muscles during the past 7 days", ["None", "1 day", "2 days", "3 days", "4 days", "5 days", "6 days", "7 days"], index=0)
    schoolmateCloseness = st.selectbox("Do you disagree that you feel close to people at your school?", ["Strongly agree", "Agree", "Not sure", "Disagree", "Strongly disagree"], index=1)
    familyAwareness = st.selectbox("How often do your parents or other adults in your family know where you are going or with whom you will be?", ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], index=4)
    concentratingIssues = st.selectbox("Because of a physical, mental, or emotional problem, do you have serious difficulty concentrating, remembering, or making decisions?", ["Yes", "No"], index=1)
    englishSpeaking = st.selectbox("How well do you speak English?", ["Very well", "Well", "Not well", "Not at all"], index=0)

user_input = {
    "age": age,
    "gender": gender,
    "grade": grade,
    "race": race,
    "hispanic": 2,
    "white": 2,
    "pacificIslander": 2,
    "black": 2,
    "asian": 2,
    "americanIndian": 2,
    "height": height,
    "weightNumber": weight,
    "sexuality": sexuality,
    "seatbeltRiding": seatbeltRiding,
    "doesNotUnderstand": 2,
    "questioning": 2,
    "other": 2,
    "bisexual": 2,
    "gay": 2,
    "straight": 2,
    "weightDescription": weightDescription,
    "weightPlan": weightPlan,
    "juice": juice,
    "fruit": fruit,
    "salad": salad,
    "potato": potato,
    "carrot": carrot,
    "otherVeg": otherVeg,
    "soda": soda,
    "milk": milk,
    "breakfastCount": breakfastCount,
    "physicalCount": physicalCount,
    "screenTime": screenTime,
    "peClassCount": peClassCount,
    "sportsTeams": sportsTeams,
    "sleepHours": sleepHours,
    "drankSportsDrink": drankSportsDrink,
    "drankWater": drankWater,
    "muscleExercise": muscleExercise,
    "schoolmateCloseness": schoolmateCloseness,
    "familyAwareness": familyAwareness,
    "concentratingIssues": concentratingIssues,
    "englishSpeaking": englishSpeaking
}

import pandas as pd
from sklearn.preprocessing import StandardScaler

def fix_data(input_data):
    gender_map = {"Female": 0, "Male": 1}
    input_data["gender"] = gender_map.get(input_data["gender"])
    grade_map = {"9th": 1, "10th": 2, "11th": 3, "12th": 4, "Other": 5}
    input_data["grade"] = grade_map.get(input_data["grade"])
    races = ["American Indian", "Asian", "Black", "Hispanic", "Pacific Islander", "White"]
    racesVariables = ["americanIndian", "asian", "black", "hispanic", "pacificIslander", "white"]
    for race, raceVariable in zip(races, racesVariables):
        input_data[raceVariable] = 1 if race in input_data.get("race", []) else 2
    del input_data["race"]
    sexualities = ["Straight", "Gay", "Bisexual", "Other", "Questioning", "Does not understand the question"]
    sexualityVariables = ["straight", "gay", "bisexual", "other", "questioning", "doesNotUnderstand"]
    for sexuality, sexualityVariable in zip(sexualities, sexualityVariables):
        input_data[sexualityVariable] = 1 if sexuality == input_data["sexuality"] else 2
    del input_data["sexuality"]
    seatbelt_map = {"Never": 1, "Rarely": 2, "Sometimes": 3, "Most of the time": 4, "Always": 5}
    input_data["seatbeltRiding"] = seatbelt_map.get(input_data["seatbeltRiding"])
    weight_desc_map = {"Very underweight": 1, "Slightly underweight": 2, "About the right weight": 3,
                       "Slightly overweight": 4, "Very overweight": 5}
    input_data["weightDescription"] = weight_desc_map.get(input_data["weightDescription"])
    weight_plan_map = {"Lose weight": 1, "Gain weight": 2, "Stay the same weight": 3, "I'm not trying to do anything about my weight": 4}
    input_data["weightPlan"] = weight_plan_map.get(input_data["weightPlan"])
    height = [input_data["height"]] if input_data["height"] is not None else [[None]]
    weight = [input_data["weightNumber"]] if input_data["weightNumber"] is not None else [[None]]
    food_map = {"None": 1, "1-3": 2, "4-6":3, "1/day": 4, "2/day": 5, "3/day": 6, "4+/day": 7}
    foods = ["juice", "fruit", "salad", "potato", "carrot", "otherVeg", "soda", "milk"]
    for food in foods:
        input_data[food] = food_map.get(input_data[food])
    days_map = {"None": 1, "1 day": 2, "2 days": 3, "3 days": 4, "4 days": 5, "5 days": 6, "6 days": 7, "7 days": 8}
    daysQuestions = ["breakfastCount", "physicalCount", "peClassCount"]
    for daysQuestion in daysQuestions:
        input_data[daysQuestion] = days_map.get(input_data[daysQuestion])
    screen_time_map = {"None": 1, "1": 2, "2": 3, "3": 4, "4": 5, "5+": 6}
    input_data["screenTime"] = screen_time_map.get(input_data["screenTime"])
    sports_teams_map = {"None":1, "1 team":2, "2 teams":3, "3+ teams":4}
    input_data["sportsTeams"] = sports_teams_map.get(input_data["sportsTeams"])
    sleep_hours_map = {"4 or less": 1, "5": 2, "6": 3, "7": 4, "8": 5, "9": 6, "10+": 7}
    input_data["sleepHours"] = sleep_hours_map.get(input_data["sleepHours"])
    drank_sports_drink_map = {"None": 1, "1-3": 2, "4-6": 3, "1/day": 4, "2/day": 5, "3/day": 6, "4/day": 7}
    input_data["drankSportsDrink"] = drank_sports_drink_map.get(input_data["drankSportsDrink"])
    drank_water_map = {"None": 1, "1-3": 2, "4-6": 3, "1/day": 4, "2/day": 5, "3/day": 6, "4+/day": 7}
    input_data["drankWater"] = drank_water_map.get(input_data["drankWater"])
    muscle_exercise_map = {"None": 1, "1 day": 2, "2 days": 3, "3 days": 4, "4 days": 5, "5 days": 6, "6 days": 7, "7 days": 8}
    input_data["muscleExercise"] = muscle_exercise_map.get(input_data["muscleExercise"])
    schoolmate_closeness_map = {"Strongly agree": 1, "Agree": 2, "Not sure": 3, "Disagree": 4, "Strongly disagree": 5}
    input_data["schoolmateCloseness"] = schoolmate_closeness_map.get(input_data["schoolmateCloseness"])
    family_awareness_map = {"Never": 1, "Rarely": 2, "Sometimes": 3, "Most of the time": 4, "Always": 5}
    input_data["familyAwareness"] = family_awareness_map.get(input_data["familyAwareness"])
    concentrating_issues_map = {"Yes": 1, "No": 0}
    input_data["concentratingIssues"] = concentrating_issues_map.get(input_data["concentratingIssues"])
    english_speaking_map = {"Very well": 4, "Well": 3, "Not well": 2, "Not at all": 1}
    input_data["englishSpeaking"] = english_speaking_map.get(input_data["englishSpeaking"])
    processed_input_data = pd.DataFrame([input_data])
    print(processed_input_data)
    return processed_input_data

ebullying_model = joblib.load("NewNewModels\ebullying_model_84.sav")
mental_health_model = joblib.load("NewNewModels\depression_model_71.sav")
pbullying_model = joblib.load("NewNewModels\pbullying_model_82.sav")
suicide_model = joblib.load("NewNewModels\suicide_model_82.sav")

def make_predictions(processed_data):
    scaler = StandardScaler()
    processed_data_scaled = scaler.fit_transform(processed_data)
    ebullying_prob = ebullying_model.predict_proba(processed_data_scaled)[0][1] * 100
    mental_health_prob = mental_health_model.predict_proba(processed_data)[0][1] * 100
    pbullying_prob = pbullying_model.predict_proba(processed_data_scaled)[0][1] * 100
    suicide_prob = suicide_model.predict_proba(processed_data)[0][1] * 100
    return {
        "Cyberbullying Probability": ebullying_prob,
        "Physical Bullying Probability": pbullying_prob,
        "Depression Probability": mental_health_prob,
        "Suicide Probability": suicide_prob
    }

processed_input = fix_data(user_input)
#st.write(processed_input)
predictions = make_predictions(processed_input)

tab1, tab2, tab3 = st.tabs(["Predict", "Learn", "Sources"])

with tab1:
    st.subheader("Predicted Probabilities")
    for key, value in predictions.items():
        st.write(f"{key}: {value:.2f}%")

with tab2:
    choice = st.selectbox("What would you like to learn about?", ["Bullying", "Mental Health", "Inclusion & Diversity"])
    information = {"Bullying": ["The Cyberbullying Research Center reports that approximately 37% of students in the United States have experienced cyberbullying at some point.",
                                "Many instances of bullying go unreported. The School Crime Supplement (SCS) found that of the students who reported being bullied, only 36% said they reported the bullying to an adult at school."],
                   "Mental Health": ["According to the Centers for Disease Control and Prevention (CDC), suicide was the second leading cause of death among individuals aged 15 to 19 in the United States.",
                                     "The National Institute of Mental Health (NIMH) reported that in 2020, an estimated 21.2% of adolescents aged 12 to 17 experienced at least one major depressive episode in the past year."],
                   "Inclusion & Diversity": ["According to the National Center for Educational Statistics (NCES), students from racial and ethnic minority groups are more likely to experience bullying compared to their peers.",
                                             "LGBTQ+ students may face higher risks. According to the Trevor Project's National Survey on LGBTQ Mental Health, 40% of LGBTQ+ youth seriously considered attempting suicide in the past year."]}
    segue = {"Bullying": "Here's how you can support students who are being bullied.",
             "Mental Health": "Here's how you can support students experiencing depression and other mental health concerns.",
             "Inclusion & Diversity": "Here's how you can create an inclusive classroom environment."}
    solutions = {"Bullying": ["Immediate Support - Ensure the safety and well-being of the bullied student.",
                              "Open Communication - Encourage the student to openly communicate their experience. Assure them that they are not alone, and their feelings are valid.",
                              "Educate Students - Conduct awareness programs to educate students about the consequences of bullying.",
                              "Provide Counseling - Offer counseling services to both the bullied student and the bully.",
                              "Peer Support - Encourage the involvement of supportive peers to create a positive environment.",
                              "Follow-Up - Regularly follow up on the situation to ensure resolution and ongoing support."],
                 "Mental Health": ["Begin by involving appropriate professionals, like school counselors, discreetly ensuring the student's safety.",
                                   "Maintain a high level of confidentiality while expressing genuine concern and encouraging the student to seek help discreetly.",
                                   "Collaborate covertly with parents or guardians to establish a supportive home environment.",
                                   "Sensitize school staff discreetly to recognize signs and implement a personalized support plan with necessary adjustments.",
                                   "Schedule confidential, regular check-ins to monitor progress discreetly, promote mental health awareness in the school community discreetly, and establish private emergency protocols.",
                                   "Connect the student confidentially with community resources for ongoing support, keeping meticulous records of interventions and progress in a secure manner."],
                 "Inclusion & Diversity": ["Communication - Foster open communication and active listening to understand diverse perspectives.",
                                           "Respect - Promote mutual respect among students, setting clear expectations for respectful behavior.",
                                           "Diversity in Teaching - Use diverse teaching materials and methodologies to cater to various learning styles and abilities.",
                                           "Incorporate Perspectives - Integrate diverse perspectives into the curriculum, celebrating cultural, ethnic, and gender identities.",
                                           "Prompt Action - Address instances of discrimination promptly, creating a safe space for all students.",
                                           "Collaborative Activities - Encourage collaborative activities to promote teamwork and understanding among students."]}
    for info in information[choice]:
        st.info(info)
    st.warning(segue[choice])
    for sol in solutions[choice]:
        st.success(sol)

with tab3:
    st.write("https://www.psychiatry.org/news-room/apa-blogs/one-in-three-students-impacted-by-cyberbullying")
    st.write("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8052596/")
    st.write("https://www.eparent.com/education/bullying-at-school-and-electronic-bullying/")
    st.write("https://www.childrenshospital.org/conditions/suicide-and-teens")
    st.write("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8503900/")
    st.write("https://nces.ed.gov/fastfacts/display.asp?id=719")
    st.write("https://www.thetrevorproject.org/survey-2023/")
