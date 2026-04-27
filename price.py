#imports
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# 3 features: demand, supply, competition
X = np.array([
    [1000, 500, 180],
    [1500, 700, 200],
    [2000, 900, 220],
    [2500, 1100, 250],
    [3000, 1300, 270]
])

y = np.array([200000, 300000, 400000, 500000, 600000])

#train model
model = LinearRegression()
model.fit(X, y)

#save model
joblib.dump(model, "model.joblib")

input_data= np.array([[1800,600,190]])
# Predict
result = model.predict(input_data)
print("Predicted Price :",result)
#print
print("Model trained and saved successfully!")