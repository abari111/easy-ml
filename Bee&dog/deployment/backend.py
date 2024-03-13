from flask import Flask, jsonify, request
import torch 
import torchvision.transforms as transforms
import torchvision
from PIL import Image
import io
import numpy as np
import requests
labels = {0: 'bee', 1: 'dog'}
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return jsonify({"hello": "kevin"})


def load():
    model_path = "model.pht"
    model = torch.load(model_path)
    return model

from utils import preprocess
# Chargement du model
model = load()




@app.route("/api/predict", methods=['POST'])
def predict():
    # recuperer l'image
    file = request.files['file']
    image = file.read()

    # Ouvrir l'image
    img = Image.open(io.BytesIO(image))
    print(img)

    #traitement de l'image
    img_processed = preprocess(img)
    model.eval()
    with torch.no_grad():
        scores = model(img_processed.unsqueeze(0))
        scores = torch.nn.functional.softmax(scores, dim=1)
        _ , pred = scores.max(1)
        #print(labels[pred.item()], f': {_}')
    model.train()

    # predictions
    return jsonify({"animal" : labels[pred.item()], "per": _.item()*100})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)