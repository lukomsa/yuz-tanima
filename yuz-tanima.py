import cv2

# Haar cascade dosyalarını yükleyin
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        if len(smiles) > 0:
            cv2.putText(frame, "Gulumsuyor", (x, y+h+40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 5)
            cv2.putText(frame, "Gulumsuyor", (x, y+h+40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        else:
            cv2.putText(frame, "Normal", (x, y+h+40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 5)
            cv2.putText(frame, "Normal", (x, y+h+40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    return frame

# Kamera başlat
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
