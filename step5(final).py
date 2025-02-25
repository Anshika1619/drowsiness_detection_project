import cv2
import dlib
import pyttsx3
from scipy.spatial import distance

engine = pyttsx3.init()

cap = cv2.VideoCapture(0)

face_detector = dlib.get_frontal_face_detector()

dlib_facelandmark = dlib.shape_predictor(r"C:\Users\khyathi\Desktop\python.py\shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat")

def Detect_Eye(eye):
    poi_A = distance.euclidean(eye[1], eye[5])
    poi_B = distance.euclidean(eye[2], eye[4])
    poi_C = distance.euclidean(eye[0], eye[3])
    aspect_ratio_Eye = (poi_A + poi_B) / (2 * poi_C)
    return aspect_ratio_Eye

eye_aspect_ratio_threshold = 0.3  
eye_closed_frames = 0  
total_frames = 0  
perclos_window = 30  

while True:
    null, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector(gray_scale)

    for face in faces:
        face_landmarks = dlib_facelandmark(gray_scale, face)
        leftEye = [] 
        rightEye = [] 

        for n in range(42, 48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x, y))
            next_point = n + 1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

        for n in range(36, 42):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x, y))
            next_point = n + 1
            if n == 41:
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (255, 255, 0), 1)

        right_Eye = Detect_Eye(rightEye)
        left_Eye = Detect_Eye(leftEye)
        Eye_Rat = (left_Eye + right_Eye) / 2

        Eye_Rat = round(Eye_Rat, 2)

        cv2.putText(frame, f"EAR: {Eye_Rat}", (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

        if Eye_Rat < eye_aspect_ratio_threshold:
            eye_closed_frames += 1  
            cv2.putText(frame, "blinking", (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
            

        total_frames += 1  

        if total_frames % perclos_window == 0:
            perclos = (eye_closed_frames / perclos_window) * 100
            print(f"PERCLOS: {perclos:.2f}%")

            if perclos > 70:
                cv2.putText(frame, "drowsiness detected", (50, 200),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
                engine.say(" wakeUp dude!Please stay alert!")
                engine.runAndWait()

            eye_closed_frames = 0
            total_frames = 0

    cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
    
    key = cv2.waitKey(9)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
