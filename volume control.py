import cv2
import mediapipe as mp
import math
import numpy as np
import os
# Initialize the MediaPipe hands module
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Get the current volume range
minVol, maxVol, volBar, volPer = 0.0, 100.0, 400, 0

# Setup the camera
wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)

def set_system_volume(volume):
    volume = int(volume)
    osascript_command = f"osascript -e 'set volume output volume {volume}'"
    os.system(osascript_command)

print("Sharan G S")
# Initialize the MediaPipe Hands
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while cam.isOpened():
        success, image = cam.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Convert the BGR image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and find the hand landmarks
        results = hands.process(image)

        # Convert the image color back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw the hand landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

                # Extract the landmark list
                lmList = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

                if lmList:
                    # Get the coordinates of the thumb tip and index finger tip
                    x1, y1 = lmList[4][1], lmList[4][2]
                    x2, y2 = lmList[8][1], lmList[8][2]

                    # Draw circles on the thumb tip and index finger tip
                    cv2.circle(image, (x1, y1), 15, (255, 255, 255), cv2.FILLED)
                    cv2.circle(image, (x2, y2), 15, (255, 255, 255), cv2.FILLED)
                    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

                    # Calculate the distance between the thumb tip and index finger tip
                    length = math.hypot(x2 - x1, y2 - y1)

                    # Interpolate the volume based on the length
                    vol = np.interp(length, [50, 220], [minVol, maxVol])

                    # Set the system volume
                    set_system_volume(vol)
                    volBar = np.interp(length, [50, 220], [400, 150])
                    volPer = np.interp(length, [50, 220], [0, 100])

                    # Draw the volume bar
                    cv2.rectangle(image, (50, 150), (85, 400), (0, 0, 0), 3)
                    cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 0, 255), cv2.FILLED)
                    cv2.putText(image, f'{int(volPer)} %', (60, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Display the image
        cv2.imshow('Volume Control', image)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()

print("Sharan G S")