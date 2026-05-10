import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "static/results")

MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pth")

ALLOWED_EXTENSIONS = {"tif", "tiff"}

PATCH_SIZE = 256
STRIDE = 64

THRESHOLD = 0.25
MIN_COMPONENT_AREA = 40