from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this import
import os
import logging
import numpy as np  # Keep this for float32 conversion
from transcriber import transcribe_audio

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return "Welcome to the Flask Transcription Service!"

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Check the file type (optional, but recommended)
        if not file.filename.lower().endswith(('.wav', '.mp3', '.m4a')):
            return jsonify({'error': 'Invalid file type. Only .wav, .mp3, or .m4a files are allowed.'}), 400
        
        # Avoid filename collisions by using a unique filename
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        logging.info(f"File saved to {filepath}")

        result = transcribe_audio(filepath)
        
        # Convert any non-JSON serializable objects (like float32) to standard Python types
        if 'classification' in result and 'probability' in result['classification']:
            result['classification']['probability'] = float(result['classification']['probability'])

        return jsonify(result)
    except Exception as e:
        logging.error(f"Error during file upload: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


# from flask import Flask, request, jsonify
# import os
# import logging
# from transcriber import transcribe_audio

# app = Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# # Set up logging
# logging.basicConfig(level=logging.INFO)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part in the request'}), 400
        
#         file = request.files['file']
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'}), 400

#         # Check the file type (optional, but recommended)
#         if not file.filename.lower().endswith(('.wav', '.mp3', '.m4a')):
#             return jsonify({'error': 'Invalid file type. Only .wav, .mp3, or .m4a files are allowed.'}), 400
        
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
#         logging.info(f"File saved to {filepath}")

#         result = transcribe_audio(filepath)
        
#         return jsonify(result)
#     except Exception as e:
#         logging.error(f"Error during file upload: {str(e)}")
#         return jsonify({'error': str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')
  






# from flask import Flask, request, jsonify
# import os
# from transcriber import transcribe_audio

# app = Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part in the request'}), 400
        
#         file = request.files['file']
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'}), 400
        
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)

#         result = transcribe_audio(filepath)
        
#         return jsonify(result)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')


# from flask import Flask, request, jsonify
# import os
# from transcriber import transcribe_audio

# app = Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400
    
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
    
#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)

#     # Transcribe the uploaded file
#     transcript = transcribe_audio(filepath)
    
#     return jsonify({'transcription': transcript})

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')
