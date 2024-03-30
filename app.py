import streamlit as st
import pickle
import pandas as pd

with open('pipe.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

teams = sorted([
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
])

cities = sorted([
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
])

st.title('IPL Winning Prediction System')

batting_team = st.selectbox('Select the batting team', teams)
bowling_team = st.selectbox('Select the bowling team', teams)
selected_city = st.selectbox('Select Host City Ground', cities)
target = st.number_input('Target Run')
score = st.number_input('Current Score')
overs = st.number_input('Completed Overs')
wickets = st.number_input('Wickets Gone')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_left],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    result = model.predict_proba(input_df)
    win_prob = result[0][1] * 100
    loss_prob = result[0][0] * 100
    st.header(f"{batting_team} - {win_prob:.2f}%")
    st.header(f"{bowling_team} - {loss_prob:.2f}%")
