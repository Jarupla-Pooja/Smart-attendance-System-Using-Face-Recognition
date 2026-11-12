import cv2
import numpy as np
import os
from datetime import datetime
import csv
import tkinter as tk
from tkinter import ttk

# ---------------- LOAD MODEL ----------------
recognizer = cv2.face.LBPHFaceRecognizer_create(
    radius=2,
    neighbors=8,
    grid_x=8,
    grid_y=8
)

recognizer.read("trained_model.yml")
labels = np.load("labels.npy", allow_pickle=True).item()

# ---------------- ATTENDANCE FILE ----------------
attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Roll", "Name", "Subject", "Date", "Time"])

marked_students = set()
face_count = {}

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("900x500")

# -------- SUBJECT DROPDOWN --------
subjects = ["Maths", "Physics", "AI", "ML", "OS"]
selected_subject = tk.StringVar()
selected_subject.set(subjects[0])

tk.Label(root, text="Select Subject:", font=("Arial", 12)).pack()
tk.OptionMenu(root, selected_subject, *subjects).pack(pady=5)

# -------- TABLE --------
columns = ("Roll", "Name", "Subject", "Date", "Time")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill="both", expand=True, pady=10)

# -------- VIEW PREVIOUS RECORDS --------
def view_records():
    view_window = tk.Toplevel(root)
    view_window.title("Attendance Records")
    view_window.geometry("900x400")

    view_tree = ttk.Treeview(view_window, columns=columns, show="headings")

    for col in columns:
        view_tree.heading(col, text=col)
        view_tree.column(col, width=150)

    view_tree.pack(fill="both", expand=True)

    with open("attendance.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            view_tree.insert("", "end", values=row)

tk.Button(root, text="View Previous Attendance", command=view_records).pack(pady=5)

# ---------------- FACE DETECTOR ----------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)

print("Recognition Started... Press Q or Close Window to quit")

# -------- RUNNING FLAG FOR SMOOTH CLOSE --------
running = True

def close_app():
    global running
    running = False

root.protocol("WM_DELETE_WINDOW", close_app)

# ---------------- RECOGNITION LOOP ----------------
while running:
    ret, frame = cam.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=7,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        label_id, confidence = recognizer.predict(face)

        if confidence < 60:
            full_name = labels[label_id]
            roll, name = full_name.split("_")
        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({int(confidence)})",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2)

        if name != "Unknown":
            key = name + "_" + selected_subject.get()
            face_count[key] = face_count.get(key, 0) + 1

            if face_count[key] >= 5 and key not in marked_students:
                marked_students.add(key)

                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time_now = now.strftime("%H:%M:%S")

                with open(attendance_file, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([roll, name, selected_subject.get(), date, time_now])

                tree.insert("", "end", values=(roll, name, selected_subject.get(), date, time_now))

                print(f"Attendance marked: {name} - {selected_subject.get()}")

    cv2.imshow("Smart Attendance - Press Q to quit", frame)

    root.update()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        running = False

# -------- CLEAN EXIT --------
cam.release()
cv2.destroyAllWindows()
root.destroy()