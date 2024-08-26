# SPOTIFY Gesture controll system
![header](header.png)


## Project structure
```sh
gesture_control/
│
├── main.py
├── config.py
├── gesture_detector/
│   ├── __init__.py
│   ├── detector.py
│   ├── model_loader.py
│   ├── hand_tracker.py
│   ├── gesture_smoother.py
│   └── spotify_controller.py
└── utils/
    ├── __init__.py
    ├── logger.py
    └── warnings_handler.py
```


## Environment variables
```sh
SPOTIPY_CLIENT_ID='XXX'
SPOTIPY_CLIENT_SECRET='XXX'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
```