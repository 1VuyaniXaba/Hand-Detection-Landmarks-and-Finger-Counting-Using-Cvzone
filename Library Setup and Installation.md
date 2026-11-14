# Hand Finger Counter

A real-time hand-tracking program that uses OpenCV and cvzone to detect hands through your webcam, count how many fingers are raised on the first detected hand, and display the result on the video feed.

## Features

- Detects up to two hands at once
- Draws hand landmarks and bounding boxes on each frame
- Counts the raised fingers on the first detected hand and shows the count on screen
- Mirrors the video so it feels natural to use
- Prints a start-up timestamp (year, month, day, hour, minute)
- Releases the camera and closes all windows cleanly on exit

## Requirements

- Python 3.8 or newer (check that your version is supported by `mediapipe`)
- A working webcam
- `pip` (comes with Python)

## Libraries Used

| Import in code | Install name (pip) | What it does |
|---|---|---|
| `cv2` | `opencv-python` | Opens the camera, reads frames, draws on them and shows the window |
| `cvzone.HandTrackingModule` | `cvzone` | Provides `HandDetector` for finding hands and counting fingers |
| `mediapipe` | `mediapipe` | The hand-tracking model that cvzone uses behind the scenes |
| `numpy` | `numpy` | Installed automatically with OpenCV, used for image arrays |
| `time` | (built in) | Gives the start-up timestamp. Nothing to install |

Note that the import name and the pip name are different for OpenCV: you `import cv2` but install `opencv-python`.

## Installation

### 1. Check that Python and pip are installed

```bash
python --version
pip --version
```

On macOS/Linux you may need `python3` and `pip3` instead. If Python is missing, download it from https://www.python.org/downloads/ (on Windows, tick **Add Python to PATH** during setup).

### 2. (Recommended) Create a virtual environment

This keeps the project's libraries separate from the rest of your system.

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

When it is active, you will see `(venv)` at the start of your terminal line.

### 3. Install all the libraries

Install everything in one command:

```bash
pip install opencv-python cvzone mediapipe
```

Or install them one at a time:

```bash
pip install opencv-python
pip install cvzone
pip install mediapipe
```

### 4. (Optional) Use a requirements file

Create a file named `requirements.txt` in the project folder containing:

```
opencv-python
cvzone
mediapipe
```

Then anyone can install everything with:

```bash
pip install -r requirements.txt
```

### 5. Check that the install worked

```bash
python -c "import cv2, cvzone, mediapipe; print('All libraries installed')"
```

If it prints `All libraries installed`, you are ready to run the program.

### Common install problems

- **`pip` is not recognized**: use `python -m pip install opencv-python cvzone mediapipe` instead.
- **`mediapipe` fails to install**: your Python version may be too new or too old for it. Try a version Mediapipe supports (for example Python 3.10 or 3.11), ideally inside a fresh virtual environment.
- **Permission errors**: add `--user` (`pip install --user ...`) or use a virtual environment.
- **`No module named cv2`**: the install went into a different Python. Make sure your virtual environment is activated, or run the script with the same Python you installed into.
- **Conflicting OpenCV packages**: if you have both `opencv-python` and `opencv-contrib-python` installed, uninstall both and reinstall just `opencv-python`.

## Usage

1. Connect your webcam.
2. Run the script:

   ```bash
   python main.py
   ```

3. Hold your hand in front of the camera. The window titled **Hand Detector** shows the live feed with landmarks, a bounding box and the finger count.
4. Press **q** to quit.

## How It Works

1. **Imports** - OpenCV (`cv2`) handles the camera and display, `HandDetector` from cvzone detects hands, and `time` supplies the start-time information.
2. **Timestamp** - `time.localtime()[0:5]` prints the date and time the program started.
3. **Camera setup** - Opens camera `0` and requests a frame size of 640 x 480 pixels.
4. **Detector setup** - Creates a `HandDetector` configured for up to two hands.
5. **Frame loop** - Each frame is read, flipped horizontally, then passed to the detector, which finds the hands and draws landmarks and bounding boxes.
6. **Finger counting** - If a hand is found, the raised fingers on the first hand are counted and the number is written onto the video.
7. **Display** - The processed frames appear in the **Hand Detector** window. Pressing `q` exits the loop.
8. **Cleanup** - OpenCV windows are closed and the camera is released.

## Customization

- **Colors**: cvzone's built-in drawing uses fixed colors. To change them, call `findHands(draw=False)` and draw the landmarks and box yourself with OpenCV (colors are in BGR order).
- **Number of hands**: change `maxHands` in the `HandDetector` setup.
- **Detection sensitivity**: change `detectionCon` (0 to 1). Higher values are stricter.
- **Camera**: change the index in `cv2.VideoCapture(0)` if you have more than one camera.

## Troubleshooting

- **Black window or "Camera capture FAILED"**: check that no other app is using the webcam, or try a different camera index.
- **Hands not detected**: improve the lighting and keep your whole hand inside the frame.
- **Import errors**: make sure all packages above are installed in the Python environment you are running.
