# VisionTuner

VisionTuner is a Python application for image processing. It doesn't use the pre-built algorithms, they are implemented from scratch.

## Features

- **Image Resizing**: Resize images using different algorithms:
  - Nearest Neighbor
  - Bilinear Interpolation (not implemented)
  - Bicubic Interpolation (not implemented)
  - Lanczos Resampling (not implemented)

- **Image Mirroring**: Mirror images horizontally, vertically, or both.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/713koukou-naizaa/visionTuner.git
    cd visionTuner
    ```

2. Install the required packages:

    ```sh
    pip install opencv-python-headless numpy
    ```

## Usage

Run the main script to start the application:

```sh
python visionTuner.py
```
