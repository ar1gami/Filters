# Filters

An augmented reality project that generates an interactive portal in the camera video using real-time hand tracking. Through a natural gesture, the user can switch between **14 distinct visual filters** that are rendered live inside the portal.

## Features

- Real-time hand tracking using MediaPipe Hands.
- Perspective portal built dynamically from the tips of the index fingers and thumbs of both hands.
- **14 visual filters** applied exclusively within the portal area. ( increased from 8)
- Filter switching via gesture: bringing the hands closer together triggers the transition to the next filter in the sequence.
- Hysteresis system to prevent accidental changes due to tremors or tracking imprecision.
- **On-screen overlay** showing the current filter name and real-time FPS counter.

## Included Filters

| Filter | Description |
|--------|-------------|
| `filtro_grid` | Grid overlay on the original image |
| `filtro_1` | Duotone segmented by brightness thresholds |
| `filtro_2` | Black-and-white halftone dot pattern |
| `filtro_3` | Chromatic aberration with RGB channel separation |
| `filtro_5` | Thermal camera simulation using a colormap |
| `filtro_6` | Vintage sepia style with vignette and grain |
| `filtro_blanco` | Frosted glass effect on the image |
| `filtro_rosa` | Pink-magenta duotone halftone |
| `filtro_sketch` | **NEW** — Pencil sketch effect in black and white |
| `filtro_glitch` | **NEW** — Digital glitch with random band tearing and color shifts |
| `filtro_cartoon` | **NEW** — Cartoon / comic-book effect with enhanced edges |
| `filtro_emboss` | **NEW** — 3D emboss / relief effect using a convolution kernel |
| `filtro_negative` | **NEW** — Color negative (inverted colors) |
| `filtro_pixelate` | **NEW** — Pixel art / retro mosaic effect |

## Installation

Clone the repository:

```bash
git clone https://github.com/mishu006/Filters.git
cd Filters

## Create a virtual environment:

python -m venv venv

Activate it:
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux

## Install the dependencies:

pip install -r requirements.txt

## Usage

python main.py

## With the camera active, raise both hands with the index finger and thumb extended: the portal is automatically generated between them. Bring your hands closer together to "close" them and advance to the next filter in the list.

In the top-left corner of the window you will see:

The name of the current filter.

The FPS (frames per second) to monitor performance.

Press q while the window is active to end the execution.

Project Structure
Filters/
├── main.py            Entry point: capture loop and filter cycle
├── hand_tracking.py   Detection of extended fingers from landmarks
├── geometry.py        Portal geometry and closing gesture detection
├── filters.py         Definition of all **14 available filters**
├── requirements.txt
└── README.md

Extending the Project
To add a new filter, simply define a function in filters.py that receives a crop in BGR format (numpy.ndarray) and returns a crop of the same size:
def filtro_nuevo(roi: np.ndarray) -> np.ndarray:
    return roi

Then, add it to the FILTROS list at the end of the file, and add its corresponding name to the FILTER_NAMES list. The filter cycle automatically adjusts to the number of elements in the FILTROS list.

Tech Stack
Python 3.10

OpenCV

MediaPipe

NumPy

License
This project is distributed under the MIT License.
Original author: mishu006
