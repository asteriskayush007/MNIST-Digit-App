import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("mnist_model.keras", compile=False)

# Streamlit page setup
st.set_page_config(page_title="MNIST Digit Recognizer", layout="centered")
st.markdown("## ✍️ Draw a Digit (0-9) and Let AI Predict")

# Drawing canvas
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=12,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

# Predict button
if st.button("Predict Digit"):
    if canvas_result.image_data is not None:
        img = canvas_result.image_data

        # Convert RGBA to grayscale
        img = cv2.cvtColor(img.astype('uint8'), cv2.COLOR_RGBA2GRAY)

        # Invert image: white digit on black to black digit on white
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

        # Resize directly to 28x28
        img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)

        # Normalize & reshape
        img = img / 255.0
        img = img.reshape(1, 28, 28, 1)

        # Show processed image for debugging
        st.image(img.reshape(28, 28), width=150, caption="Processed Input")

        # Predict using model
        prediction = model.predict(img)
        predicted_digit = np.argmax(prediction)

        st.success(f"🧠 Predicted Digit: {predicted_digit}")
    else:
        st.warning("⚠️ Please draw a digit first.")
