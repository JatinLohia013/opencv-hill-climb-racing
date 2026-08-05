# 🚗 Hill Climb Racing Using Hand Gestures

Control **Hill Climb Racing** using only your **hand gestures**! This project leverages **Computer Vision** with **OpenCV** and **MediaPipe** to detect hand gestures in real time and translate them into keyboard controls for the game.

---

## 📌 Overview

This project demonstrates how hand tracking and gesture recognition can be integrated with game automation. Using a webcam, the application detects your hand, recognizes predefined gestures, and controls the vehicle in **Hill Climb Racing** without requiring a keyboard.

---

## 🎥 Demo

<video controls src="Screen Recording 2026-08-04 224517.mp4" title="Title"></video>

---

## ✨ Features

- 🖐️ Real-time hand detection using MediaPipe
- 🎯 Accurate hand landmark tracking
- ✊ Fist gesture for braking
- ✋ Open palm gesture for acceleration
- 🎮 Keyboard automation using PyAutoGUI
- 📷 Live webcam feed with gesture visualization
- ⚡ Smooth and responsive gameplay

---

## 🛠️ Technologies Used

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

---

## 🎮 Controls

| Gesture | Action |
|----------|--------|
| ✋ Open Palm | Accelerate |
| ✊ Fist | Brake |
| ❓ Unknown Gesture | Release Both Keys |

---

## 🧠 How It Works

1. Captures live video from the webcam.
2. Detects a single hand using MediaPipe Hands.
3. Identifies all 21 hand landmarks.
4. Determines whether each finger is open or closed.
5. Recognizes predefined gestures:
   - Open Palm
   - Fist
6. Converts gestures into keyboard inputs:
   - Right Arrow → Accelerate
   - Left Arrow → Brake
7. Displays the detected gesture and hand label in real time.

---

## 🔮 Future Improvements

- Support for more hand gestures
- Gesture customization
- Multi-hand controls
- FPS optimization
- Gesture smoothing to reduce flickering
- Support for additional games
- GUI for gesture configuration

---

## 📋 Requirements

- Python 3.9+
- Webcam
- Hill Climb Racing running on PC
- Windows (tested)

---

## 👨‍💻 Author

**Jatin Lohia**

B.Tech (AI & Data Science)

Passionate about Computer Vision, Artificial Intelligence, and Automation.

---

## ⭐ If you like this project

Give this repository a ⭐ and feel free to fork it!

---

## 📄 License

This project is licensed under the MIT License.