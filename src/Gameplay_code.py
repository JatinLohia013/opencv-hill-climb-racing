import cv2
import mediapipe as mp
import time
import pyautogui

mp_hands=mp.solutions.hands
mp_draw=mp.solutions.drawing_utils

hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.5,min_tracking_confidence=0.5)

cap=cv2.VideoCapture(0)

left_pressed=False
right_pressed=False

while True:
    success,frame=cap.read()

    if not success:
        break
    frame=cv2.flip(frame,1)

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    results=hands.process(rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks,handedness in zip(results.multi_hand_landmarks,results.multi_handedness):

            mp_draw.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)

            landmarks=hand_landmarks.landmark
            label=handedness.classification[0].label

            #Thumb Detection
            if label=="Right":
                thumb_open=landmarks[4].x < landmarks[3].x
            else:
                thumb_open=landmarks[4].x > landmarks[3].x

            #Other Fingers
            index_open=landmarks[8].y < landmarks[6].y
            middle_open=landmarks[12].y < landmarks[10].y
            ring_open=landmarks[16].y < landmarks[14].y
            pinky_open=landmarks[20].y < landmarks[18].y

            #Finger List

            fingers=[thumb_open,index_open,middle_open,ring_open,pinky_open]

            finger_count=fingers.count(True)

            #Gesture Detection
            gesture="Unknown"

            if fingers==[False,False,False,False,False]:
                gesture="Fist"

            elif fingers==[True,True,True,True,True]:
                gesture="Open Palm"

            else:
                gesture="Unknown"
            
            # Game Controls   
            if gesture == "Open Palm":
                # Release Brake
                if left_pressed:
                    pyautogui.keyUp("left")
                    left_pressed = False
                # Hold Accelerator
                if not right_pressed:
                    pyautogui.keyDown("right")
                    right_pressed = True

            elif gesture == "Fist":
                # Release Accelerator
                if right_pressed:
                    pyautogui.keyUp("right")
                    right_pressed = False

                # Hold Brake
                if not left_pressed:
                    pyautogui.keyDown("left")
                    left_pressed = True

            else:

                # Release Both Keys
                if right_pressed:
                    pyautogui.keyUp("right")
                    right_pressed = False

                if left_pressed:
                    pyautogui.keyUp("left")
                    left_pressed = False


            cv2.putText(frame,f"Gesture: {gesture}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

            #Display Left/Right Hand

            cv2.putText(frame,f"Hand:{label}",(20,120),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("Hill Climb Racing",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



            
