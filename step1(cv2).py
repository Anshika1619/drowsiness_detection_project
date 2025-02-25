import cv2
import dlib
import pyttsx3
from scipy.spatial import distance

engine = pyttsx3.init()

# SETTING UP OF CAMERA TO 1 YOU
cap = cv2.VideoCapture(0)

while True:
	null, frame = cap.read()
	gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
	key = cv2.waitKey(9)
	if key == 27:
		break
cap.release()
cv2.destroyAllWindows()
