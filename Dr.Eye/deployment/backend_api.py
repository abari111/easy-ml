from flask import Flask, render_template, request
import io
from utils import predict_ret_stade
app = Flask(__name__)


@app("/")
def home():
    return render_template('home.html')


@app("/api/predict", methods=['POST'])
def predict():
    data = request.files['file']
    image = io.BytesIO(data)
