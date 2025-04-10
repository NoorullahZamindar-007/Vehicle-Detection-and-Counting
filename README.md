# Vehicle-Detection-and-Counting
Vehicle Detection and Counting with Flask


---



``markdown
# 🚗 Vehicle Detection and Counting with Flask

This is a Flask-based web application that performs vehicle detection and counting in uploaded video files using OpenCV and Haar Cascade Classifiers.

---

## 🔍 Features

- Upload `.mp4` video files
- Detects cars and buses using Haar Cascades
- Draws bounding boxes frame-by-frame
- Counts total detected vehicles
- Provides processed video for download

---

## 📦 Project Structure

`
vehicle_app/

│
├── static/

│   └── uploads/               # Stores uploaded and processed videos

│

├── templates/

│   └── index.html             # Web UI

│
├── haar_cascades/

│   ├── cars.xml               # Car detection Haar cascade

│   └── Bus_front.xml          # Bus detection Haar cascade

│

├── app.py                     # Flask backend

├── vehicle_detect.py          # Vehicle detection logic

└── README.md                  # This file


``

---

## 💻 Installation

### 1. Clone the repository
`bash
git clone https://github.com/
cd vehicle-detection-flask
``

### 2. Create a virtual environment (optional but recommended)
``bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
``

### 3. Install required packages
``bash
pip install -r requirements.txt
``

### 4. Install OpenCV Haar Cascades
Download `cars.xml` and `Bus_front.xml` and place them in the `haar_cascades/` folder.

---

## ▶️ Run the App

``bash
python app.py
``

Then open your browser and go to:  
**http://127.0.0.1:5000/**

---

## 🧠 Notes

- Output video may not play in-browser. A download link is provided.
- To make the output video browser-playable, integrate `ffmpeg` to convert it to H.264 format.

---

## 📂 Example

![](screenshot.png)

---

## ✨ Future Improvements

- Switch to YOLOv5 or YOLOv8 for more accurate detection
- Add object tracking to avoid double-counting
- Allow playback of output video directly in browser

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).


---

### ✅ Bonus: Create `requirements.txt`
If you don’t already have one, generate it using:
``bash
pip freeze > requirements.txt


---

Let me know if you'd like me to prepare a ZIP of the whole ready-to-upload project, or help you publish this on GitHub step-by-step.
