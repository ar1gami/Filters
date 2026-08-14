import cv2
import mediapipe as mp
<<<<<<< HEAD
import numpy as np
from filters import FILTROS
from geometry import closing_detector, render_portal, portal_width
from hand_tracking import is_finger_extended
=======
import time

from hand_tracking import INDEX_TIP, THUMB_TIP
from geometry import render_portal, portal_width, ClosingGestureDetector
from filters import FILTROS, FILTER_NAMES
>>>>>>> 7c0c3c68b8230706d54c8a462b2a328a693a1eb6

mp_hands = mp.solutions.hands
INDEX_TIP = mp_hands.HandLandmark.INDEX_FINGER_TIP
THUMB_TIP = mp_hands.HandLandmark.THUMB_TIP

def main():
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        filtro_index = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

<<<<<<< HEAD
            left_hand = None
            right_hand = None
            if results.multi_hand_landmarks and results.multi_handedness:
                for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    label = handedness.classification[0].label
                    # MediaPipe returns "Left" and "Right" – we keep as is
                    if label == "Left":
                        left_hand = hand_landmarks
                    else:
                        right_hand = hand_landmarks
=======
    filtro_index = 0
    closing_detector = ClosingGestureDetector()
    prev_time = time.time()
>>>>>>> 7c0c3c68b8230706d54c8a462b2a328a693a1eb6

            if left_hand is not None and right_hand is not None:
                lm_left = left_hand.landmark
                lm_right = right_hand.landmark

<<<<<<< HEAD
                # Get index tips
                p1 = (int(lm_left[INDEX_TIP].x * w), int(lm_left[INDEX_TIP].y * h))
                p2 = (int(lm_right[INDEX_TIP].x * w), int(lm_right[INDEX_TIP].y * h))
                # Get thumb tips (for the other two corners)
                p3 = (int(lm_left[THUMB_TIP].x * w), int(lm_left[THUMB_TIP].y * h))
                p4 = (int(lm_right[THUMB_TIP].x * w), int(lm_right[THUMB_TIP].y * h))
=======
        # FPS calculation (optional but handy)
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if (curr_time - prev_time) > 0 else 0
        prev_time = curr_time

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
>>>>>>> 7c0c3c68b8230706d54c8a462b2a328a693a1eb6

                # Calculate some width/height for gesture detection (adjust as needed)
                width = int(np.linalg.norm(np.array(p1) - np.array(p2)))
                if closing_detector.update(width, w):   # assuming this function exists
                    filtro_index = (filtro_index + 1) % len(FILTROS)

                frame = render_portal(frame, p1, p2, p3, p4, FILTROS[filtro_index])

<<<<<<< HEAD
            cv2.imshow("Filters", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
=======
                if label == "Left":
                    left_hand = hand_landmarks
                else:
                    right_hand = hand_landmarks

        if left_hand is not None and right_hand is not None:
            lm_left = left_hand.landmark
            lm_right = right_hand.landmark

            p1 = (lm_left[INDEX_TIP].x * w, lm_left[INDEX_TIP].y * h)
            p2 = (lm_left[THUMB_TIP].x * w, lm_left[THUMB_TIP].y * h)
            p3 = (lm_right[INDEX_TIP].x * w, lm_right[INDEX_TIP].y * h)
            p4 = (lm_right[THUMB_TIP].x * w, lm_right[THUMB_TIP].y * h)

            width = portal_width(p1, p2, p3, p4)

            if closing_detector.update(width, w):
                filtro_index = (filtro_index + 1) % len(FILTROS)

            frame = render_portal(frame, p1, p2, p3, p4, FILTROS[filtro_index])

            # Display current filter name and FPS on screen
            cv2.putText(frame, f"Filter: {FILTER_NAMES[filtro_index]}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Filters", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
>>>>>>> 7c0c3c68b8230706d54c8a462b2a328a693a1eb6

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
