import cv2
import os
import time

roll = input("Enter Roll Number: ")
name = input("Enter Name: ")

person_id = roll + "_" + name

if not os.path.exists("dataset"):
    os.mkdir("dataset")

person_path = os.path.join("dataset", person_id)
if not os.path.exists(person_path):
    os.mkdir(person_path)

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("ERROR: Camera not opened")
    exit()

time.sleep(2)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0
print("Look straight at the camera. Only ONE face should be visible.")

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lighting normalization
    gray = cv2.equalizeHist(gray)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=7,
        minSize=(100, 100)
    )

    # Only capture if exactly one face
    if len(faces) == 1:
        (x, y, w, h) = faces[0]

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (200, 200))

        count += 1
        cv2.imwrite(f"{person_path}/{count}.jpg", face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        time.sleep(0.4)

    cv2.putText(frame, f"Images: {count}/30", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Face Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 30:
        break

cam.release()
cv2.destroyAllWindows()
print("Dataset created successfully")