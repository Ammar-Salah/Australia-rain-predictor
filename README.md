# 🌧️ Rain Tomorrow Predictor

This is a machine learning web application built with Streamlit that predicts whether it will rain tomorrow in various locations across Australia, based on today's weather parameters. It uses a trained Artificial Neural Network (ANN) model built with TensorFlow/Keras.

## 🚀 Features

- Interactive web interface using **Streamlit**.
- Predictive modeling using a pre-trained **TensorFlow/Keras** ANN (`weather_ann_model.keras`).
- Pre-processing utilizing scikit-learn's `StandardScaler` and `LabelEncoder`.
- Configurable inputs including Temperature, Rainfall, Sunshine, Wind Direction/Speed, Humidity, and Pressure.

## 📸 Screenshots

<img width="1366" height="614" alt="image" src="https://github.com/user-attachments/assets/714d1368-2d23-4ea5-bafc-32c125e67193" />
<img width="1357" height="621" alt="image" src="https://github.com/user-attachments/assets/5f4eca3b-dd56-4452-9adf-3df7baa70e9d" />
<img width="1359" height="78" alt="image" src="https://github.com/user-attachments/assets/38f2bb73-4944-4d73-9039-95ab7bb004ba" />




## 📦 Project Structure

- `app.py`: The main Streamlit web application script defining the UI.
- `main.py`: Contains the logic for parsing user inputs, applying preprocessing (scaling and encoding), and querying the ML model.
- `weather_ann_model.keras` & `weather_ann_model.h5`: The saved pre-trained TensorFlow/Keras neural network models.
- `scaler.pkl`: Pickled `StandardScaler` used to scale numerical features during inference.
- `label_encoder.pkl`: Pickled `LabelEncoder` for categorical variables.
- `weatherAUS.csv`: The dataset containing historical daily weather observations from Australia.
- `requirements.txt`: List of Python dependencies required to run the project.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ammar-Salah/Australia-rain-predictor.git
   cd Australia-rain-predictor
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: If you are on Windows and face a "Long Path" error when installing `tensorflow`, you may need to [enable long paths in the Windows Registry](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry).)*

## 🖥️ Running the Application

Once the dependencies are installed, you can launch the app by running:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 📝 Usage

1. Select the **Date** and **Location** (e.g., Cobar, Sydney, etc.).
2. Enter the current weather parameters (Min/Max temp, Wind, Humidity, Pressure, Cloud Cover, etc.).
3. Click the **Predict** button at the bottom of the page.
4. The model will instantly calculate and display whether it's likely to rain tomorrow!

## ⚠️ Troubleshooting

- **`ModuleNotFoundError: No module named 'tensorflow'`:** This means TensorFlow didn't install correctly. Ensure your virtual environment is activated and try running `pip install tensorflow` again.
- **Model Loading Issues:** The app requires `weather_ann_model.keras`, `scaler.pkl`, and `label_encoder.pkl` to be present in the root directory. Ensure they are downloaded or exist in the repo.
