"""CLI script.
(1) Converts a PNG file into ICO icon file of various sizes.
"""

import logging
import os
import sys

import click
from topshelfsoftware_util.log import get_logger

from image_converter import convert_png2ico
# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(__name__, level=logging.INFO)

# --------------------------------------------------------------------------- #
#                                --- MAIN ---                                 #
# --------------------------------------------------------------------------- #
@click.command()
@click.option("-p", "--png", required=True, type=str,
              help="Path to the PNG file to be converted.")
@click.option("-o", "--output-dir", required=False, type=str, default='./output', show_default=True,
              help="Path to the output directory.")
def run(png: str, output_dir: str = "output"):
    """Converts a PNG file into ICO icon file of various sizes."""
    
    logger.info("Running...")

    # validate provided path
    if not os.path.exists(png):
        err_msg = f"Path does not exist: {png}."
        logger.error(err_msg)
        sys.exit("Exiting script")

    convert_png2ico(png, output_dir)


if __name__ == "__main__":
    run()
