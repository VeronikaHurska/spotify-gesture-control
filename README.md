# SPOTIFY Gesture controll system
![header](header.png)


This project is an implementation of gesture-based controls for Spotify using hand tracking and machine learning. It leverages TensorFlow for gesture recognition, MediaPipe for hand tracking, and Spotipy for controlling Spotify.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Project Overview

The Spotify Gesture Control project allows users to control Spotify using hand gestures. For example, you can swipe left to skip to the previous track or swipe right to skip to the next track. The system uses computer vision and deep learning to recognize these gestures in real-time.

## Features

- Hand tracking using MediaPipe.
- Gesture recognition using a TensorFlow model.
- Gesture smoothing using Exponential Moving Average (EMA).
- Control Spotify playback (next/previous track) with gestures.
- Configurable parameters for fine-tuning performance.

## Installation

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)
- Spotify Developer Account

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/spotify-gesture-control.git
    cd spotify-gesture-control
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Spotify credentials:**

   Get your Spotify API credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

   Set the following environment variables in your shell or `.env` file:

    ```bash
    export SPOTIPY_CLIENT_ID='your_client_id'
    export SPOTIPY_CLIENT_SECRET='your_client_secret'
    export SPOTIPY_REDIRECT_URI='your_redirect_uri'
    ```

## Configuration

Configuration options can be adjusted in `config.py`:

```python
MODEL_PATH = 'model_318.keras'
SEQUENCE_LENGTH = 25
SWIPE_THRESHOLD = 0.3
CONSISTENT_FRAMES = 5
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 30
```
## Usage

Run the main script:

``` bash
python main.py
```

## Project Structure
```sh
gesture_control/
│
├── main.py                    # Entry point of the application
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── gesture_detector/
│   ├── __init__.py
│   ├── detector.py            # Main gesture detection logic
│   ├── model_loader.py        # Handles loading the TensorFlow model
│   ├── hand_tracker.py        # Handles hand tracking using MediaPipe
│   ├── gesture_smoother.py    # Smooths gesture predictions using EMA
│   └── spotify_controller.py  # Controls Spotify playback using Spotipy
└── utils/
    ├── __init__.py
    ├── logger.py              # Logging setup (optional)
    └── warnings_handler.py    # Suppresses unnecessary warnings
```
## How It Works

1. Hand Tracking: The system uses MediaPipe to detect hand landmarks in real-time.
2. Gesture Recognition: A TensorFlow model predicts gestures based on hand movement sequences.
3. Gesture Smoothing: The Exponential Moving Average (EMA) technique is applied to filter out noise and make predictions more stable.
4. Spotify Control: Based on the detected gesture, Spotify is controlled using the Spotipy library.

## Troubleshooting
1. TensorFlow Warnings: You might see some warnings from TensorFlow. You can suppress them using the included warning handler.
2. Spotify Authentication Issues: Make sure your environment variables are set correctly. Double-check your Spotify API credentials.
3. Performance Issues: If you experience lag, try adjusting the FPS or reducing the SEQUENCE_LENGTH in the configuration.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for more information.

MIT License

Copyright (c) 2024 Hurska Veronika Andriivna