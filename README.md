# minorproject

Air Canvas version 1:
Air Canvas is an innovative virtual drawing application powered by MediaPipe and OpenCV that lets you draw on screen using just your hands. With intuitive gesture recognition, it turns your webcam into an interactive canvas controller.

✨ Features
Gesture-Based Drawing: Use simple hand gestures for intuitive drawing and control.
Real-Time Fingertip Tracking: Smooth and accurate detection using MediaPipe's hand landmark model.

Gesture Modes:
Fist (No fingers visible): No action — canvas remains idle.
Index Finger Only: Enters Selection Mode — switch between marker colors.
Index Finger with Open Palm: Enters Drawing Mode — draw using the fingertip.
Eraser Tool: Use a custom gesture (e.g., two fingers or specific distance) to erase.
Clear Canvas: with open palm, trace your index finger to clear the canvas. 

Customizable Colors and Thickness.
📦 Installation
**Clone the Repository:**
git clone https://github.com/Bhumikalalwani/minorproject.git
cd minorproject
**Install Dependencies:**
Make sure you have Python 3.7+ installed.
pip install opencv-python mediapipe numpy
**Run the App:**
python aircanvas.py

🧪 How It Works
MediaPipe tracks hand landmarks in real-time using your webcam.
Based on which fingers are raised, the system switches between modes.
Drawings are plotted on a transparent canvas overlay and combined with the camera feed.

🛠 To Do / Future Upgrades

Shape selection via gestures (rectangle, circle).
Undo and Redo features.
Dynamic brush thickness via gesture spacing.
GUI-based color palette and exit control.

🤝 Contribution

Feel free to fork and contribute with better gesture recognition, UI enhancements, or performance optimizations.

📜 License
This project is licensed under the MIT License.

