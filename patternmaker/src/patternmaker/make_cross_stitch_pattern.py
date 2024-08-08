from .get_DMC import get_dmc_hex
from .image_to_pattern import image_to_pattern

def make_cross_stitch_pattern(image_path=None,
                              dmc=True,
                              anchor=False,
                              madeira=False):

    # ensure you only get one 
    if anchor or madeira:
        dmc=False

    if dmc:
        dmc_hex = get_dmc_hex()
    # elif anchor:
    #     anchor_hex = get_anchor_hex()
    # elif madeira:
    #     anchor_hex = get_madeira_hex()
    else:
        raise ValueError("Please specify a cross stitch colour scheme to use.")

    if image_path is None:
        raise ValueError("Please provide an image to convert to a pattern.")
    
    pattern_grid = image_to_pattern(image_path=image_path)