from PIL import Image
import numpy as np

def image_to_pattern(image_path=None,):
    '''
    add comments here later.
    '''

    # check if an image is provided - if not, 
    if image_path is None:
        raise ValueError("Please provide an image to convert the ")

    # convert and resize image
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((100, 100))  # Resize to a manageable size

    # convert to an image array (?)
    img_array = np.array(img)
    return img_array