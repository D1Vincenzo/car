import RPi.GPIO as GPIO
import time
from tkinter import *

class CarControl:
    # Initialize GPIO
    def __init__(self):
        # Identify GPIO
        self.PWMA = 16
        self.PWMB = 18
        # 左前轮
        self.IN1 = 11
        self.IN2 = 13
        # 左后轮
        self.IN3 = 15
        self.IN4 = 12
        
        # Define GPIO for right wheels
        self.PWMC = 37  # Assuming these pins, you can change them
        self.PWMD = 31
        # 右前轮
        self.IN5 = 35
        self.IN6 = 33
        # 右后轮
        self.IN7 = 36
        self.IN8 = 38
        
        self.speed = 50
        # Initialize GPIO
        self.init_gpio()
        # Create PWM objects for all motors
        self.LF_Motor = GPIO.PWM(self.PWMA, 100)  # Left Front Motor
        self.LB_Motor = GPIO.PWM(self.PWMB, 100)  # Left Back Motor
        self.RF_Motor = GPIO.PWM(self.PWMC, 100)  # Right Front Motor
        self.RB_Motor = GPIO.PWM(self.PWMD, 100)  # Right Back Motor
    
    def init_gpio(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        # Set pins for left wheels
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.PWMB, GPIO.OUT)
        # Set pins for right wheels
        GPIO.setup(self.IN5, GPIO.OUT)
        GPIO.setup(self.IN6, GPIO.OUT)
        GPIO.setup(self.IN7, GPIO.OUT)
        GPIO.setup(self.IN8, GPIO.OUT)
        GPIO.setup(self.PWMC, GPIO.OUT)
        GPIO.setup(self.PWMD, GPIO.OUT)
        # Start PWM for left wheels
        pwmA = GPIO.PWM(self.PWMA, 1000)
        pwmA.start(0)
        pwmB = GPIO.PWM(self.PWMB, 1000)
        pwmB.start(0)
        # Start PWM for right wheels
        pwmC = GPIO.PWM(self.PWMC, 1000)
        pwmC.start(0)
        pwmD = GPIO.PWM(self.PWMD, 1000)
        pwmD.start(0)

    def set_speed(self, val):
        # Set the speed to the given value
        self.speed = int(val)

    def turn_up(self, t_time):
        # Control left front wheel
        self.LF_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)
        # Control left back wheel
        self.LB_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        # Control right front wheel
        self.RF_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN5, GPIO.HIGH)
        GPIO.output(self.IN6, GPIO.LOW)
        # Control right back wheel
        self.RB_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN7, GPIO.LOW)
        GPIO.output(self.IN8, GPIO.HIGH)
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
        # Control left front wheel
        self.LF_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)
        # Control left back wheel
        self.LB_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)
        # Control right front wheel
        self.RF_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN5, False)
        GPIO.output(self.IN6, False)
        # Control right back wheel
        self.RB_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN7, False)
        GPIO.output(self.IN8, False)
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
        speed_slider = Scale(slidef, from_=100, to=25, orient=VERTICAL, label="Speed", command=self.set_speed)
        speed_slider.set(self.speed)

        # Create buttons
        up = Button(ctrlf, text="前进", command=lambda: self.turn_up(0.5), activeforeground="green", activebackground="yellow", height=1, width=4)
        left=Button(ctrlf, text="左转",command=lambda: self.turn_left(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        right=Button(ctrlf, text="右转",command=lambda: self.turn_right(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        back=Button(ctrlf, text="后退",command=lambda: self.turn_back(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        stop=Button(ctrlf, text="停止",command=lambda: self.car_stop(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)

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
    car = CarControl()
    car.LF_Motor.start(car.speed)
    car.LB_Motor.start(car.speed)
    car.RF_Motor.start(car.speed)
    car.RB_Motor.start(car.speed)
    try:
        car.ConInterface()
    except KeyboardInterrupt:
        GPIO.cleanup()
