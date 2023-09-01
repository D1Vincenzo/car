import picamera
import picamera.array
import cv2
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (800, 600)
    sleep(1)

    # Create a memory stream so photos doesn't need to be saved in a file
    with picamera.array.PiRGBArray(camera) as output:

        # camera.capture(output, 'rgb', use_video_port=True)
        for foo in camera.capture_continuous(output, 'rgb', use_video_port=True):

        # Use the camera to capture an image
            print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))

            # Convert the image from BGR to RGB
            dst = cv2.cvtColor(output.array, cv2.COLOR_RGB2BGR)

            # Show the image
            cv2.imshow("img", dst)
            

            # Clear the stream in preparation for the next frame
            output.truncate(0)

            # Exit on 'q' press
            if cv2.waitKey(1) == ord('q'):
                print("Exiting program.")
                break