import joblib
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image

MODEL_FILE = 'ai_brain.joblib'

class SelfImprovingAI:
    def __init__(self):
        """Initializes or loads the AI model from a file."""
        self.model = self._load_model()
        
    def _load_model(self):
        """Attempts to load the model; otherwise, initializes a new one."""
        try:
            model = joblib.load(MODEL_FILE)
            print("AI: Loaded existing model from file.")
        except FileNotFoundError:
            print("AI: No existing model found. Starting fresh with initial training.")
            # Initialize with synthetic data for the first run
            initial_features = np.array([
                np.mean(np.array(Image.new('RGB', (150, 150), (0, 0, 255))), axis=(0, 1)), # blue for 'cat'
                np.mean(np.array(Image.new('RGB', (150, 150), (255, 0, 0))), axis=(0, 1)), # red for 'dog'
                np.mean(np.array(Image.new('RGB', (150, 150), (0, 128, 0))), axis=(0, 1))  # green for 'bird'
            ])
            initial_labels = ['cat', 'dog', 'bird']
            model = KNeighborsClassifier(n_neighbors=1)
            model.fit(initial_features, initial_labels)
            
        return model

    def _extract_features(self, image):
        """
        Extracts a simple feature from an image (average color).
        In a more advanced AI, this would be a complex feature extraction process.
        """
        return np.mean(np.array(image.convert('RGB')), axis=(0, 1)).reshape(1, -1)

    def guess_word(self, image):
        """The AI makes a prediction based on the image."""
        features = self._extract_features(image)
        return self.model.predict(features)[0]

    def improve(self, image, correct_word):
        """
        The self-improvement step: Retrain the model with new, correct data.
        """
        print("AI: Learning from mistake...")
        features = self._extract_features(image)
        
        # Check if the model already has training data
        if hasattr(self.model, 'X_train_') and hasattr(self.model, 'y_train_'):
            X_new = np.vstack([self.model.X_train_, features])
            y_new = self.model.y_train_ + [correct_word]
        else: # Handle the first-run case where the model has no internal state
            X_new = features
            y_new = [correct_word]
        
        # Retrain the model with the expanded dataset
        self.model.fit(X_new, y_new)
        
        # Store the new training data for the next session
        self.model.X_train_ = X_new
        self.model.y_train_ = y_new
        
        self._save_model()
        print("AI: Progress saved.")

    def _save_model(self):
        """Saves the current state of the model to a file."""
        joblib.dump(self.model, MODEL_FILE)
        print("AI: Brain state saved.")

