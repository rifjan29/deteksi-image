from flask import Flask, request, jsonify
import cv2
import numpy as np
import base64

app = Flask(__name__)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

@app.route('/detect_face', methods=['POST'])
def detect_face():
    data = request.get_json()
    nis = data['nis']
    nama = data['nama']
    image_data = data['imageBase64']
    image_data = image_data.split(',')[1]
    image = np.frombuffer(base64.b64decode(image_data), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 1:
        x, y, w, h = faces[0]
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        response = {
            'success': True,
            'nama':  nama, # Replace with actual name detection logic
            'nis':  nis, # Replace with actual name detection logic
        }
    else:
        response = {
            'success': False
        }

    _, buffer = cv2.imencode('.jpg', image)
    response['image'] = base64.b64encode(buffer).decode('utf-8')
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)