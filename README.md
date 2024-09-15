# **Pneumonia-Detection-using-Deep-Learning**

This project uses deep learning to detect pneumonia from chest X-ray images.

## Getting Started

### Clone the Repository
Clone this repository to your local machine and download the dataset from Kaggle.

- Dataset Link: [Chest X-Ray Pneumonia Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/data)

```bash
git clone https://github.com/Alex0-7/Pneumonia-Detection-using-Deep-Learning.git
```
## Step 1: Install Required Libraries
Install all the necessary libraries by using the requirement.txt file.
```bash
pip install -r requirment.txt
```
## Step 2: Update File Paths and Run Pneumonia.py
1. Open the Pneumonia.py file.
2. Update the following lines with the correct paths to your train and test data files:
Line 10
Line 11
Line 16
Line 32
Line 36
3. Run the script (this may take some time depending on your system).
```bash
python Pneumonia.py
```
## Step 3: Update File Path and Run test.py
1. Open the test.py file.
2. Update the path in line 11 to point to your PNEUMONIA folder inside the val directory.
3. Run the script.
```bash
python test.py
```
## That’s it! 🎉
You’re now ready to run pneumonia detection on chest X-ray images.
