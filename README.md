# PII Detector

This project is a Flask-based web application that detects and masks Personally Identifiable Information (PII) in images. It utilizes a custom-trained object detection model via the Roboflow API to find specific PII fields (like Aadhaar numbers, masked numbers, etc.) and redacts them by drawing a black rectangle over the detected areas.

## Features

- **Upload Image**: Upload an image containing PII data.
- **Automated Masking**: Automatically detects PII such as Aadhaar numbers and masks them.
- **Download**: Download the masked image safely.

## Prerequisites

Make sure you have Python installed on your system.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Praveenraja195/pii_detector.git
   cd pii_detector
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Upload an image through the web interface to see the PII masking in action.

## Project Structure

- `app.py`: The main Flask application file handling routes and logic.
- `Mask.py`: Contains helper functions for processing Roboflow API responses and drawing masks on images using OpenCV.
- `templates/`: Contains the HTML template (`index.html`) for the web interface.
- `static/`: Contains static assets like the loading GIF.
- `requirements.txt`: List of Python dependencies required to run the project.

## Note

Ensure your Roboflow API key in `app.py` is kept secure and valid.

## License

MIT License
