import requests
import io
from PIL import Image

import numpy as np
import torch 
import torchvision.transforms as transforms
import torchvision

from flask import Flask, jsonify, request
from utils import preprocess, load

labels = {0: 'bee', 1: 'dog'}
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"Greetings": "Hello"})

model = load()

@app.route("/api/predict", methods=['POST'])
def predict():
    file = request.files['file']
    image = file.read()
    img = Image.open(io.BytesIO(image))

    img_processed = preprocess(img)
    model.eval()

    with torch.no_grad():
        scores = model(img_processed.unsqueeze(0))
        scores = torch.nn.functional.softmax(scores, dim=1)
        _ , pred = scores.max(1)

    model.train()
    return jsonify({"animal" : labels[pred.item()], "per": _.item()*100})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)