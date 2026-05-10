import cv2
import numpy as np
import os

from config import THRESHOLD, MIN_COMPONENT_AREA

def generate_outputs(pred, before_rgb, after_rgb, output_folder):

    pred_norm = pred / (pred.max() + 1e-6)

    pred_norm = np.power(pred_norm, 0.6)

    damage_mask = (pred_norm > THRESHOLD).astype(np.uint8)

    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
        damage_mask,
        connectivity=8
    )

    clean_mask = np.zeros_like(damage_mask)

    for i in range(1, num_labels):

        area = stats[i, cv2.CC_STAT_AREA]

        if area > MIN_COMPONENT_AREA:

            clean_mask[labels == i] = 1

    damage_mask = clean_mask

    damage_pixels = np.sum(damage_mask)

    diff = cv2.absdiff(before_rgb, after_rgb)

    diff_gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

    urban_mask = diff_gray > 25

    urban_pixels = np.sum(urban_mask)

    damage_percent = (
        damage_pixels / (urban_pixels + 1e-6)
    ) * 100

    heatmap = cv2.applyColorMap(
        (pred_norm * 255).astype(np.uint8),
        cv2.COLORMAP_HOT
    )

    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

    overlay = cv2.addWeighted(
        after_rgb,
        0.45,
        heatmap,
        0.55,
        0
    )

    highlight = after_rgb.copy()

    highlight[damage_mask == 1] = [255,0,0]

    damage_overlay = cv2.addWeighted(
        after_rgb,
        0.7,
        highlight,
        0.3,
        0
    )

    os.makedirs(output_folder, exist_ok=True)

    overlay_path = os.path.join(
        output_folder,
        "overlay.png"
    )

    mask_path = os.path.join(
        output_folder,
        "mask.png"
    )

    heatmap_path = os.path.join(
        output_folder,
        "heatmap.png"
    )

    cv2.imwrite(
        overlay_path,
        cv2.cvtColor(damage_overlay, cv2.COLOR_RGB2BGR)
    )

    cv2.imwrite(
        mask_path,
        damage_mask * 255
    )

    cv2.imwrite(
        heatmap_path,
        cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)
    )

    return damage_percent, overlay_path, mask_path, heatmap_path