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
Sign-Language-Detection/
│── Model/
│   ├── keras_model.h5        # Pre-trained model
│   ├── labels.txt            # Gesture labels
│
│── images/                   # Gesture reference images
│   ├── hello.jpg
│   ├── yes.jpg
│   ├── no.jpg
│   └── ...
│
│── app.py                    # Main Streamlit app
│── requirements.txt          # Dependencies
│── README.md                 # Project documentation

## ⚙️ Installation

### Clone this repository:

git clone https://github.com/your-username/sign-language-detection.git
cd sign-language-detection


### Install dependencies:

pip install -r requirements.txt


### Run the Streamlit app:

streamlit run app.py

## 🎯 Usage

>Launch the app.

>The gesture list panel on the left shows available gestures with sample images.

>Allow webcam access.

>Perform any gesture in front of the camera.

>The app will display the prediction in real-time.

## 🖼️ Example Output

Gesture: "Yes" → Prediction displayed on screen.

Gesture: "Help" → Model recognizes and highlights it.
