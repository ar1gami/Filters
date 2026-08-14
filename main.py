import cv2
import mediapipe as mp
import numpy as np
from filters import FILTROS
from geometry import closing_detector, render_portal, portal_width
from hand_tracking import is_finger_extended

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

            if left_hand is not None and right_hand is not None:
                lm_left = left_hand.landmark
                lm_right = right_hand.landmark

                # Get index tips
                p1 = (int(lm_left[INDEX_TIP].x * w), int(lm_left[INDEX_TIP].y * h))
                p2 = (int(lm_right[INDEX_TIP].x * w), int(lm_right[INDEX_TIP].y * h))
                # Get thumb tips (for the other two corners)
                p3 = (int(lm_left[THUMB_TIP].x * w), int(lm_left[THUMB_TIP].y * h))
                p4 = (int(lm_right[THUMB_TIP].x * w), int(lm_right[THUMB_TIP].y * h))

                # Calculate some width/height for gesture detection (adjust as needed)
                width = int(np.linalg.norm(np.array(p1) - np.array(p2)))
                if closing_detector.update(width, w):   # assuming this function exists
                    filtro_index = (filtro_index + 1) % len(FILTROS)

                frame = render_portal(frame, p1, p2, p3, p4, FILTROS[filtro_index])

            cv2.imshow("Filters", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
