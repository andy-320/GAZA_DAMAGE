from flask import Flask, render_template, request
import os
import cv2

from config import *
from src.model_loader import load_model
from src.data_ingestion import save_uploaded_files
from src.prediction import predict_tiff
from src.visualization import generate_outputs

app = Flask(__name__)

model = load_model()

@app.route("/")

def home():

    return render_template("index.html")

@app.route("/predict", methods=["POST"])

def predict():

    before_file = request.files["before"]

    after_file = request.files["after"]

    before_path, after_path = save_uploaded_files(
        before_file,
        after_file,
        UPLOAD_FOLDER
    )

    pred, before, after = predict_tiff(
        model,
        before_path,
        after_path
    )

    before_rgb = before[:,:,:3].astype("uint8")

    after_rgb = after[:,:,:3].astype("uint8")

    damage_percent, overlay, mask, heatmap = generate_outputs(
        pred,
        before_rgb,
        after_rgb,
        OUTPUT_FOLDER
    )

    return render_template(
        "result.html",
        damage=round(damage_percent,2),
        overlay=overlay,
        mask=mask,
        heatmap=heatmap
    )

if __name__ == "__main__":

    app.run(debug=True)