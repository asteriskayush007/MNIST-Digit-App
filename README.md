# 🧠 MNIST Handwritten Digit Recognition Web App

### ✍️ Draw a digit from 0–9 and let the AI predict what you wrote — in real-time, in your browser!

---

## 🚀 Features

* Hand-drawn digit input canvas
* Real-time prediction using trained CNN model
* Clean Streamlit interface
* Live preview of preprocessed input image

---

## 🛠️ Technologies Used

| Tool             | Purpose                            |
| ---------------- | ---------------------------------- |
| TensorFlow/Keras | Deep learning (CNN model training) |
| OpenCV           | Image preprocessing                |
| Streamlit        | Web app interface                  |
| NumPy            | Numerical operations               |

---

## 📁 Project Structure

```
MNIST-Digit-App/
│
├── app.py                # Streamlit app
├── train_model.py        # CNN model training script
├── mnist_model.keras     # Saved trained model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ✅ How to Run the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/MNIST-Digit-App.git
cd MNIST-Digit-App
```

### 2. Create & activate a virtual environment (optional but recommended)

```bash
python -m venv mnist-env
source mnist-env/bin/activate  # On Windows: mnist-env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model (if `mnist_model.keras` doesn't exist)

```bash
python train_model.py
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🧪 Example Workflow

1. Launch the app.
2. Draw a digit (0–9) using your mouse.
3. Click **“Predict Digit”**.
4. See the processed digit and prediction below!

---

## 📦 `requirements.txt`

```
streamlit
streamlit-drawable-canvas
opencv-python
numpy
tensorflow
```

---

## ⚠️ Common Issues

* **"pop from empty list" error**
  → Your model file may be corrupt. Delete `mnist_model.keras` and retrain it with `train_model.py`.

* **Always predicts 0**
  → Make sure you're preprocessing the image correctly: resize to 28x28, grayscale, normalize, reshape.

---

## 🙌 Credits

* MNIST dataset: [Yann LeCun et al.](http://yann.lecun.com/exdb/mnist/)
* Streamlit Canvas: [streamlit-drawable-canvas](https://github.com/andfanilo/streamlit-drawable-canvas)

---

## 📄 License

This project is licensed under the MIT License.
