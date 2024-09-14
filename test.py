from keras_preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os

# Load the model
model = load_model('pneumonia_model.keras')

# Directory containing the images
image_data_dir = r'C:\Project\Pneumonia-Detection-using-Deep-Learning\val\PNEUMONIA'

# Iterate through all JPEG images in the directory
for filename in os.listdir(image_data_dir):
    if filename.endswith('.jpeg'):
        image_path = os.path.join(image_data_dir, filename)

        # Load and preprocess the image
        img = image.load_img(image_path, target_size=(224, 224))
        imagee = image.img_to_array(img)
        imagee = np.expand_dims(imagee, axis=0)
        img_data = preprocess_input(imagee)

        # Make prediction
        prediction = model.predict(img_data)

        # Print the prediction
        if prediction[0][0] > prediction[0][1]:
            print(f"Person is safe. Image: {filename}")
        else:
            print(f"Person is affected with Pneumonia. Image: {filename}")

        print(f"Predictions: {prediction}")