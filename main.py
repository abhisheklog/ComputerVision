import cv2 as cv

cap = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    success, img = cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in face_detect:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

    cv.imshow("video", img)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindow