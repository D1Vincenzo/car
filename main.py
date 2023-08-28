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
        # Set the duty cycle of the PWM to the given value
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        # Wait for the given time
        time.sleep(t_time)

    def turn_left(self, t_time):
        # Set the duty cycle of the PWM to the given value
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,False)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3,GPIO.HIGH)
        GPIO.output(self.IN4,GPIO.LOW)
        # Wait for the given time
        time.sleep(t_time)

    def turn_right(self, t_time):
        # Set the duty cycle of the PWM to the given value
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1,GPIO.HIGH)
        GPIO.output(self.IN2,GPIO.LOW)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,False)
        # Wait for the given time
        time.sleep(t_time)

    def car_stop(self):
        # Set the duty cycle of the PWM to 0
        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)

        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)
    
    def ConInterface(self):
        # Create a Tkinter window, set the title, size and bg color
        root = Tk()
        root.title("Control")
        root.geometry("800x600")
        root['bg'] = "#333333"
        # Make the window not resizable
        root.resizable(width=False, height=False)

        # Create the frame for the video, controller and side
        videof = Frame(root, height=360, width=675, cursor="cross")
        ctrlf = Frame(root, height=270, width=540, cursor="circle", bg="#333333")
        sidef = Frame(root, height=180, width=540, cursor="plus", bg="#333333")

        # Place the frame in the window
        videof.place(x=199, y=0)
        ctrlf.place(x=269, y=359)
        sidef.place(x=269, y=629)

        # Create a speed slider and set the speed of it
        speed_slider = Scale(sidef, from_=50, to=100, orient=HORIZONTAL, label="Speed", command=self.set_speed)
        speed_slider.set(self.speed)

        # Create buttons
        up = Button(ctrlf, text="前进", command=lambda: self.turn_up(0.5), activeforeground="green", activebackground="yellow", height=1, width=4)
        left=Button(ctrlf,text="左转",command=lambda: self.turn_left(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        right=Button(ctrlf,text="右转",command=lambda: self.turn_right(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        back=Button(ctrlf,text="后退",command=lambda: self.turn_back(0.5), activeforeground="green",activebackground="yellow",height=1,width=4)
        stop=Button(ctrlf,text="停止",command=lambda: self.car_stop, activeforeground="green",activebackground="yellow",height=1,width=4)

        # Place the speed slider and buttons in the frame
        speed_slider.place(x=100, y=5)
        up.place(x=267, y=39)
        left.place(x=132,y=134)
        right.place(x=412,y=134)
        back.place(x=267,y=230)
        stop.place(x=267,y=134)

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
