from PIL import Image
from rembg import remove
import numpy as np

def extract_background_and_foreground(image_path):
    # Load the input image
    input_image = Image.open(image_path)
    # Remove the background to get the foreground
    foreground_image = remove(input_image)
    # Ensure the output image has an alpha channel
    foreground_image = foreground_image.convert('RGBA')
    # Create a mask from the alpha channel
    alpha = foreground_image.split()[-1]
    background_mask = Image.eval(alpha, lambda a: 255 - a)
    # Convert images to numpy arrays
    original_np = np.array(input_image.convert('RGBA'))
    background_mask_np = np.array(background_mask)
    # Apply the mask to the original image to get the background
    background_np = original_np.copy()
    background_np[:, :, 3] = background_mask_np  # Set alpha channel to the inverted mask
    # Convert back to PIL Image
    background_image = Image.fromarray(background_np, 'RGBA')
    return foreground_image, background_image
