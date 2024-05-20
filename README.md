# png2ico

Convert PNG images to ICO icons.

## Getting Started

### Setup

Run the following command to setup a Python virtual env and install required packages.

```bash
make setup
```

### Formatting

This project uses `black` to format code and `ruff` to lint. Run the following target to do both:

```bash
make format
```

### Unit Tests

This project leverages `pytest` for unit testing. Run the following command to run all unit tests:

```bash
make test
```

## Usage

A CLI has been supplied to run the image converter. Using a virtual env with the required packages can be run like so from the project root dir:

```bash
python src/main.py --png <path-to-png-file> [--output-dir <path-to-output-dir>]
```

The CLI also includes a help flag to provide more information on available commands.

```bash
python src/main.py --help
```
