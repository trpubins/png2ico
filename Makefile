.PHONY: setup clean format run

# Define the Python version and virtual environment directory
PROJ_ROOT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
VENV_DIR := $(PROJ_ROOT_DIR).venv
PYTHON := python3.10

# Define the requirements files
REQUIREMENTS_DEV  := $(PROJ_ROOT_DIR)/requirements.txt
REQUIREMENTS_TEST := $(PROJ_ROOT_DIR)/tests/requirements.txt
REQUIREMENTS_SRC  := $(PROJ_ROOT_DIR)/src/requirements.txt

# The setup target creates a virtual env and installs packages.
# It depends on the virtual env activation script ($(VENV_DIR)/bin/activate).
# If this script doesn't exist, it will trigger the commands below to create the
# virtual env and install packages.
setup: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate:
	@echo "Setting up virtual environment using $(PYTHON)..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Upgrading pip..."
	$(VENV_DIR)/bin/pip install --upgrade pip
	@echo "Installing required Python packages..."
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_DEV)
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_TEST)
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_SRC)
	@echo "Virtual environment setup complete."

# Clean target to remove the virtual environment
clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)
	@echo "Clean complete."

# Format code using black and lint using ruff
format:
	$(VENV_DIR)/bin/$(PYTHON) -m black $(PROJ_ROOT_DIR)
	$(VENV_DIR)/bin/$(PYTHON) -m ruff check $(PROJ_ROOT_DIR)

# Run unit tests with coverage
test:
	$(VENV_DIR)/bin/$(PYTHON) -m pytest --cov=$(PROJ_ROOT_DIR)/src -s -v
