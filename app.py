from flask import Flask, request, jsonify, render_template, send_file
import os
import cv2
from Mask import *  # Assuming your masking functions are in this module
from roboflow import Roboflow
from werkzeug.utils import secure_filename

rf = Roboflow(api_key="hhpnbI4UnbbEKjVL9QpF")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MASKED_FOLDER'] = 'masked/'

# Create the uploads and masked folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['MASKED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        file.save(file_path)
        masked_path = create_masked_image(file_path)
        if masked_path is None:
            return jsonify({'error': 'Failed to create masked image'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    masked_filename = os.path.basename(masked_path)
    return jsonify({'message': 'File uploaded and masked successfully', 'masked_image': masked_path}), 200



def create_masked_image(file_path):
    try:
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError("Could not read the image.")

        project = rf.workspace().project("pii-lahpn")
        model = project.version(2).model
        response = model.predict(file_path, confidence=40, overlap=30).json()

        target_class = 'maskedno' 
        detections = extract_detections_from_response(response)
        mask_text_on_image(image, detections, target_class)

        masked_filename = f"masked_{os.path.basename(file_path)}"
        masked_path = os.path.join(app.config['MASKED_FOLDER'], masked_filename)

        cv2.imwrite(masked_path, image)
        return masked_path
    except Exception as e:
        print(f"Error creating masked image: {e}")
        return None

@app.route('/masked/<filename>')
def serve_masked_image(filename):
    return send_file(os.path.join(app.config['MASKED_FOLDER'], filename))


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(app.config['MASKED_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
