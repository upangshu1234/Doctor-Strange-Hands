Doctor Strange Magic Circle Effect using OpenCV & MediaPipe
This project uses OpenCV and MediaPipe to create a real-time Doctor Strange-inspired magic circle effect using hand tracking. It captures hand landmarks, calculates distances between fingers, and overlays spinning magic circles when the user forms a specific hand gesture.

Libraries Used
To run this project, install the following dependencies:

bash
Copy
Edit
pip install opencv-python mediapipe numpy
How It Works
Hand Tracking: Uses MediaPipe to track hand landmarks in real time.
Gesture Detection: Calculates the ratio of the index fingertip and pinky fingertip distance to the wrist-index MCP distance.
Magic Effect Activation:
If the ratio is between 0.5 and 1.3, lines are drawn between key hand points.
If the ratio is greater than 1.3, the magic circle effect appears at the middle finger MCP position.
Rotating Magic Circles: Two transparent PNG images (clockwise and counterclockwise magic circles) are overlaid and rotated dynamically.
Camera Feed Processing: The program captures real-time video, processes frames, and renders the augmented effect.
Key Features
✅ Real-time Hand Tracking using MediaPipe
✅ Dynamic Gesture Recognition to trigger effects
✅ Transparent Magic Circles overlay using OpenCV
✅ Rotating Effects for an animated visual

Future Improvements
Improve gesture recognition for more precise control.
Add multi-hand support for dual magic circles.
Enhance visual effects with OpenCV filters.
