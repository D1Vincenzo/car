# camera_stream.py

# camera_stream.py

import cv2
import picamera
import picamera.array

def capture_stream():
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        with picamera.array.PiRGBArray(camera) as stream:
            while True:
                camera.capture(stream, 'bgr', use_video_port=True)
                frame = stream.array
                yield frame  # Yield the frame to be used elsewhere
                stream.truncate(0)


if __name__ == "__main__":
    capture_stream()
