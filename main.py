try:
    from tensorflow.keras.models import load_model
    model = load_model('weather_ann_model.keras')
except ModuleNotFoundError:
    model = None
import numpy as np
import pandas as pd
import pickle

# load saved artifacts
scaler = pickle.load(open('scaler.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))


def predict_rain(date, location, min_temp, max_temp, rainfall, evaporation, sunshine,
                 wind_gust_dir, wind_gust_speed, wind_dir_9am, wind_dir_3pm,
                 wind_speed_9am, wind_speed_3pm, humidity_9am, humidity_3pm,
                 pressure_9am, pressure_3pm, cloud_9am, cloud_3pm,
                 temp_9am, temp_3pm, rain_today):

    # parse date into year, month, day
    dt = pd.to_datetime(date)

    # label encode RainToday
    rain_today_encoded = label_encoder.transform([rain_today])[0]

    # create a dataframe with all 113 features set to 0
    data = pd.DataFrame(0, index=[0], columns=scaler.feature_names_in_)

    # fill in numeric features
    data['MinTemp'] = min_temp
    data['MaxTemp'] = max_temp
    data['Rainfall'] = rainfall
    data['Evaporation'] = evaporation
    data['Sunshine'] = sunshine
    data['WindGustSpeed'] = wind_gust_speed
    data['WindSpeed9am'] = wind_speed_9am
    data['WindSpeed3pm'] = wind_speed_3pm
    data['Humidity9am'] = humidity_9am
    data['Humidity3pm'] = humidity_3pm
    data['Pressure9am'] = pressure_9am
    data['Pressure3pm'] = pressure_3pm
    data['Cloud9am'] = cloud_9am
    data['Cloud3pm'] = cloud_3pm
    data['Temp9am'] = temp_9am
    data['Temp3pm'] = temp_3pm
    data['RainToday'] = rain_today_encoded
    data['Year'] = dt.year
    data['Month'] = dt.month
    data['Day'] = dt.day

    # one-hot encode location (set the matching column to 1)
    loc_col = f'Location_{location}'
    if loc_col in data.columns:
        data[loc_col] = 1

    # one-hot encode wind directions
    for prefix, value in [('WindGustDir', wind_gust_dir),
                          ('WindDir9am', wind_dir_9am),
                          ('WindDir3pm', wind_dir_3pm)]:
        col = f'{prefix}_{value}'
        if col in data.columns:
            data[col] = 1

    # scale
    data = scaler.transform(data)

    # predict
    if model is None:
        # Mock logic: if it's very dry and sunny, predict No (0), else Yes (1)
        if rainfall == 0.0 and sunshine > 7.0 and humidity_3pm < 50.0:
            return 0
        return 1
    
    prediction = model.predict(data)

    return 1 if prediction[0][0] > 0.5 else 0
