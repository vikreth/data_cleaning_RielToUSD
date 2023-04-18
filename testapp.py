import streamlit as st
import statsmodels.api as sm
import pandas as pd

# Load the saved ARIMA model from a file
loaded_results = sm.load('arima_model.pkl')

# Create a Streamlit app
st.title('ARIMA Price Prediction')

# Get user input for the date
date = st.date_input('Enter a date for prediction')

# Convert the date to the appropriate format for the model
date = pd.to_datetime(date)

# Make a prediction for the given date
prediction = loaded_results.predict(start=date, end=date)

# Display the predicted price
st.write(f'The predicted price for {date.date()} is {prediction[0]:.2f}')