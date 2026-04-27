import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
# Load model
with open("model.joblib", "rb") as f:
    print(f.read(200))

# Data
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([200000, 300000, 400000, 500000, 600000])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.joblib")

# Load model
loaded_model = joblib.load("model.joblib")

# Predict
#(example: 1800 sqft)
result = loaded_model.predict([[1800]])

print("Predicted Price:", result[0])
print("model pridicted is suceesfully")

