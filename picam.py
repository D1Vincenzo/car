# -*- coding: utf-8 -*-

from time import sleep
from picamera import PiCamera

def open_preview():
    with PiCamera() as camera:
        camera.resolution = (1024, 768)

        camera.start_preview()
        sleep(5)

def capture_preview():
    with PiCamera() as camera:
        camera.resolution = (320, 240)

        camera.start_preview()

        for i in range(5):
            sleep(i)

            camera.capture(str(i) + ".jpg", resize=(80, 60))

    # 当获取到 PiCamera() 对象后就已经打开摄像头了，并不一定需要调用 camera.start_preview() 进行预览后才能保存图像
    # capture(output, format=None, use_video_port=False, resize=None, splitter_port=0, bayer=False, **options)
    '''
    format: 
    'jpeg' - Write a JPEG file
    'png' - Write a PNG file
    'gif' - Write a GIF file
    'bmp' - Write a Windows bitmap file
    'yuv' - Write the raw image data to a file in YUV420 format
    'rgb' - Write the raw image data to a file in 24-bit RGB format
    'rgba' - Write the raw image data to a file in 32-bit RGBA format
    'bgr' - Write the raw image data to a file in 24-bit BGR format
    'bgra' - Write the raw image data to a file in 32-bit BGRA format
    'raw' - Deprecated option for raw captures; the format is taken from the deprecated raw_format attribute
    '''

def record_video():

    with PiCamera() as camera:
        camera.resolution = (320, 240)

        camera.start_preview()
        camera.start_recording('my.h264')

        camera.wait_recording(10)
        camera.stop_recording()

    '''
    format:
    'h264' - Write an H.264 video stream
    'mjpeg' - Write an M-JPEG video stream
    'yuv' - Write the raw video data to a file in YUV420 format
    'rgb' - Write the raw video data to a file in 24-bit RGB format
    'rgba' - Write the raw video data to a file in 32-bit RGBA format
    'bgr' - Write the raw video data to a file in 24-bit BGR format
    'bgra' - Write the raw video data to a file in 32-bit BGRA format
    '''

if __name__ == '__main__':
    record_video()

