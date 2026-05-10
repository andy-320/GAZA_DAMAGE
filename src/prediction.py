import torch
import numpy as np
import cv2

from config import PATCH_SIZE, STRIDE
from src.utils import read_tiff
from src.data_transformation import prepare_input
from src.model_loader import device

def predict_tiff(model, before_path, after_path):

    before, _ = read_tiff(before_path)

    after, _ = read_tiff(after_path)

    combined, before, after = prepare_input(before, after)

    H, W = before.shape[:2]

    pred_map = np.zeros((H,W))

    count_map = np.zeros((H,W))

    for i in range(0, H-PATCH_SIZE, STRIDE):

        for j in range(0, W-PATCH_SIZE, STRIDE):

            patch = combined[i:i+PATCH_SIZE, j:j+PATCH_SIZE]

            patch = np.transpose(patch, (2,0,1))

            inp = torch.tensor(patch).unsqueeze(0).float().to(device)

            with torch.no_grad():

                pred = torch.sigmoid(model(inp)).cpu().numpy()[0,0]

            pred_map[i:i+PATCH_SIZE, j:j+PATCH_SIZE] += pred

            count_map[i:i+PATCH_SIZE, j:j+PATCH_SIZE] += 1

    pred_map = pred_map / (count_map + 1e-6)

    return pred_map, before, after