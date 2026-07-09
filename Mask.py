import cv2

# Read the image
#image = cv2.imread('test1.jpg')

def extract_detections_from_response(response): 
    detections = []
    for result in response['predictions']:
        # Extract necessary data from response
        detections.append({
            'class': result.get('class'),
            'x': result.get('x'),
            'y': result.get('y'),
            'width': result.get('width'),
            'height': result.get('height')
        })
    return detections

def mask_text_on_image(image, detections, target_class):
    for detection in detections:
        # Check if the class of the detection matches the target class
        if detection['class'] == target_class:
            x_center = detection['x']
            y_center = detection['y']
            width = detection['width']
            height = detection['height']
            
            # Convert center coordinates and dimensions to top-left and bottom-right
            x_min = int(x_center - width / 2)
            y_min = int(y_center - height / 2)
            x_max = int(x_center + width / 2)
            y_max = int(y_center + height / 2)
            
            # Draw a filled black rectangle over the detected text area
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 0, 0), -1)

# Extract detections
response = {
    "predictions": [
        {
            "x": 271.5,
            "y": 512.5,
            "width": 139,
            "height": 57,
            "confidence": 0.753,
            "class": "maskedno",
            "class_id": 1,
            "detection_id": "8440026c-fc9e-48a0-a91a-d8076fae6526"
        },
        {
            "x": 312.5,
            "y": 511,
            "width": 229,
            "height": 62,
            "confidence": 0.683,
            "class": "aadharno",
            "class_id": 0,
            "detection_id": "5ec10a7e-dc77-4c02-a6f9-2182ab296921"
        }
    ]
}

# Process the image
#target_class = 'maskedno' 
#detections = extract_detections_from_response(response)
#mask_text_on_image(image, detections, target_class)

# Save the modified image
#cv2.imwrite('masked_image.jpg', image)
