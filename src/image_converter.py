import logging
import os

from PIL import Image

from topshelfsoftware_util.log import get_logger
# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(__name__, level=logging.INFO)

# --------------------------------------------------------------------------- #
#                                --- MAIN ---                                 #
# --------------------------------------------------------------------------- #
def convert_png2ico(
    png_fp: str,
    output_dir: str = "output",
    icon_sizes: list[tuple] = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
) -> str:
    """
    Convert a PNG image to ICO format with multiple icon sizes.

    Parameters
    ----------
    png_fp: str
        Path to the input PNG file.
    
    output_dir: str, Optional
        Directory to save the output ICO file.
        Default is './output/".
    
    icon_sizes: list[tuple], Optional
        List of sizes to store in the ICO file.
        Default is all of the following: 16x16, 32x32, 48x48, 64x64, 128x128, and 256x256.
    
    Returns
    ----------
    str
        Path to the resulting ICO file.
    """
    # Open the PNG image
    logger.info(f"Loading PNG to memory: {png_fp}")
    img = Image.open(png_fp)

    # Generate output filename based on PNG file
    png_basename, _ = os.path.splitext(os.path.basename(png_fp))
    ico_fn = os.path.join(output_dir, f"{png_basename}.ico")

    # Create the output dir as needed
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the image as ICO file with the specified sizes
    logger.info(f"Saving ICO to '{ico_fn}' dir with the following sizes: {icon_sizes}")
    img.save(ico_fn, format="ICO", sizes=icon_sizes)
    
    return ico_fn
