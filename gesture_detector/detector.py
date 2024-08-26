import cv2
from gesture_detector.model_loader import ModelLoader
from gesture_detector.hand_tracker import HandTracker
from gesture_detector.gesture_smoother import GestureSmoother
from gesture_detector.spotify_controller import SpotifyController
from config import SEQUENCE_LENGTH, SWIPE_THRESHOLD, CONSISTENT_FRAMES, FRAME_WIDTH, FRAME_HEIGHT, FPS
import numpy as np

class GestureDetector:
    def __init__(self, model_path):
        self.model_loader = ModelLoader(model_path)
        self.hand_tracker = HandTracker()
        self.gesture_smoother = GestureSmoother(SEQUENCE_LENGTH, SWIPE_THRESHOLD, CONSISTENT_FRAMES)
        self.spotify_controller = SpotifyController()
        self.movement_history = []
        self.last_detected_gesture = "no_gesture"
        self.hand_missing_frames = 0
        self.max_missing_frames = 3

    def detect_gesture(self, frame):
        landmarks = self.hand_tracker.get_hand_landmarks(frame)
        
        if landmarks:
            self.hand_missing_frames = 0
            self.gesture_smoother.update_landmarks(landmarks)  # Make sure update_landmarks is called

            if len(self.gesture_smoother.movement_history) == SEQUENCE_LENGTH:
                initial_x = self.gesture_smoother.movement_history[0][0]  # Initial X coordinate
                final_x = self.gesture_smoother.movement_history[-1][0]  # Final X coordinate

                if abs(final_x - initial_x) > SWIPE_THRESHOLD:
                    sequence = self.gesture_smoother.preprocess_sequence(self.gesture_smoother.movement_history)
                    prediction = self.model_loader.model.predict(sequence)
                    predicted_class = self.gesture_smoother.gesture_classes[np.argmax(prediction)]

                    # Apply EMA for gesture smoothing
                    smoothed_gesture = self.gesture_smoother.apply_ema(predicted_class)
                    self.last_detected_gesture = smoothed_gesture

                    # Control Spotify based on detected gesture
                    if self.last_detected_gesture != "no_gesture":
                        self.spotify_controller.control_spotify(self.last_detected_gesture)

                    # Clear movement history after inference
                    self.gesture_smoother.movement_history.clear()
        else:
            self.hand_missing_frames += 1
            if self.hand_missing_frames > self.max_missing_frames:
                self.gesture_smoother.movement_history.clear()
                self.last_detected_gesture = "no_gesture"

        return frame

    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        cap.set(cv2.CAP_PROP_FPS, FPS)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)  # Flip horizontally
            frame = self.detect_gesture(frame)

            # Display stats and detected gesture
            cv2.putText(frame, f'Gesture: {self.last_detected_gesture}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow('Hand Gesture Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
