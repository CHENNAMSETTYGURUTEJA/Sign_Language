import streamlit as st
import cv2
import numpy as np
import math
import time
import base64
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from pathlib import Path

# -------- User config: update these paths if needed ----------
MODEL_PATH = "Sign-Language-detection\\Model\\keras_model.h5"   # put keras model file here
LABELS_PATH = "Sign-Language-detection\\Model\\labels.txt"   # put labels file here
IMAGES_DIR = Path("Sign-Language-detection\\images")   # put images like images/hello.jpg, images/home.jpg ...
# ------------------------------------------------------------

st.set_page_config(page_title="Sign Language Detection", layout="wide")

# ============================================================
# SECTION 1: GLOBAL STYLES (CSS)
# ============================================================
st.markdown(
    """
    <style>
      .title-box {
        background: #3aa05a;
        color: white;
        padding: 18px 36px;
        font-weight:700;
        border-radius: 18px;
        display:inline-block;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        margin-top: -40px;
        margin-bottom: 14px;
        font-size: 28px;
      }
      .card {
        background: #f7fafc;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
        box-shadow: 0 6px 18px rgba(17,24,39,0.06);
        display:flex;
        align-items:center;
        justify-content:space-between;
      }
       .pill {
        background:#4caf50;
        color:white;
        padding:10px 16px; 
        font-weight:700;        
        font-size: 16px;
        display:flex;
        align-items:center;    
        justify-content:center;  
        text-align:center;
        max-width: 140px;       
        overflow: hidden;        
        text-overflow: ellipsis; 
        white-space: nowrap;
      }
      .imgbox {
        width: 120px;        
        height: 120px;      
        overflow:hidden;
        background: white;
        display:inline-flex;
        align-items:center;
        justify-content:center;
      }
      .welcome {
    font-size: 22px;
    font-weight: bold;
    color: navy;
    margin-top: -30px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.2); 
     .sub {
    color: #475569;
    margin-top: -15px;   
    font-size: 18px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# SECTION 2: LOAD LABELS & GESTURE IMAGES
# ============================================================
if Path(LABELS_PATH).exists():
    with open(LABELS_PATH, "r") as f:
        labels = [line.strip() for line in f.readlines() if line.strip()]
else:
    labels = [
    "Hello",
    "OK"
    "Home",
    "I Love You",
    "Thank You",
    "Sorry",
    "Accident",
    "Danger",
    "Call",
    "Fire",
    "Pain",
    "Help",
    "No",
    "Yes",
    "Police",
    "Request",
    "Tension",
    "Thief",
    "Sad",
    "Anger"
]

gestures = []
for lab in labels:
    found = None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        candidate = IMAGES_DIR / (lab.replace(" ", "_").lower() + ext)
        if candidate.exists():
            found = candidate
            break
    gestures.append((lab, str(found) if found else None))

# ============================================================
# SECTION 3: SESSION STATE KEYS
# ============================================================
if "run_stream" not in st.session_state:
    st.session_state["run_stream"] = False
if "selected_gesture" not in st.session_state:
    st.session_state["selected_gesture"] = None

# ============================================================
# SECTION 4: PAGE LAYOUT (LEFT LIST + MAIN)
# ============================================================
left_col, main_col = st.columns([1,3])

# ============================================================
# SECTION 5: LEFT COLUMN → GESTURE LIST CARDS
# ============================================================
with left_col:
    st.markdown("#### Sign Language Gesture List")
    st.write("")  # space
    for lab, imgpath in gestures:
        img_b64 = ""
        if imgpath:
            try:
                with open(imgpath, "rb") as f:
                    img_b64 = base64.b64encode(f.read()).decode("utf-8")
            except Exception:
                img_b64 = ""
        card_html = f"""
        <div class="card">
          <div style="flex:1;padding-right:12px">
            <div class="pill">{lab}</div>
          </div>
          <div class="imgbox">
            {"<img src='data:image/png;base64," + img_b64 + "' style='width:100%;height:100%;object-fit:cover;'/>" if img_b64 else "<div style='color:#94a3b8;font-size:12px'>No image</div>"}
          </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

# ============================================================
# SECTION 6: MAIN COLUMN → HEADER + WELCOME TEXT
# ============================================================
with main_col:
    st.markdown("<div style='text-align:center;'><span class='title-box'>SIGN LANGUAGE DETECTION</span></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<div style='text-align:center;' class='welcome'>Welcome to the Sign Language Recognition App!</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;' class='sub'>This app recognizes sign language gestures in real-time using a pre-trained machine learning model.</div>", unsafe_allow_html=True)
    st.write("")

# ============================================================
# SECTION 7: SELECTED GESTURE PREVIEW
# ============================================================
    preview_cols = st.columns([1, 2])

# ============================================================
# SECTION 8: VIDEO STREAM PLACEHOLDER (CENTERED, NO BUTTONS)
# ============================================================
    center_cols = st.columns([1, 2, 1])
    video_placeholder = center_cols[1].empty()

    st.session_state["run_stream"] = True  
    stop_cols = st.columns([1, 2, 1])
    with stop_cols[1]:
        if st.button("⏹️ Stop Stream", key="stop_stream"):
            st.session_state["run_stream"] = False
# ============================================================
# SECTION 10: VIDEO STREAM DISPLAY
# ============================================================
    if not st.session_state["run_stream"]:
        video_placeholder.image(np.zeros((480, 640, 3), dtype=np.uint8) + 220, channels="RGB") 
    else:
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not cap.isOpened():
            st.error("Cannot open webcam. Check permissions or camera index.")
            st.session_state["run_stream"] = False
        else:
            try:
                detector = HandDetector(maxHands=1)
                classifier = Classifier(MODEL_PATH, LABELS_PATH)
                counter = 0
                while st.session_state["run_stream"]:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    imgOutput = frame.copy()
                    hands, _img = detector.findHands(frame, draw=False)
                    if hands:
                        hand = hands[0]
                        x, y, w, h = hand["bbox"]
                        offset = 20
                        imgSize = 300

                        x1 = max(0, x - offset)
                        y1 = max(0, y - offset)
                        x2 = min(frame.shape[1], x + w + offset)
                        y2 = min(frame.shape[0], y + h + offset)
                        imgCrop = frame[y1:y2, x1:x2]

                        if imgCrop.size != 0:
                            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
                            aspectRatio = (y2 - y1) / (x2 - x1 + 1e-6)

                            if aspectRatio > 1:
                                k = imgSize / (y2 - y1)
                                wCal = math.ceil(k * (x2 - x1))
                                wCal = max(wCal, 1)
                                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                                wGap = math.ceil((imgSize - wCal) / 2)
                                imgWhite[:, wGap:wCal + wGap] = imgResize
                            else:
                                k = imgSize / (x2 - x1)
                                hCal = math.ceil(k * (y2 - y1))
                                hCal = max(hCal, 1)
                                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                                hGap = math.ceil((imgSize - hCal) / 2)
                                imgWhite[hGap:hCal + hGap, :] = imgResize

                            try:
                                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                                predicted_label = labels[index] if 0 <= index < len(labels) else "Unknown"
                            except Exception:
                                predicted_label = "Error"
                                index = 0

                            cv2.rectangle(imgOutput, (x1, y1), (x2, y2), (0, 200, 0), 3)

                            text = f"Prediction: {predicted_label}"
                            font = cv2.FONT_HERSHEY_COMPLEX
                            font_scale = 1  
                            thickness = 2 
                            (text_w, text_h), baseline = cv2.getTextSize(text, font, font_scale, thickness)

                            box_x, box_y = 5, 5 
                            box_w, box_h = text_w + 20, text_h + 20

                            cv2.rectangle(imgOutput, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 0, 0), -1)

                            cv2.putText(imgOutput, text, (box_x + 10, box_y + text_h + 5),
                                font, font_scale, (255, 255, 255), thickness)


                    imgRGB = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2RGB)
                    video_placeholder.image(imgRGB, channels="RGB")
                    time.sleep(0.02)

            except Exception as e:
                st.error(f"Stream error: {e}")
            finally:
                cap.release()
                st.session_state["run_stream"] = False

    if st.session_state["run_stream"]:
        if st.button("Stop Stream", key="stop_stream"):
            st.session_state["run_stream"] = False
