#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.9)

cap = cv2.VideoCapture(0)

# Create a blank white canvas
canvas = 255 * np.ones(shape=[720, 1280, 3], dtype=np.uint8)

# Default drawing color
current_color = (0, 0, 255)  # Red

# Define button positions & colors
buttons = {
    "Red": ((50, 50), (150, 100), (0, 0, 255)),
    "Green": ((180, 50), (280, 100), (0, 255, 0)),
    "Blue": ((310, 50), (410, 100), (255, 0, 0)),
    "Yellow": ((440, 50), (540, 100), (0, 255, 255)),
    "Erase": ((570, 50), (670, 100), (200, 200, 200)),  # Gray for Eraser
    "Clear": ((700, 50), (850, 100), (255, 255, 255))  # White for Clear
}

# Store points with color history
points_with_colors = []
erase_mode = False  # Track whether erase mode is on

# Function to check if a button was clicked
def check_button_click(x, y):
    global current_color, canvas, erase_mode
    for label, ((x1, y1), (x2, y2), color) in buttons.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            if label == "Erase":
                erase_mode = True  # Activate erase mode
            elif label == "Clear":
                canvas[:] = 255  # Clear everything
                points_with_colors.clear()
                erase_mode = False  # Reset erase mode
            else:
                current_color = color
                erase_mode = False  # Turn off erase mode when switching colors
            return True
    return False

# Function to detect if hand is a fist (to stop writing)
def is_fist(hand_landmarks):
    """Detect if most fingers are bent (making a fist)"""
    folded_fingers = 0
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y > hand_landmarks.landmark[pip].y:
            folded_fingers += 1

    return folded_fingers >= 3  # If 3+ fingers are bent, it's a fist

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for mirror effect
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame for hand tracking
    results = hands.process(rgb_frame)

    # Draw UI buttons
    for label, ((x1, y1), (x2, y2), color) in buttons.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)
        text_color = (0, 0, 0) if label not in ["Erase", "Clear"] else (0, 0, 0)
        cv2.putText(frame, label, (x1 + 5, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)

    # Process hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index fingertip coordinates
            cx, cy = int(hand_landmarks.landmark[8].x * width), int(hand_landmarks.landmark[8].y * height)

            # If clicking a button, change color or clear canvas
            if check_button_click(cx, cy):
                continue  # Skip drawing if a button was clicked

            # **Stop writing if fist is closed**
            if is_fist(hand_landmarks):
                continue

            # If erase mode is active, erase the drawing
            if erase_mode:
                canvas[:] = 255  # Clear the canvas completely
                points_with_colors.clear()
                erase_mode = False  # Turn off erase mode after clearing

            else:
                # Store points with selected color
                points_with_colors.append(((cx, cy), current_color))

    # Draw stored points on canvas
    for i in range(1, len(points_with_colors)):
        cv2.line(canvas, points_with_colors[i - 1][0], points_with_colors[i][0], points_with_colors[i][1], 5)

    # Show the frames
    cv2.imshow("MediaPipe Hands", frame)
    cv2.imshow("Canvas", canvas)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# In[2]:


import cv2
import mediapipe as mp
import numpy as np


# In[3]:


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.9)


# In[4]:


cap = cv2.VideoCapture(0)

# Create a blank white canvas
canvas = 255 * np.ones(shape=[720, 1280, 3], dtype=np.uint8)

# Default drawing color
current_color = (0, 0, 255)  # Red


# In[5]:


# Define button positions & colors
buttons = {
    "Red": ((50, 50), (150, 100), (0, 0, 255)),
    "Green": ((180, 50), (280, 100), (0, 255, 0)),
    "Blue": ((310, 50), (410, 100), (255, 0, 0)),
    "Yellow": ((440, 50), (540, 100), (0, 255, 255)),
    "Erase": ((570, 50), (670, 100), (200, 200, 200)),  # Gray for Eraser
    "Clear": ((700, 50), (850, 100), (255, 255, 255))  # White for Clear
}

# Store points with color history
points_with_colors = []
erase_mode = False  # Track whether erase mode is on


# In[6]:


# Function to check if a button was clicked
def check_button_click(x, y):
    global current_color, canvas, erase_mode
    for label, ((x1, y1), (x2, y2), color) in buttons.items():
        if x1 <= x <= x2 and y1 <= y <= y2:
            if label == "Erase":
                erase_mode = True  # Activate erase mode
            elif label == "Clear":
                canvas[:] = 255  # Clear everything
                points_with_colors.clear()
                erase_mode = False  # Reset erase mode
            else:
                current_color = color
                erase_mode = False  # Turn off erase mode when switching colors
            return True
    return False


# In[7]:


# Function to detect if hand is a fist (to stop writing)
def is_fist(hand_landmarks):
    """Detect if most fingers are bent (making a fist)"""
    folded_fingers = 0
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]

    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y > hand_landmarks.landmark[pip].y:
            folded_fingers += 1

    return folded_fingers >= 3  # If 3+ fingers are bent, it's a fist


# In[9]:


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip for mirror effect
    frame = cv2.flip(frame, 1)
    height, width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame for hand tracking
    results = hands.process(rgb_frame)

    # Draw UI buttons
    for label, ((x1, y1), (x2, y2), color) in buttons.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)
        text_color = (0, 0, 0) if label not in ["Erase", "Clear"] else (0, 0, 0)
        cv2.putText(frame, label, (x1 + 5, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)

    # Process hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index fingertip coordinates
            cx, cy = int(hand_landmarks.landmark[8].x * width), int(hand_landmarks.landmark[8].y * height)

            # If clicking a button, change color or clear canvas
            if check_button_click(cx, cy):
                continue  # Skip drawing if a button was clicked

            # **Stop writing if fist is closed**
            if is_fist(hand_landmarks):
                continue

            # If erase mode is active, erase the drawing
            if erase_mode:
                canvas[:] = 255  # Clear the canvas completely
                points_with_colors.clear()
                erase_mode = False  # Turn off erase mode after clearing

            else:
                # Store points with selected color
                points_with_colors.append(((cx, cy), current_color))

    # Draw stored points on canvas
    for i in range(1, len(points_with_colors)):
        cv2.line(canvas, points_with_colors[i - 1][0], points_with_colors[i][0], points_with_colors[i][1], 5)

    # Show the frames
    cv2.imshow("MediaPipe Hands", frame)
    cv2.imshow("Canvas", canvas)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:




