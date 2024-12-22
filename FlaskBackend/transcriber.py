import speech_recognition as sr
from pydub import AudioSegment
import os
import joblib
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Updated paths to your new project structure
TOKENIZER_PATH = r"pretrained_models_datasets\\fraud_words_tokenizer.joblib"
MODEL_PATH = r"pretrained_models_datasets\\fraud_words_rnn_model.h5"  # Ensure the model file is .h5

# Load the tokenizer and model
try:
    tokenizer = joblib.load(TOKENIZER_PATH)
    classification_model = load_model(MODEL_PATH)
except Exception as e:
    logging.error(f"Error loading tokenizer or model: {e}")
    raise  # Raise the exception to stop further execution

def convert_to_wav(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="wav")
    except Exception as e:
        logging.error(f"Error converting file {input_file} to {output_file}: {e}")
        raise  # Raise the exception to indicate failure

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    output_file = file_path.replace('.m4a', '.wav')

    try:
        convert_to_wav(file_path, output_file)

        with sr.AudioFile(output_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            classification_result = classify_text(text)
            return {'transcription': text, 'classification': classification_result}
    except sr.UnknownValueError:
        return {'transcription': "Audio not clear enough to transcribe", 'classification': None}
    except sr.RequestError:
        return {'transcription': "Could not request results from Google Speech Recognition service", 'classification': None}
    except Exception as e:
        logging.error(f"Error during transcription: {e}")
        return {'transcription': "Error occurred during transcription", 'classification': None}
    finally:
        # Ensure the temporary file is deleted if it exists
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except Exception as e:
                logging.error(f"Error deleting temporary file {output_file}: {e}")

def classify_text(text):
    try:
        # Tokenize and pad the input text
        new_seq = tokenizer.texts_to_sequences([text])
        new_pad = pad_sequences(new_seq, maxlen=100)
        
        # Predict using the new model
        prediction = classification_model.predict(new_pad)
        if prediction.shape[0] > 0 and prediction.shape[1] > 0:
            probability = prediction[0][0]
            predicted_label = 'fraud' if int(round(probability)) == 1 else 'normal'
            return {
                'predicted_label': predicted_label,
                'probability': float(probability)  # Convert to Python float
            }
        else:
            logging.warning("Unexpected prediction output shape.")
            return {'predicted_label': 'Unknown', 'probability': None}
    except Exception as e:
        logging.error(f"Error during classification: {e}")
        return {'predicted_label': 'Error', 'probability': None}
