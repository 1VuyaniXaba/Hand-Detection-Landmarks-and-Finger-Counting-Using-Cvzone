# Hand-Detection-Landmarks-and-Finger-Counting-Using-Cvzone
This real-time hand-tracking program uses OpenCV and a hand detector to follow up to two hands through your webcam. Each frame is mirrored, hands are outlined with landmarks and bounding boxes, and the fingers raised on the first detected hand are counted and shown on screen. Press q to quit, and the camera is released cleanly.
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

- Python 3.8 or newer
- A working webcam
- Python packages:
  - `opencv-python`
  - `cvzone`
  - `mediapipe`

## Installation

```bash
pip install opencv-python cvzone mediapipe
```

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
