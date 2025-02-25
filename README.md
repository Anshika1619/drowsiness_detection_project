
Drowsiness Detection System

Overview
This project is a real-time drowsiness detection system using computer vision and machine learning techniques. It monitors the driver's eye movements to detect signs of fatigue or drowsiness. If the system detects that the driver is at risk of falling asleep, it triggers an alert using text-to-speech and visual cues on the screen. This project is implemented using OpenCV, dlib, and pyttsx3 for real-time face and eye tracking.

Features
Real-time Eye Aspect Ratio (EAR) Calculation: Calculates the Eye Aspect Ratio (EAR) to monitor eyelid movements.
Drowsiness Detection: When the eye aspect ratio falls below a certain threshold, indicating a potential eye closure or drowsiness, the system triggers an alert.
Alert System: When drowsiness is detected, a spoken alert is generated using pyttsx3, along with a visual cue on the screen.
Visual Feedback: Displays the EAR value and alerts the user about blinking and drowsiness.

Requirements
Python 3.x
OpenCV
dlib
pyttsx3
SciPy

How it Works
Face Detection: The system uses dlib's frontal face detector to identify faces in the camera feed.
Landmark Detection: It then detects facial landmarks using a pre-trained dlib model (shape_predictor_68_face_landmarks.dat).
Eye Detection: The system isolates the eye landmarks (from the facial landmarks) to analyze eye movements.
Eye Aspect Ratio (EAR): The Eye Aspect Ratio (EAR) is computed to determine if the eyes are open or closed. A threshold value is used to detect eye closures, indicating drowsiness.
Alert Mechanism: If the EAR falls below a threshold for a defined number of frames, the system detects drowsiness and generates an alert.
PERCLOS Calculation: The system calculates the PERCLOS (Percentage of Eye Closure) over a window of frames. If the PERCLOS exceeds a certain threshold (e.g., 70%), an alert is triggered.

How to Use
Download the necessary files:
You need the dlib face landmark model, shape_predictor_68_face_landmarks.dat. Download it and place it in the same directory as the Python script.
Monitor the Output:
The camera feed will display, and the system will monitor eye movements.
If the system detects drowsiness (based on eye closures), it will alert the driver both visually (on the screen) and audibly (via text-to-speech).
Exit:
Press ESC to close the camera window and stop the program.

Code Explanation
Detect_Eye function: This function calculates the Eye Aspect Ratio (EAR) using the distance between key points of the eye.
Main Loop: The camera feed is processed frame by frame, where face detection and eye aspect ratio calculations occur. Alerts are generated if drowsiness is detected based on the PERCLOS score.
Troubleshooting
Camera Access: Ensure that your webcam is properly connected and accessible by OpenCV.
Shape Predictor File: Ensure the shape_predictor_68_face_landmarks.dat file is correctly downloaded and the path is provided correctly in the script.
