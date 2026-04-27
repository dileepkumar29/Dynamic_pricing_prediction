# import streamlit as st
# import joblib
# import numpy as np

# # Load model
# model = joblib.load("model.joblib")

# st.title("Dynamic Pricing Prediction App")

# # Inputs
# demand = st.number_input("Demand", min_value=0.0)
# supply = st.number_input("Supply", min_value=0.0)
# competition = st.number_input("Competition Price", min_value=0.0)

# if st.button("Predict Price"):

#     # Input must match training features (3 features)
#     input_data = np.array([[demand, supply, competition]])

#     # Prediction
#     prediction = model.predict(input_data[0])

#     #  OUTPUT DISPLAY (VISIBLE IN UI)
#     st.success(f"Predicted Price: {prediction}")

#     st.metric("Dynamic Price", f"{prediction:.2f}")

#     st.write("Raw Output:", prediction)


import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.joblib")

st.title("Dynamic Pricing Prediction App")

# Inputs
demand = st.number_input("Demand", min_value=0.0)
supply = st.number_input("Supply", min_value=0.0)
competition = st.number_input("Competition Price", min_value=0.0)

if st.button("Predict Price"):

    # Create 2D input (IMPORTANT)
    input_data = np.array([[demand, supply, competition]])

    # Prediction (FIXED)
    prediction = model.predict(input_data)

     # Extract single value
    price = prediction[0]

    # Display output
    st.success(f"Predicted Price: ₹{price}")

    st.metric("Dynamic Price", f"₹{price:,.2f}")

    st.write("Raw Output:", prediction)