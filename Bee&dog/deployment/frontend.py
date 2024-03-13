import streamlit as st
from PIL import Image
import requests
import torch

st.title("Bee&Dog")

upload = st.file_uploader("Chargez l'image de votre objet",
                           type=['png', 'jpeg', 'jpg'])

c1, c2 = st.columns(2)

if upload:
    files = {"file" :  upload.getvalue()}

    req = requests.post("http://127.0.0.1:8080/api/predict", files=files)
    resultat = req.json()
    label = resultat["animal"]
    per = resultat["per"]

    c1.image(Image.open(upload))
    c2.write(f"The animal is a {label} predicted with {per:.2f}%")