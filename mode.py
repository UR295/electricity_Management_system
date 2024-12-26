import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


data = pd.read_csv('d2.csv')


data['Dates'] = pd.to_datetime(data['Dates'], format='%d/%m/%Y %H:%M:%S')


data['Year'] = data['Dates'].dt.year
data['Month'] = data['Dates'].dt.month
data['Day'] = data['Dates'].dt.day
data['DayOfWeek'] = data['Dates'].dt.dayofweek


label_encoder = LabelEncoder()
data['State_encoded'] = label_encoder.fit_transform(data['States'])
data['Region_encoded'] = label_encoder.fit_transform(data['Regions'])


features = ['State_encoded', 'Region_encoded', 'latitude', 'longitude', 'Year', 'Month', 'Day', 'DayOfWeek']
target = 'Usage'


if target not in data.columns:
    raise ValueError(f"The target variable '{target}' does not exist in the data.")

X = data[features]
y = data[target]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R2: {r2:.2f}")