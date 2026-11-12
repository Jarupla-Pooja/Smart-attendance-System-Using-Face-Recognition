# Smart Attendance System Using Face Recognition

## 📌 Project Overview

The **Smart Attendance System** is a Python-based application developed to automate student attendance using real-time face detection and recognition. The system uses a webcam to capture student faces, identifies registered students, and automatically records their attendance.

It reduces manual attendance work and maintains digital attendance records with student details, subject, date, and time.

## 🎯 Objectives

- Automate the traditional attendance process.
- Detect and recognize student faces using a webcam.
- Maintain student face datasets for recognition.
- Record attendance automatically.
- Avoid duplicate attendance entries during a session.
- Store attendance records digitally in CSV format.
- Provide an interface to view previous attendance records.

## 🛠️ Technologies & Tools Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Image processing and face recognition |
| Haar Cascade | Real-time face detection |
| LBPH Face Recognizer | Face recognition |
| NumPy | Numerical operations and label handling |
| Tkinter | Graphical User Interface |
| CSV | Attendance data storage |
| Webcam | Live face capture |

## ⚙️ Key Features

1. **Face Detection:** Detects student faces using the Haar Cascade classifier.
2. **Face Recognition:** Identifies registered students using the LBPH algorithm.
3. **Dataset Collection:** Captures and stores multiple face images for each student.
4. **Model Training:** Trains the recognition model using collected face images.
5. **Real-Time Attendance:** Recognizes students through a webcam and records attendance.
6. **Subject Selection:** Allows attendance to be recorded for different subjects.
7. **Duplicate Prevention:** Prevents the same student from being marked repeatedly for the same subject during a session.
8. **Attendance Storage:** Saves student roll number, name, subject, date, and time in a CSV file.
9. **Attendance Viewing:** Provides an option to view previously recorded attendance.

## 🔄 Project Workflow

1. Capture student face images using a webcam.
2. Store the collected images in the dataset.
3. Train the face recognition model using LBPH.
4. Load the trained model and student labels.
5. Open the webcam for real-time face detection.
6. Recognize registered students.
7. Select the required subject.
8. Record attendance after successful recognition.
9. Save the attendance details in a CSV file.

## 📂 Project Structure

```text
Smart-Attendance-System/
│
├── dataset/
│   └── Student face images
│
├── capture.py
├── train.py
├── attendance.py
├── view_attendance.py
│
├── trained_model.yml
├── labels.npy
├── attendance.csv
│
└── README.md
```

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Gauri-V12/Smart-Attendance-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Smart-Attendance-System
```

### 3. Install Required Libraries

```bash
pip install opencv-contrib-python numpy
```

### 4. Run the Project

First, collect student face images:

```bash
python capture.py
```

Next, train the face recognition model:

```bash
python train.py
```

Finally, start the attendance system:

```bash
python attendance.py
```

To view previous attendance records:

```bash
python view_attendance.py
```

## 📊 Attendance Record Format

Attendance is stored in CSV format with the following fields:

| Roll Number | Student Name | Subject | Date | Time |
|---|---|---|---|---|
| Student Roll No. | Student Name | Maths | YYYY-MM-DD | HH:MM:SS |

## 📚 Concepts Applied

- Computer Vision
- Image Processing
- Face Detection
- Face Recognition
- Haar Cascade Classifier
- Local Binary Patterns Histograms (LBPH)
- Real-Time Video Processing
- Python File Handling
- CSV Data Management
- Graphical User Interface Development

## 🚀 Future Enhancements

- Generate downloadable attendance reports in PDF format.
- Add student and administrator management features.
- Extend the system to support larger student datasets.
- Improve recognition performance under different lighting conditions.
- Introduce centralized attendance management.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in Python programming, OpenCV, computer vision, face detection, face recognition, model training, GUI development, and automated data management.

This project helped me understand how Python and computer vision techniques can be applied to solve real-world problems.

⭐ If you find this project interesting, feel free to explore the repository!
