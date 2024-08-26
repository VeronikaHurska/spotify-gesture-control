from tensorflow.keras.models import load_model

class ModelLoader:
    def __init__(self, model_path):
        self.model = load_model(model_path)
