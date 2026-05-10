import torch
import segmentation_models_pytorch as smp
from config import MODEL_PATH

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model():

    model = smp.Unet(
        encoder_name="resnet34",
        encoder_weights=None,
        in_channels=9,
        classes=1
    )

    model.load_state_dict(
        torch.load(MODEL_PATH, map_location=device)
    )

    model.to(device)

    model.eval()

    return model