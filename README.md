
# Face Detection with Haar Cascade Classifiers

Face Detection with Haar Cascade ClassifiersFace Detection with Haar Cascade Classifiers

## Lain - Lain

#### Features

- Face Detection: Uses Haar Cascade Classifiers to detect faces in images.
- Real-Time Feedback: Provides immediate feedback on the detection results.
- Image Annotation: Annotates detected faces in the image and returns the processed image.

#### Technologies Used

- Backend: Python (Flask)
- Libraries: OpenCV, NumPy, Base64




## Project Structure

```javascript
.
├── app.py
├── haarcascade_frontalface_default.xml
├── requirements.txt
└── README.md

```


## Setup and Installation

Prerequisites
- Python 3.6+
- Flask
- OpenCV
- NumPy
Instructions : 
1. Clone the Repository
```bash
  git clone https://github.com/yourusername/face-detection-haarcascade.git
cd face-detection-haarcascade
```
2. Clone the Repository
```bash
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
```
3. Download Haar Cascade XML File
- Ensure the haarcascade_frontalface_default.xml file is in the project directory.
4. Start the Flask Server
```bash
- python app.py
```


## Python Dependencies

Create a requirements.txt file with the following content:
`
- Flask
- opencv-python-headless
- numpy`



## API Reference

#### POST /detect_face

```http
  POST /detect_face
```

| Content-Type | Body     
| :-------- | :------- | 
| `application/json` | `string` | 

`
{
    "nis": "12345",
    "nama": "John Doe",
    "imageBase64": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/..."
}
`


