# War Conflict Damage Detection Using Satellite TIFF Images

AI-powered satellite image damage assessment system using Deep Learning and U-Net segmentation for detecting structural and urban damage from multi-temporal TIFF imagery.

---

# Project Overview

This project performs automated damage detection using pre-disaster and post-disaster satellite TIFF images.

The system uses a U-Net deep learning segmentation model trained on satellite imagery patches to identify damaged regions and estimate overall damage percentage.

The application provides:

- Damage segmentation masks
- Heatmap visualization
- Overlay predictions
- Damage percentage estimation
- Interactive Flask web application

---

# Features

- Multi-temporal satellite image analysis
- TIFF image support
- U-Net semantic segmentation
- Damage percentage estimation
- Prediction heatmaps
- Binary damage masks
- Overlay visualization
- Flask-based web application
- Responsive modern UI
- Fullscreen result viewer
- Modular ML pipeline structure

---

# Technologies Used

## Deep Learning

- PyTorch
- segmentation-models-pytorch
- U-Net Architecture

## Image Processing

- OpenCV
- Rasterio
- NumPy
- Albumentations

## Backend

- Flask

## Frontend

- HTML5
- CSS3
- JavaScript

---

# Project Structure

```text
GAZA_PRO/
│
├── Dataset/
│
├── models/
│   └── best_model.pth
│
├── notebook/
│   └── training.ipynb
│
├── src/
│   ├── components/
│   ├── pipeline/
│   └── utils/
│
├── static/
│   ├── css/
│   ├── images/
│   └── results/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── config.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# Dataset Structure

Organize dataset as:

```text
Dataset/
│
├── area_1/
│   ├── before.tif
│   ├── after.tif
│   ├── before_mask.tif
│   └── after_mask.tif
│
├── area_2/
│
└── ...
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### CMD

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Training the Model

Open:

```text
notebook/training.ipynb
```

Run all cells to:

- Read TIFF images
- Generate patches
- Apply augmentation
- Train U-Net model
- Evaluate performance
- Save best model

Saved model:

```text
models/best_model.pth
```

---

# Run Flask Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Workflow

## Training Pipeline

```text
Satellite TIFF Images
        ↓
Patch Generation
        ↓
Data Augmentation
        ↓
U-Net Training
        ↓
Best Model Saving
```

---

## Prediction Pipeline

```text
Upload TIFF Images
        ↓
Image Preprocessing
        ↓
Model Prediction
        ↓
Damage Segmentation
        ↓
Heatmap Generation
        ↓
Damage Percentage Calculation
        ↓
Visualization on Webpage
```

---

# Outputs

The system generates:

- Overlay prediction image
- Damage highlighted image
- Binary damage mask
- Prediction heatmap
- Estimated damage percentage

---

# Example Results

## Overlay Prediction

Shows heatmap blended with post-disaster image.

## Damage Highlight

Displays damaged regions in red.

## Binary Mask

Shows segmented damaged areas.

## Heatmap

Displays model confidence distribution.

---

# Future Improvements

- Attention U-Net integration
- Transformer-based segmentation
- Real-time satellite stream support
- Cloud deployment
- Multi-class damage classification
- GIS integration
- Geo-referenced output export

---

# Research Applications

- Disaster management
- War zone assessment
- Urban damage monitoring
- Humanitarian response
- Infrastructure monitoring
- Remote sensing analysis

---

# Author

Developed by Harsh

---

# License

This project is developed for educational and research purposes

