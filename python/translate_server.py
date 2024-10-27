from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator
import os  # Import the os module

app = Flask(__name__)
CORS(app)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '')
        target_lang = data.get('target_lang', 'en')
        
        translation = translator.translate(text, dest=target_lang)
        
        return jsonify({
            'translation': translation.text,
            'source_lang': translation.src,
            'target_lang': translation.dest
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable
    app.run(host='0.0.0.0', port=port)  # Bind to 0.0.0.0

