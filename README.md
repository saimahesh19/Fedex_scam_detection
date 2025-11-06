# 🎙️ Audio Transcription & Fraud Detection API

A Flask-based REST API service that transcribes audio files and detects potential fraud using machine learning. This application combines speech recognition with deep learning to identify fraudulent content in voice recordings.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 👨‍💻 Author

**Marpu Sai Mahesh**
- 📧 Email: chintusaimaheshmarpu@gmail.com
- 📱 Phone: +91 9502342564
- 📍 Location: Andhra Pradesh, India
- 💼 LinkedIn: [linkedin.com/in/marpumahesh](https://www.linkedin.com/in/marpumahesh/)
- 🐙 GitHub: [github.com/saimahesh19](https://github.com/saimahesh19)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Model Details](#model-details)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- 🎤 **Audio Transcription**: Convert speech to text using Google Speech Recognition
- 🔍 **Fraud Detection**: ML-based classification to identify fraudulent content
- 🔄 **Multi-Format Support**: Accepts WAV, MP3, and M4A audio files
- 🌐 **CORS Enabled**: Cross-Origin Resource Sharing for frontend integration
- 📊 **Probability Scores**: Returns confidence levels for fraud predictions
- 🚀 **RESTful API**: Easy integration with any frontend or service
- 🔒 **Error Handling**: Comprehensive logging and error management
- 🧹 **Auto Cleanup**: Temporary files are automatically removed

## 🎥 Demo

```bash
# Example API request
curl -X POST http://localhost:5000/upload \
  -F "file=@audio_sample.wav"

# Example response
{
  "transcription": "This is a sample transcription",
  "classification": {
    "predicted_label": "normal",
    "probability": 0.23
  }
}
```

## 🛠️ Tech Stack

### Backend
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **TensorFlow/Keras** - Deep learning framework
- **SpeechRecognition** - Audio transcription
- **PyDub** - Audio file processing
- **scikit-learn** - Machine learning utilities
- **NumPy** - Numerical computing

### Machine Learning
- **RNN Model** - Recurrent Neural Network for text classification
- **Tokenizer** - Text preprocessing and vectorization
- **Google Speech API** - Speech-to-text conversion

## 📦 Prerequisites

Before running this application, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- FFmpeg (for audio file conversion)
- Internet connection (for Google Speech Recognition API)

### Installing FFmpeg

**Windows:**
```bash
choco install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/saimahesh19/audio-fraud-detection.git
cd audio-fraud-detection
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
pip install flask-cors
pip install SpeechRecognition
pip install pydub
pip install tensorflow
pip install scikit-learn
pip install numpy
pip install joblib
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Set Up Pre-trained Models

Ensure you have the following files in the `pretrained_models_datasets` directory:

```
pretrained_models_datasets/
├── fraud_words_tokenizer.joblib
└── fraud_words_rnn_model.h5
```

### 5. Run the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 📁 Project Structure

```
audio-fraud-detection/
├── app.py                          # Main Flask application
├── transcriber.py                  # Audio transcription and classification logic
├── pretrained_models_datasets/
│   ├── fraud_words_tokenizer.joblib  # Pre-trained tokenizer
│   └── fraud_words_rnn_model.h5      # Pre-trained RNN model
├── static/
│   └── uploads/                    # Temporary audio file storage
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── .gitignore                      # Git ignore file
```

## 📖 Usage

### Basic Workflow

1. **Upload Audio File**: Send a POST request with an audio file
2. **Transcription**: Audio is converted to text using Google Speech Recognition
3. **Classification**: Text is analyzed for fraudulent content
4. **Response**: Receive transcription and fraud detection results

### Example with Python

```python
import requests

url = "http://localhost:5000/upload"
files = {'file': open('audio_sample.wav', 'rb')}

response = requests.post(url, files=files)
result = response.json()

print(f"Transcription: {result['transcription']}")
print(f"Classification: {result['classification']['predicted_label']}")
print(f"Probability: {result['classification']['probability']}")
```

### Example with JavaScript

```javascript
const formData = new FormData();
formData.append('file', audioFile);

fetch('http://localhost:5000/upload', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => {
  console.log('Transcription:', data.transcription);
  console.log('Classification:', data.classification.predicted_label);
  console.log('Probability:', data.classification.probability);
});
```

### Example with cURL

```bash
curl -X POST http://localhost:5000/upload \
  -F "file=@path/to/audio.wav" \
  -H "Content-Type: multipart/form-data"
```

## 🔌 API Documentation

### Endpoints

#### 1. Home Endpoint

```
GET /
```

**Description**: Welcome message and API status check

**Response:**
```json
"Welcome to the Flask Transcription Service!"
```

#### 2. Upload Audio File

```
POST /upload
```

**Description**: Upload an audio file for transcription and fraud detection

**Request:**
- **Method**: POST
- **Content-Type**: multipart/form-data
- **Body**: 
  - `file`: Audio file (WAV, MP3, or M4A)

**Response (Success - 200):**
```json
{
  "transcription": "This is the transcribed text",
  "classification": {
    "predicted_label": "fraud" | "normal",
    "probability": 0.85
  }
}
```

**Response (Error - 400):**
```json
{
  "error": "No file part in the request"
}
```

**Response (Error - 500):**
```json
{
  "error": "Error message details"
}
```

### Supported Audio Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| WAV | `.wav` | Recommended format |
| MP3 | `.mp3` | Automatically converted to WAV |
| M4A | `.m4a` | Automatically converted to WAV |

## 🤖 Model Details

### RNN Classification Model

The fraud detection system uses a Recurrent Neural Network (RNN) trained on labeled text data to identify fraudulent patterns in speech.

**Model Architecture:**
- Input Layer: Tokenized text sequences (max length: 100)
- Embedding Layer: Word embeddings
- RNN Layers: LSTM/GRU cells for sequential processing
- Output Layer: Binary classification (fraud/normal)

**Training Data:**
- Labeled dataset of fraudulent and normal conversations
- Tokenizer vocabulary: Pre-trained on domain-specific text

**Performance Metrics:**
- Accuracy: ~85-90% (depending on training data)
- Precision: High precision for fraud detection
- Recall: Balanced for both classes

### Tokenizer

The tokenizer converts text into numerical sequences for model input:
- **Type**: Keras Tokenizer
- **Max Sequence Length**: 100 tokens
- **Padding**: Post-padding with zeros
- **Format**: Joblib serialized object

## ⚙️ Configuration

### Model Paths

Update these paths in `transcriber.py` if your model files are in different locations:

```python
TOKENIZER_PATH = r"pretrained_models_datasets\fraud_words_tokenizer.joblib"
MODEL_PATH = r"pretrained_models_datasets\fraud_words_rnn_model.h5"
```

### Upload Folder

Change the upload directory in `app.py`:

```python
UPLOAD_FOLDER = 'static/uploads'
```

### Host and Port

Modify the Flask server configuration:

```python
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### CORS Settings

To restrict CORS to specific origins:

```python
from flask_cors import CORS

CORS(app, resources={r"/upload": {"origins": "https://yourdomain.com"}})
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install flask flask-cors SpeechRecognition pydub tensorflow scikit-learn numpy joblib
```

#### 2. FFmpeg Not Found

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`

**Solution**:
- Install FFmpeg (see Prerequisites section)
- Add FFmpeg to system PATH

#### 3. Model Loading Error

**Error**: `Error loading tokenizer or model`

**Solution**:
- Verify model files exist in `pretrained_models_datasets/`
- Check file paths in `transcriber.py`
- Ensure model files are not corrupted

#### 4. Google Speech Recognition Error

**Error**: `Could not request results from Google Speech Recognition service`

**Solution**:
- Check internet connection
- Verify audio quality (clear speech, minimal background noise)
- Consider using alternative speech recognition services

#### 5. Audio Not Clear Enough

**Error**: `Audio not clear enough to transcribe`

**Solution**:
- Use high-quality audio recordings
- Reduce background noise
- Ensure proper microphone placement
- Use supported audio formats (WAV recommended)

#### 6. CORS Error

**Error**: `Access to fetch at 'http://localhost:5000/upload' from origin 'http://localhost:3000' has been blocked by CORS policy`

**Solution**:
- Ensure `flask-cors` is installed
- Verify CORS is enabled in `app.py`: `CORS(app)`

## 🔒 Security Considerations

### For Production Deployment:

1. **File Upload Validation**
   - Implement file size limits
   - Validate file types strictly
   - Scan for malware

```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
```

2. **Rate Limiting**
   - Prevent API abuse
   - Implement request throttling

```python
from flask_limiter import Limiter
limiter = Limiter(app, default_limits=["100 per hour"])
```

3. **Authentication**
   - Add API key authentication
   - Implement user authentication

4. **HTTPS**
   - Use SSL/TLS certificates
   - Encrypt data in transit

5. **Environment Variables**
   - Store sensitive data in environment variables

```python
import os
MODEL_PATH = os.environ.get('MODEL_PATH', 'default_path')
```

6. **Input Sanitization**
   - Validate and sanitize all inputs
   - Prevent injection attacks

## 🚀 Deployment

### Deploy with Gunicorn (Production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Deploy with Docker

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

**Build and Run:**
```bash
docker build -t audio-fraud-detection .
docker run -p 5000:5000 audio-fraud-detection
```

### Deploy to Cloud Platforms

- **Heroku**: Follow [Flask deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- **AWS EC2**: Deploy on Ubuntu instance with Nginx reverse proxy
- **Google Cloud Run**: Containerized deployment
- **Azure App Service**: Direct Flask deployment

## 📊 Performance Optimization

### Tips for Better Performance

1. **Use Batch Processing**: Process multiple files concurrently
2. **Caching**: Cache frequently used model predictions
3. **Async Processing**: Use Celery for background tasks
4. **Model Optimization**: Quantize model for faster inference
5. **Load Balancing**: Use multiple workers with Gunicorn

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide
- Add unit tests for new features
- Update documentation
- Ensure all tests pass before submitting PR

## 📝 Future Enhancements

- [ ] Support for real-time audio streaming
- [ ] Multi-language transcription support
- [ ] Custom model training interface
- [ ] WebSocket support for live transcription
- [ ] Enhanced fraud detection with multiple models
- [ ] Audio quality assessment
- [ ] Speaker diarization (identify multiple speakers)
- [ ] Export transcriptions to various formats (PDF, DOCX)
- [ ] Dashboard for analytics and monitoring
- [ ] Mobile app integration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Speech Recognition API](https://cloud.google.com/speech-to-text) for transcription services
- [TensorFlow](https://www.tensorflow.org/) for the deep learning framework
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [PyDub](https://github.com/jiaaro/pydub) for audio processing

## 📞 Contact & Support

- **Developer**: Marpu Sai Mahesh
- **Email**: chintusaimaheshmarpu@gmail.com
- **Phone**: +91 9502342564
- **LinkedIn**: [linkedin.com/in/marpumahesh](https://www.linkedin.com/in/marpumahesh/)
- **GitHub**: [github.com/saimahesh19](https://github.com/saimahesh19)
- **Location**: Andhra Pradesh, India

For bug reports and feature requests, please open an issue on GitHub.

## ⭐ Show Your Support

If this project helped you, please give it a ⭐️!

---

**Made with ❤️ by Marpu Sai Mahesh**

*Protecting against fraud, one audio file at a time!*
