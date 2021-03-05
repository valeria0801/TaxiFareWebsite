import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...
#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
#1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger count


d = st.date_input(
    "When are you going to travel?",
    datetime.date(2019, 7, 6))

t = st.time_input('What time are you going to travel?', datetime.time(8, 45))
pickup_datetime = f'{d}%20{t}%20UTC'

#st.write(pickup_datetime)
#st.write('Your are going to travel on:', d, t)

pickup_longitude = st.number_input('Please insert your pickup longitude')
pickup_latitude = st.number_input('Please insert your pickup latitude')
dropoff_longitude = st.number_input('Please insert your dropoff longitude')
dropoff_latitude = st.number_input('Please insert your dropoff latitude')
#st.write('Your pickup coordinates are: ', pickup_longitude, pickup_latitude)
#st.write('Your dropoff coordinates are: ', dropoff_longitude, dropoff_latitude)
passenger_count = st.number_input('How many people are going to travel?')
#st.write(passenger_count, 'passenger')

#'''
## Once we have these, let's call our API in order to retrieve a prediction
#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
#:cara_pensativa: How could we call our API ? Off course... The `requests` package :bombilla:
#'''

url = 'http://taxifare.lewagon.ai/predict_fare/'
#if url == 'http://taxifare.lewagon.ai/predict_fare/':
#    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
#'''
#2. Let's build a dictionary containing the parameters for our API...
'''
'''
params = {"key": "1",
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": float(pickup_longitude),
        "pickup_latitude": float(pickup_latitude),
        "dropoff_longitude": float(dropoff_longitude),
        "dropoff_latitude": float(dropoff_latitude),
        "passenger_count": int(passenger_count)}


#3. Let's call our API using the `requests` package...


url_params = f"{url}?key={params['key']}&pickup_datetime={params['pickup_datetime']}&pickup_longitude={params['pickup_longitude']}&pickup_latitude={params['pickup_latitude']}&dropoff_longitude={params['dropoff_longitude']}&dropoff_latitude={params['dropoff_latitude']}&passenger_count={params['passenger_count']}"

prediction = requests.get(url_params).json()['prediction']

if st.button('click me'):
    st.write(prediction)
else:
    st.write('I was not clicked 😞')


#st.write(prediction)


#4. Let's retrieve the prediction from the **JSON** returned by the API...
## Finally, we can display the prediction to the user

# st.success('This is a success!')
