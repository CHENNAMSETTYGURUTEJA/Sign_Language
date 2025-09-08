# 🖐️ Sign_Language_Detection
This project detects and recognizes sign language gestures in real-time using Computer Vision and a pre-trained Machine Learning model. The goal is to help bridge communication between sign language users and non-users.

## 📌 Features

> Live webcam streaming for gesture detection

> Hand detection using cvzone.HandTrackingModule

> Gesture classification with a custom-trained Keras model (keras_model.h5)

> Gesture list panel with images for reference

> Interactive Streamlit web app with user-friendly UI

## 🚀 Tech Stack

>Python

>Streamlit – for web interface

>OpenCV (cv2) – for video processing

>cvzone – for hand tracking

>TensorFlow/Keras – for model training and inference

>NumPy – for array operations

## 📂Project Structure
The project is organized as follows:

>Model/ → Contains the pre-trained model and gesture labels

>>keras_model.h5 → Trained deep learning model for gesture recognition

>>labels.txt → List of gesture names used for classification

>images/ → Reference images of gestures for the left-side panel in the UI

>>Example: hello.jpg, yes.jpg, no.jpg, etc.

>app.py → Main Streamlit application file (runs the real-time detection app)

>requirements.txt → List of dependencies needed to run the project

>README.md → Project documentation (this file)

## ⚙️ Installation

### 1)Clone this repository:

git clone https://github.com/CHENNAMSETTYGURUTEJA/Sign_Language.git

cd Sign_Language

### 2)Create and activate a virtual environment:

python -m venv env

####  Activate it on Windows

env\Scripts\activate

#### Activate it on Mac/Linux

source env/bin/activate

### 3)Install dependencies:

pip install -r requirements.txt


### 4)Run the Streamlit app:

streamlit run app.py

## 🎯 Usage

>Launch the app.

>The gesture list panel on the left shows available gestures with sample images.

>Allow webcam access.

>Perform any gesture in front of the camera.

>The app will display the prediction in real-time.

## 🖼️ Example Output

![IMG_20250908_205009 1](https://github.com/user-attachments/assets/98c00cb2-3a71-44c6-94cc-87489259c0cd)

