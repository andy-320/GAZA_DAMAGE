import cv2
import numpy as np

def prepare_input(before, after):

    h = min(before.shape[0], after.shape[0])
    w = min(before.shape[1], after.shape[1])

    before = cv2.resize(before, (w,h))
    after = cv2.resize(after, (w,h))

    diff = after.astype(np.float32) - before.astype(np.float32)

    combined = np.concatenate([
        before,
        after,
        diff
    ], axis=-1)

    combined = combined.astype(np.float32)

    combined = (
        combined - combined.min()
    ) / (
        combined.max() - combined.min() + 1e-6
    )

    return combined, before, after