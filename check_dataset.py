import pandas as pd

df = pd.read_csv("data/Crop_recommendation.csv")

print("✅ Dataset loaded successfully")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns)
