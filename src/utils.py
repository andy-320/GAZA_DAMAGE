import rasterio
import numpy as np

def read_tiff(path):

    with rasterio.open(path) as src:

        img = src.read()

        img = np.transpose(img, (1,2,0))

        meta = {
            "crs": src.crs,
            "transform": src.transform,
            "height": src.height,
            "width": src.width
        }

    return img, meta