from gesture_detector.detector import GestureDetector
from config import MODEL_PATH

def main():
    detector = GestureDetector(model_path=MODEL_PATH)
    detector.run()

if __name__ == "__main__":
    main()
