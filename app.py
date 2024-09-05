import joblib
import streamlit as st
import numpy as np
import pandas as pd
from fpdf import FPDF

depression_model = joblib.load('NewNewNewModels/depression_model_69_72_82.sav')
suicide_model = joblib.load('NewNewNewModels/suicide_model_79_82_94.sav')

def preprocess_input(age, grade, height, weight, sexuality, juice, fruit, salad, potato, carrot, otherVeg, soda, milk, breakfastCount,
                     physicalCount, screenTime, peClassCount, sportsTeams, sleepHours, drankSportsDrink, drankWater,
                     schoolmateCloseness, familyAwareness):
    grade_map = {"9th": 9, "10th": 10, "11th": 11, "12th": 12, "Other": 0}
    frequency_map = {
        "None": 0, "1-3": 1, "4-6": 2, "1/day": 3, "2/day": 4, "3/day": 5,
        "4/day": 6, "4+/day": 7
    }

    sexuality_map = {"Straight": 0, "Gay": 1, "Bisexual": 2, "Other": 3, "Questioning": 4, "Does not understand the question": 5}
    day_map = {"None": 0, "1 day": 1, "2 days": 2, "3 days": 3, "4 days": 4, "5 days": 5, "6 days": 6, "7 days": 7}
    sports_teams_map = {"None": 0, "1 team": 1, "2 teams": 2, "3+ teams": 3}
    sleep_hours_map = {"4 or less": 1, "5": 2, "6": 3, "7": 4, "8": 5, "9": 6, "10+": 7}
    agreement_map = {"Strongly agree": 5, "Agree": 4, "Not sure": 3, "Disagree": 2, "Strongly disagree": 1}
    awareness_map = {"Never": 1, "Rarely": 2, "Sometimes": 3, "Most of the time": 4, "Always": 5}
    screen_time_map = {"None": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5+": 5}

    data = [
        age,
        grade_map[grade],
        height,
        weight,
        sexuality_map[sexuality],
        frequency_map[juice],
        frequency_map[fruit],
        frequency_map[salad],
        frequency_map[potato],
        frequency_map[carrot],
        frequency_map[otherVeg],
        frequency_map[soda],
        frequency_map[milk],
        day_map[breakfastCount],
        day_map[physicalCount],
        screen_time_map[screenTime],
        day_map[peClassCount],
        sports_teams_map[sportsTeams],
        sleep_hours_map[sleepHours],
        frequency_map[drankSportsDrink],
        frequency_map[drankWater],
        agreement_map[schoolmateCloseness],
        awareness_map[familyAwareness]
    ]
    return np.array(data).reshape(1, -1)

def StringToPDF(string):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font(fname='DejaVuSansCondensed.ttf', uni = True)
    pdf.add_font(fname='DejaVuSansCondensed.ttf', style='B', uni = True)
    pdf.set_font('DejaVuSansCondensed', size=14)
    pdf.multi_cell(190, 10, txt=string, markdown=True)
    return bytes(pdf.output())

st.title("Project AllyED")
st.caption("Welcome to Project AllyED! We're here to help you foster an environment where your students can feel safe. Trained on the Youth Risk Behavior Survey (YRBS), our model uses the information you enter in the sidebar to predict whether a student might be at a higher risk for depression, suicidal thoughts, physical bullying, and cyberbullying. You can also generally toggle the options to see how different factors affect the probability of various student risks.")
st.caption("_The AllyED model isn't perfect and shouldn't be used as a diagnostic tool - it's just meant to give you an idea of whether your students might need more support, and what you can do to help them out._")


if st.button('Visit our partner, TEDDY!'):
    st.markdown("https://teddy-technovation.streamlit.app/", unsafe_allow_html=True)
    
with st.sidebar:
    st.header("Bulk Input")
    file = st.file_uploader("Upload a CSV File", ["csv"])
    st.header("Trial Mode")
    age = st.number_input("Age", min_value=0, max_value=100, value=17)
    grade = st.selectbox("Grade Level", ["9th", "10th", "11th", "12th", "Other"], index=0)
    height = st.number_input("Height (m)", min_value=0.0, max_value=3.0, value=1.38, step=0.1)
    weight = st.number_input("Weight (kg)", min_value=0, max_value=300, value=60, step=1)
    sexuality = st.selectbox("Sexuality", ["Straight", "Gay/Lesbian", "Bisexual", "Other", "Questioning", "Does not understand the question"], index=0)
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
    screenTime = st.selectbox("What’s your average daily screen time in hours? (Do NOT count time spent doing schoolwork.)", ["None", "1", "2", "3", "4", "5+"], index=5)
    peClassCount = st.selectbox("How many days did you attend PE class during the past 7 days?", ["None", "1 day", "2 days", "3 days", "4 days", "5 days", "6 days", "7 days"], index=0)
    sportsTeams = st.selectbox("How many sports teams did you play during the past 12 months?", ["None", "1 team", "2 teams", "3+ teams"], index=0)
    sleepHours = st.selectbox("On an average school night, how many hours of sleep do you get?", ["4 or less", "5", "6", "7", "8", "9", "10+"], index=3) 
    drankSportsDrink = st.selectbox("How many times did you drink a sport drink during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4/day"], index=0)
    drankWater = st.selectbox("How many times did you drink a glass of water during the past 7 days?", ["None", "1-3", "4-6", "1/day", "2/day", "3/day", "4+/day"], index=6)
    schoolmateCloseness = st.selectbox("Do you agree that you feel close to people at your school?", ["Strongly agree", "Agree", "Not sure", "Disagree", "Strongly disagree"], index=1)
    familyAwareness = st.selectbox("How often do your parents or other adults in your family know where you are going or with whom you will be?", ["Never", "Rarely", "Sometimes", "Most of the time", "Always"], index=4)

