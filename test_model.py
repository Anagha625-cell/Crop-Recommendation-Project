import joblib
import numpy as np

model = joblib.load("model/crop_model.pkl")

# Example input — you can change these numbers later
sample = np.array([[90, 42, 43, 25, 80, 6.5, 200]])
prediction = model.predict(sample)
print("✅ Predicted Crop:", prediction[0])
