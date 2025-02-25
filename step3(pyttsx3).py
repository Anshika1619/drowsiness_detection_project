import pyttsx3
import cv2

engine = pyttsx3.init()

def trigger_alert():
    print("Drowsiness detected!")
    engine.say("Please stay alert!")
    engine.runAndWait()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.putText(frame, "drowsiness detected", (50, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

    key = cv2.waitKey(1)
    if key == ord("d"):  
        trigger_alert()

    cv2.imshow("Drowsiness Alert System", frame)

    if key == 27:  
        break

cap.release()
cv2.destroyAllWindows()
  