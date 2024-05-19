import os

import pytest

from topshelfsoftware_util.io import cdtmp
from topshelfsoftware_util.log import get_logger

from conftest import get_json_files
# ----------------------------------------------------------------------------#
#                               --- Globals ---                               #
# ----------------------------------------------------------------------------#
from __setup__ import TEST_EVENTS_PATH, TEST_FILES_PATH
MODULE = "image_converter"

# ----------------------------------------------------------------------------#
#                               --- Logging ---                               #
# ----------------------------------------------------------------------------#
logger = get_logger(f"test_{MODULE}")

# ----------------------------------------------------------------------------#
#                           --- Lambda Imports ---                            #
# ----------------------------------------------------------------------------#
from src.image_converter import convert_png2ico

# ----------------------------------------------------------------------------#
#                                --- TESTS ---                                #
# ----------------------------------------------------------------------------#
@pytest.mark.parametrize("event_dir", [TEST_EVENTS_PATH])
@pytest.mark.parametrize("event_file", get_json_files(TEST_EVENTS_PATH, "png2ico"))
def test_01_convert_png2ico(get_event_as_dict):
    png_fp = os.path.join(TEST_FILES_PATH, get_event_as_dict["files"]["png_fn"])
    logger.info("Testing convert_png2ico in temp dir")
    with cdtmp():
        ico_fp = convert_png2ico(png_fp)
        logger.info(f"Asserting ICO file '{ico_fp}' exists")
        assert os.path.exists(ico_fp)
        