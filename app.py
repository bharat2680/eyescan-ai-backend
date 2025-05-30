from flask import Flask, request, jsonify
from PIL import Image
import io
import numpy as np

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_eye():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']
    img = Image.open(image_file).convert('RGB')

    # Simulated AI logic – placeholder
    np_image = np.array(img)
    result = "AI Diagnosis: No obvious issues detected."

    return jsonify({"diagnosis": result})

if __name__ == '__main__':
    app.run()
