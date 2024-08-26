import numpy as np
from collections import deque

class GestureSmoother:
    def __init__(self, sequence_length, swipe_threshold, consistent_frames):
        self.sequence_length = sequence_length
        self.swipe_threshold = swipe_threshold
        self.consistent_frames = consistent_frames
        self.ema_alpha = 0.7
        self.gesture_classes = ["swipe_left", "swipe_right", "no_gesture"]
        self.movement_history = deque(maxlen=self.sequence_length)
        self.ema_gesture = None

    def update_landmarks(self, landmarks):
        """Update movement history with the new landmarks."""
        self.movement_history.append(landmarks)

    def preprocess_sequence(self, sequence):
        """Preprocess the sequence for the model."""
        sequence = np.array(sequence)
        sequence = np.expand_dims(sequence, axis=0)  # Add batch dimension
        return sequence

    def apply_ema(self, current_gesture):
        """Apply exponential moving average for gesture smoothing."""
        current_gesture_index = self.gesture_classes.index(current_gesture)
        if self.ema_gesture is None:
            self.ema_gesture = current_gesture_index
        else:
            self.ema_gesture = self.ema_alpha * current_gesture_index + (1 - self.ema_alpha) * self.ema_gesture
        return self.gesture_classes[int(round(self.ema_gesture))]
