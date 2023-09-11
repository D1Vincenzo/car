import sys
sys.path.append('/home/hxy/car')
from tkinter import *
from control.carcontrol import CarControl
import RPi.GPIO as GPIO
from PIL import Image, ImageTk
from cam.camera_stream import capture_stream

def ConInterface(car):
    # Create a Tkinter window, set the title, size and bg color
    root = Tk()
    root.title("Control")
    window_width = 800
    window_height = 600
    root.geometry("{}x{}".format(window_width, window_height))
    background = "#333333"
    root['bg'] = background
    # Make the window resizable
    root.resizable(width=True, height=True)

    # Create the frame for the video, controller and side
    video_height = window_height*0.5
    video_width = window_width*0.5
    videof = Frame(root, height=video_height, width=video_width, cursor="cross")

    ctrl_height = window_height*0.5
    ctrl_width = window_width*0.5
    ctrlf = Frame(root, height=ctrl_height, width=ctrl_width, cursor="circle", bg=background)

    slidef = Frame(root, height=100, width=100, cursor="plus", bg=background)

    # Create a speed slider and set the speed of it
    speed_slider = Scale(slidef, from_=100, to=25, orient=VERTICAL, label="Speed", command=car.set_speed)
    speed_slider.set(car.speed)

    # Create buttons
    up = Button(ctrlf, text="前进", command=lambda: car.turn_up(), activeforeground="green", activebackground="yellow", height=1, width=4)
    left=Button(ctrlf, text="左转",command=lambda: car.turn_left(), activeforeground="green",activebackground="yellow",height=1,width=4)
    right=Button(ctrlf, text="右转",command=lambda: car.turn_right(), activeforeground="green",activebackground="yellow",height=1,width=4)
    back=Button(ctrlf, text="后退",command=lambda: car.turn_back(), activeforeground="green",activebackground="yellow",height=1,width=4)
    stop=Button(ctrlf, text="停止",command=lambda: car.car_stop(), activeforeground="green",activebackground="yellow",height=1,width=4)

    # Place the frame in the window
    videof.place(relx=0.5, rely=0.1, anchor='n')
    ctrlf.place(relx=0.5, rely=0.9, anchor='s')
    slidef.place(relx=0.8, rely=0.6, anchor='nw')

    # Place the speed slider and buttons in the frame
    speed_slider.place(relx=0.5, rely=0.5, anchor='c')

    up.place(relx=0.5, rely=0.3, anchor='c')
    left.place(relx=0.3, rely=0.5, anchor='c')
    right.place(relx=0.7, rely=0.5, anchor='c')
    stop.place(relx=0.5, rely=0.5, anchor='c')
    back.place(relx=0.5, rely=0.7, anchor='c')


    video_label = Label(videof)
    video_label.pack(fill=BOTH, expand=YES)

    # Start the camera stream generator
    stream_gen = capture_stream()

    # Update the video frame in the Tkinter window
    update_video_frame(videof, video_label, stream_gen)

    # Start the interaction window
    root.mainloop()


def update_video_frame(videof, video_label, stream_gen):
    try:
        frame = next(stream_gen)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=image)
        video_label.config(image=photo)
        video_label.image = photo
        videof.after(10, update_video_frame, videof, video_label, stream_gen)
    except StopIteration:
        pass


if __name__ == "__main__":
    car = CarControl()
    car.LF_Motor.start(car.speed)
    car.LB_Motor.start(car.speed)
    car.RF_Motor.start(car.speed)
    car.RB_Motor.start(car.speed)
    try:
        ConInterface(car)

    except KeyboardInterrupt:
        pass

    GPIO.cleanup()




