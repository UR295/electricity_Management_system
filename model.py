import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load the dataset
data = pd.read_csv('d2.csv')

# Convert the 'Dates' column to datetime format
data['Dates'] = pd.to_datetime(data['Dates'], format='%d/%m/%Y %H:%M:%S')

# Extract additional features from 'Dates'
data['Year'] = data['Dates'].dt.year
data['Month'] = data['Dates'].dt.month
data['Day'] = data['Dates'].dt.day
data['DayOfWeek'] = data['Dates'].dt.dayofweek

# Encode categorical variables
state_encoder = LabelEncoder()
region_encoder = LabelEncoder()

# Fit encoders on the entire dataset
data['State_encoded'] = state_encoder.fit_transform(data['States'])
data['Region_encoded'] = region_encoder.fit_transform(data['Regions'])

# Define features and target
features = ['State_encoded', 'Region_encoded', 'latitude', 'longitude', 'Year', 'Month', 'Day', 'DayOfWeek']
target = 'Usage'

X = data[features]
y = data[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set and calculate accuracy metrics
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Streamlit App
st.title("Data Usage Prediction by State")
st.write(f"Model Accuracy: RMSE = {rmse:.2f}, R² = {r2:.2f}")

# User input for prediction
st.header("Predict Data Usage")
state_input = st.selectbox("Select State", data['States'].unique())
region_input = st.selectbox("Select Region", data['Regions'].unique())
latitude_input = st.slider("Latitude", float(data['latitude'].min()), float(data['latitude'].max()), float(data['latitude'].mean()))
longitude_input = st.slider("Longitude", float(data['longitude'].min()), float(data['longitude'].max()), float(data['longitude'].mean()))
year_input = st.slider("Year", int(data['Year'].min()), int(data['Year'].max()), int(data['Year'].mean()))
month_input = st.slider("Month", 1, 12, 1)
day_input = st.slider("Day", 1, 31, 1)
dayofweek_input = st.slider("Day of the Week", 0, 6, 0)

# Encode the user inputs with fallback for unseen labels
try:
    state_encoded = state_encoder.transform([state_input])[0]
except ValueError:
    st.error(f"The state '{state_input}' was not seen during training. Please choose a different state.")
    st.stop()

try:
    region_encoded = region_encoder.transform([region_input])[0]
except ValueError:
    st.error(f"The region '{region_input}' was not seen during training. Please choose a different region.")
    st.stop()

# Create a DataFrame for prediction
input_features = pd.DataFrame([[state_encoded, region_encoded, latitude_input, longitude_input, year_input, month_input, day_input, dayofweek_input]], 
                              columns=features)

# Make prediction
prediction = model.predict(input_features)

# Display the prediction
st.subheader("Predicted Data Usage")
st.write(f"Predicted Usage: {prediction[0]:.2f} MB")
