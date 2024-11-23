from flask import Flask, render_template, request, redirect
import os
from PIL import Image
import pickle

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'  # Folder to store uploaded images
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the pickled model
model_path = "model (1).pkl"  # Adjust the path if necessary
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print(f"Error: Model file '{model_path}' not found. Please ensure the file exists.")
    model = None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded file
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Process the image to generate a caption
        image = Image.open(image_path)
        caption = generate_image_caption(image)

        # Render the result
        return render_template('index.html', caption=caption)

def generate_image_caption(image):
    """
    Generate a caption for the provided image using the loaded model.
    Replace this with your actual model prediction code.
    """
    if not model:
        return "Error: Model is not loaded."

    # Example pseudo-code for model prediction:
    # Convert the image to the format required by your model (e.g., resizing, normalization)
    # prediction = model.predict(preprocessed_image)
    # return decode_prediction_to_caption(prediction)
    caption = "This is a generated caption from the loaded model."  # Replace with real logic
    return caption


if __name__ == '__main__':
    app.run(debug=True)
