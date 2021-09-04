# ascii_art

Python program to play videos in ascii form in the terminal

## Getting started

```
pip install pillow numpy python-opencv
```

## Running it

```
python vid2frames.py --video <video_path>
```

```
python videoascii.py --fps <fps>
```


## How it works

- Splits the video into frames and saves them in the /frames folder
- Converts the frames to grayscale at runtime
- uses a pixel intensity map to display the pixels on the screen as characters