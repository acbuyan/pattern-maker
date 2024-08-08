
import numpy as np

# maybe....?
# from PIL import Image
import skimage as ski

def image_to_pattern(image_path=None,
                     horizontal_stitches=100,
                     vertical_stitches=100):
    '''
    add comments here later.
    '''

    # check if an image is provided - if not, 
    if image_path is None:
        raise ValueError("Please provide an image to convert to a pattern.")

    # convert and resize image
    img = Image.open(image_path).convert('RGB')  # Convert to grayscale
    img = img.resize((horizontal_stitches, vertical_stitches))  # Resize to a manageable size

    # convert to an image array (?)
    img_array = np.array(img)

    # return array for further processing
    return img_array