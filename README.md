# 🎥 OpenCV Motion Detection System

A real-time motion detection application built using **Python**, **OpenCV**, **Pandas**, and **Bokeh**. The system detects moving objects through a webcam, records the motion timestamps, stores them in a CSV file, and generates an interactive timeline visualization in HTML.

---

## 📌 Overview

This project uses computer vision techniques to detect movement in front of a webcam. Whenever motion is detected, the application records the start and end time of the event. These events are stored in a CSV file and later visualized as an interactive timeline using Bokeh.

This project is suitable for beginners learning:

- OpenCV
- Image Processing
- Motion Detection
- Data Visualization
- Computer Vision
- Python Projects

---

## ✨ Features

- 📷 Real-time webcam motion detection
- 🟢 Bounding box around detected objects
- ⏱ Automatically records motion start and end time
- 📄 Saves motion logs to CSV
- 📊 Interactive motion timeline using Bokeh
- 🖱 Hover to view event details
- 📈 Displays total motion events and total duration
- 🔄 Automatically adapts to lighting changes
- ❌ Press **Q** to quit the application

---

## 📂 Project Structure

```
OpenCV-Motion-Detection-System/
│
├── app.py                 # Motion detection application
├── graph.py               # Generates interactive motion graph
├── Times.csv              # Motion event log
├── Graph1.html            # Interactive timeline graph
├── requirements.txt
├── README.md
└── screenshots/
    ├── detection.png
    ├── graph.png
```

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Motion Detection |
| Pandas | Data Storage & Processing |
| Bokeh | Interactive Visualization |
| Datetime | Timestamp Recording |

---

## ⚙ How It Works

1. The webcam captures live video.
2. The first frame is stored as the reference background.
3. Each new frame is converted to grayscale and blurred.
4. The current frame is compared with the reference frame.
5. Thresholding and contour detection identify moving objects.
6. When motion starts, the current timestamp is recorded.
7. When motion stops, the ending timestamp is recorded.
8. Motion events are saved to **Times.csv**.
9. **graph.py** reads the CSV and creates an interactive HTML graph.

---

## 📷 Motion Detection Pipeline

```
Webcam
   │
   ▼
Capture Frame
   │
   ▼
Grayscale Conversion
   │
   ▼
Gaussian Blur
   │
   ▼
Frame Difference
   │
   ▼
Thresholding
   │
   ▼
Dilation
   │
   ▼
Contour Detection
   │
   ▼
Motion Detected
   │
   ▼
Record Start & End Time
   │
   ▼
Save to CSV
   │
   ▼
Generate Interactive Graph
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/OpenCV-Motion-Detection-System.git
```

### Navigate into Project

```bash
cd OpenCV-Motion-Detection-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install opencv-python pandas bokeh
```

---

## ▶ Run the Motion Detector

```bash
python app.py
```

Press **Q** to stop detection.

---

## 📊 Generate Motion Timeline

```bash
python graph.py
```

This generates:

```
Graph1.html
```

Open the HTML file in your browser to view the interactive motion timeline.

---

## 📄 Sample CSV Output

```
Start,End
2026-05-13 10:53:07.329248,2026-05-13 10:53:07.376224
2026-05-13 10:53:08.334424,2026-05-13 10:53:08.368061
2026-05-13 10:53:09.326435,2026-05-13 10:53:09.472226
```

---

## 📈 Interactive Graph Features

- Motion timeline
- Zoom and pan
- Hover tooltips
- Motion duration
- Motion start time
- Motion end time
- Total motion events
- Total motion duration
- Date summary

---

## 📸 Screenshots

### Motion Detection

Add your screenshot here.

```
screenshots/detection.png
```

---

### Motion Timeline

Add your generated graph screenshot here.

```
screenshots/graph.png
```

---

## 📚 Concepts Used

- Background Subtraction
- Frame Differencing
- Gaussian Blur
- Image Thresholding
- Contour Detection
- Bounding Rectangle
- Motion Tracking
- CSV File Handling
- Interactive Data Visualization

---

## 🚀 Future Improvements

- Email notification on motion detection
- Save captured images automatically
- Video recording during motion
- Multi-camera support
- Face detection integration
- Person detection using YOLO
- Motion sensitivity adjustment
- GUI using Tkinter or PyQt
- SQLite/MySQL database integration
- Live dashboard using Streamlit

---

## 📋 Requirements

```
Python 3.9+
opencv-python
pandas
bokeh
```

---

## requirements.txt

```
opencv-python
pandas
bokeh
```

---

## 👨‍💻 Author

**Subhranshu Kumar Parhi**

Machine Learning | Computer Vision | Deep Learning | Python Developer

---

## ⭐ If you found this project useful, please consider giving it a star on GitHub!
