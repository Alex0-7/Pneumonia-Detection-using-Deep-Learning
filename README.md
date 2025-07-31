# Pneumonia Detection Using Deep Learning

This project leverages deep learning techniques to automatically detect pneumonia from chest X-ray images. It utilizes a Convolutional Neural Network (CNN) to classify X-ray scans as either **Normal** or **Pneumonia**.

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Alex0-7/Pneumonia-Detection-using-Deep-Learning.git
```

### 2. Download the Dataset

Download the chest X-ray dataset from Kaggle and extract it into your project directory:

**Dataset Link**: [Chest X-Ray Pneumonia Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/data)

---

## 📦 Installation

Install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Model

### Step 1: Update File Paths in `Pneumonia.py`

Before running the training script, update the following lines in `Pneumonia.py` with your local dataset paths:

* Line 10
* Line 11
* Line 16
* Line 32
* Line 36

Then, run the script:

```bash
python Pneumonia.py
```

---

### Step 2: Test the Model Using `test.py`

To evaluate the model on validation data:

1. Open the `test.py` file.
2. Update **line 11** with the correct path to the `PNEUMONIA` folder inside the `val` directory.
3. Run the test script:

```bash
python test.py
```

---

## ✅ Output

The model will output predictions for the input X-ray images, indicating whether the image is **Normal** or shows signs of **Pneumonia**.

---

## 📌 Notes

* Ensure the dataset folder structure aligns with the script expectations.
* Training time may vary based on your hardware (e.g., CPU vs GPU).

---

## 🤝 Acknowledgments

* Dataset provided by [Paul Mooney on Kaggle](https://www.kaggle.com/paultimothymooney)
* Inspired by real-world applications in medical image analysis and diagnostics.

---

Feel free to contribute, suggest improvements, or report issues!
