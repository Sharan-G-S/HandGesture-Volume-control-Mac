# HandGesture-Volume-control-Mac

#Sharan G S

# System Volume Control Using Hand Gestures

This project implements a system volume control for macOS using hand gestures. It utilizes OpenCV and MediaPipe libraries to detect hand landmarks and adjusts the system volume based on the distance between the thumb and index finger.

## Features
- Real-time hand tracking using a webcam.
- Gesture-based volume adjustment.
- Smooth interpolation for precise volume control.
- Visual feedback with a volume bar.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.7 or higher
- OpenCV (`cv2`)
- MediaPipe
- NumPy
- macOS operating system (for system volume control via AppleScript)

Install the required Python libraries with:
```bash
pip install opencv-python mediapipe numpy
```

## How It Works
1. The script initializes the webcam and the MediaPipe Hands module for detecting hand landmarks.
2. It calculates the distance between the thumb tip and the index finger tip.
3. The distance is mapped to the system volume range (0-100%).
4. The system volume is updated dynamically using an AppleScript command.
5. A visual volume bar is displayed on the screen, providing feedback on the current volume level.

## Usage

1. Clone or download the repository containing the script.
2. Open a terminal and navigate to the script's directory.
3. Run the script using:
   ```bash
   python volume_control.py
   ```
4. Allow access to the webcam if prompted.
5. Adjust the system volume by moving your thumb and index finger closer or farther apart.
6. Press `q` to exit the application.

#Sharan G S

## Notes
- The script is designed for macOS. Modifications will be required to make it work on other operating systems.
- Ensure that your webcam is functioning and that there is enough light for proper hand tracking.
- The distance thresholds and volume mappings can be adjusted in the code as needed.

## Troubleshooting
- If the webcam feed does not appear, ensure no other application is using the webcam.
- If hand tracking is not working, check lighting conditions and ensure your hand is within the camera's frame.
- If volume control is not working, verify that AppleScript commands are enabled on your macOS.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

#Sharan G S
