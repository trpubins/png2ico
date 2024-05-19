import os
import sys

# add source code dir to system path, otherwise cannot import modules
PROJ_ROOT_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir
)
SRC_PATH = os.path.join(PROJ_ROOT_PATH, "src")
sys.path.append(PROJ_ROOT_PATH)
sys.path.append(SRC_PATH)

# test file paths
TEST_EVENTS_PATH = os.path.join(PROJ_ROOT_PATH, "tests", "events")
TEST_FILES_PATH = os.path.join(PROJ_ROOT_PATH, "tests", "files")
