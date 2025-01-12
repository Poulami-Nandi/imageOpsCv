import cv2
import numpy as np

def generate_mask(image_path: str, lower_hsv: tuple, upper_hsv: tuple) -> np.ndarray:
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path '{image_path}' could not be loaded.")
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_hsv, upper_hsv)
    return mask

