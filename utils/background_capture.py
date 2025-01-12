import cv2
import numpy as np

def capture_background(image_path: str) -> np.ndarray:
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path '{image_path}' could not be loaded.")
    background_subtractor = cv2.createBackgroundSubtractorMOG2()
    mask = background_subtractor.apply(image)
    background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
    return background

