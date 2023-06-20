import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

vid = cv2.VideoCapture(0)

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while(True):
    ret, frame = vid.read()
    if ret is False:
        break
    faces = detect_bounding_box(
        frame
    )
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

vid.release()
cv2.destroyAllWindows()