input_data = preprocess_input(age, grade, height, weight, sexuality, juice, fruit, salad, potato, carrot, otherVeg, soda, milk, breakfastCount,
                              physicalCount, screenTime, peClassCount, sportsTeams, sleepHours, drankSportsDrink, drankWater,
                              schoolmateCloseness, familyAwareness)
print("SITE_DATA", input_data, sep="\n")
depression_probability = depression_model.predict_proba(input_data)[0][1]
suicidal_thoughts_probability = suicide_model.predict_proba(input_data)[0][1]

st.header("Results for Trial Mode")
st.write(f"**Probability of Depression:** {depression_probability:.2%}")
st.write(f"**Probability of Suicidal Thoughts:** {suicidal_thoughts_probability:.2%}")

st.info("Note: These probabilities are based on statistical models and should not be used as a substitute for professional mental health evaluation. If you or someone you know is in distress, please seek professional help.")

if file != None:
    df = pd.read_csv(file)
    df = df.reset_index()
    string = "RESULTS\nName | Depression Risk | Suicide Risk\n"
    
    for index, row in df.iterrows():
        input_data = preprocess_input(row["age"], str(row["grade"]), row["height"], row["weight"], str(row["sexuality"]), str(row["juice"]), str(row["fruit"]), str(row["salad"]),
                                      str(row["potato"]), str(row["carrot"]), str(row["otherVeg"]), str(row["soda"]),
                                      str(row["milk"]), str(row["breakfastCount"]), str(row["physicalCount"]), str(row["screenTime"]), str(row["peClassCount"]),
                                      str(row["sportsTeams"]), str(row["sleepHours"]),
                                      str(row["drankSportsDrink"]), str(row["drankWater"]), str(row["schoolmateCloseness"]), str(row["familyAwareness"]))
        print("FILE_DATA", input_data, sep="\n")
        name = row["name"]
        depression_probability = round(depression_model.predict_proba(input_data)[0][1] * 100)
        suicidal_thoughts_probability = round(suicide_model.predict_proba(input_data)[0][1] * 100)
        string += name + " | " + str(depression_probability) + "% | " + str(suicidal_thoughts_probability) + "%" + "\n"

    st.header("Results for Bulk Input")        
    st.download_button("Download Report", StringToPDF(string), file_name="Report.pdf")
    print(string)
