import RPi.GPIO as GPIO
import time
from tkinter import *

class CarControl:
    # Initialize GPIO
    def __init__(self):
        # Identify GPIO
        self.PWMA = 16
        self.PWMB = 18
        self.IN1 = 11
        self.IN2 = 13
        self.IN3 = 15
        self.IN4 = 12
        self.speed = 50
        # Initialize GPIO
        self.init_gpio()
        # Create PWM objects for left and right motors
        self.L_Motor = GPIO.PWM(self.PWMA, 100)
        self.R_Motor = GPIO.PWM(self.PWMB, 100)
    
    def init_gpio(self):
        # Set warnings to False
        GPIO.setwarnings(False)
        # Set the GPIO mode to BOARD
        GPIO.setmode(GPIO.BOARD)
        # Set pins 13, 15, 16 to output
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        # Set the PWM pins to output
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.PWMB, GPIO.OUT)
        # Set the PWM to use the initial speed of 0
        pwm = GPIO.PWM(self.PWMA, 1000)
        pwm.start(0)

    def set_speed(self, val):
        # Set the speed to the given value
        self.speed = int(val)

    def turn_up(self, t_time):
        # Set the duty cycle of the PWM to the given value
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
        # Wait for the given time
        time.sleep(t_time)

    def turn_back(self, t_time):
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(t_time)

    def turn_left(self, t_time):
        # Set the duty cycle of the PWM to the given value
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,False)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
        time.sleep(t_time)

    def turn_right(self, t_time):
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,False)
        time.sleep(t_time)

    def car_stop(self, t_time):
        # Set the duty cycle of the PWM to 0
        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)

        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)
        time.sleep(t_time)

    def ConInterface(self):
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
        speed_slider = Scale(slidef, from_=100, to=50, orient=VERTICAL, label="Speed", command=self.set_speed)
        speed_slider.set(self.speed)

        # Create buttons
        up = Button(ctrlf, text="前进", command=lambda: self.turn_up(0.5), activeforeground="green", activebackground="yellow", height=1, width=4)
        left=Button(ctrlf,text="左转",command=lambda: self.turn_left(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        right=Button(ctrlf,text="右转",command=lambda: self.turn_right(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        back=Button(ctrlf,text="后退",command=lambda: self.turn_back(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        stop=Button(ctrlf,text="停止",command=lambda: self.car_stop(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)

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

        # Start the interaction window
        root.mainloop()

if __name__ == "__main__":
    # Create a car object
    car = CarControl()
    # Start the car
    car.L_Motor.start(car.speed)
    car.R_Motor.start(car.speed)

    try:
        # Start the control interface
        car.ConInterface()

    except KeyboardInterrupt:
        # Clean up the GPIO pins
        GPIO.cleanup()
