# 🖐️ Sign_Language_Detection
This project detects and recognizes sign language gestures in real-time using Computer Vision and a pre-trained Machine Learning model. The goal is to help bridge communication between sign language users and non-users.

## 📌 Features

✅ Live webcam streaming for gesture detection

✅ Hand detection using cvzone.HandTrackingModule

✅ Gesture classification with a custom-trained Keras model (keras_model.h5)

✅ Gesture list panel with images for reference

✅ Interactive Streamlit web app with user-friendly UI

## 🚀 Tech Stack

*️⃣ Python

*️⃣ Streamlit – for web interface

*️⃣ OpenCV (cv2) – for video processing

*️⃣ cvzone – for hand tracking

*️⃣ TensorFlow/Keras – for model training and inference

*️⃣ NumPy – for array operations

## 📂Project Structure

Sign-Language-Detection/

│

├── app.py                  # Main Streamlit application

├── requirements.txt        # Dependencies

├── README.md               # Project documentation

│

├── Model/                  # Pre-trained model and labels

│   ├── keras_model.h5

│   └── labels.txt

│

├── images/                 # Gesture reference images

│   ├── hello.jpg

│   ├── yes.jpg

│   ├── no.jpg

│   ├── help.jpg

│   └── ...

└── 

## ⚙️ Installation

#### 1)Clone this repository:

```bash
git clone https://github.com/CHENNAMSETTYGURUTEJA/Sign_Language.git
cd Sign_Language
```

#### 2)Create and activate a virtual environment:

```bash
python -m venv env
```

####  Activate it on Windows

```bash
env\Scripts\activate
```

#### Activate it on Mac/Linux
```bash
source env/bin/activate
```

#### 3)Install dependencies:

```bash
pip install -r requirements.txt
```

#### 4)Run the Streamlit app:

```bash
streamlit run app.py
```

## 🎯 Usage

1️⃣ Launch the app.

2️⃣ The gesture list panel on the left shows available gestures with sample images.

3️⃣ Allow webcam access.

4️⃣ Perform any gesture in front of the camera.

5️⃣ The app will display the prediction in real-time.

## 🖼️ Example Output

![IMG_20250908_204944](https://github.com/user-attachments/assets/6217c65f-8509-4a4b-9881-085496a1edef)
![IMG_20250908_204923](https://github.com/user-attachments/assets/3fd9d04d-e9fa-448c-b74f-a0275c5fe795)


