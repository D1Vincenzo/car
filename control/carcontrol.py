import RPi.GPIO as GPIO
import time
from tkinter import *

class CarControl:
    # Initialize GPIO
    def __init__(self):
        # Identify GPIO
        self.PWMA = 16
        self.PWMB = 18
        # 左前轮,HIGHLOW前转
        self.IN1 = 15
        self.IN2 = 12
        # 左后轮,LOWHIGH前转
        self.IN3 = 11
        self.IN4 = 13
        
        # Define GPIO for right wheels
        self.PWMC = 37  
        self.PWMD = 31
        # 右前轮,HIGHLOW前转
        self.IN5 = 35
        self.IN6 = 33
        # 右后轮,LOWHIGH前转
        self.IN7 = 36
        self.IN8 = 38
        
        self.speed = 100
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

    def motor_forward(self, motor, speed):
        if motor == 'LF':
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
            self.LF_Motor.ChangeDutyCycle(speed)
        elif motor == 'LB':
            GPIO.output(self.IN3, GPIO.LOW)
            GPIO.output(self.IN4, GPIO.HIGH)
            self.LB_Motor.ChangeDutyCycle(speed)
        elif motor == 'RF':
            GPIO.output(self.IN5, GPIO.HIGH)
            GPIO.output(self.IN6, GPIO.LOW)
            self.RF_Motor.ChangeDutyCycle(speed)
        elif motor == 'RB':
            GPIO.output(self.IN7, GPIO.LOW)
            GPIO.output(self.IN8, GPIO.HIGH)
            self.RB_Motor.ChangeDutyCycle(speed)

    def motor_backward(self, motor, speed):
        if motor == 'LF':
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
            self.LF_Motor.ChangeDutyCycle(speed)
        elif motor == 'LB':
            GPIO.output(self.IN3, GPIO.HIGH)
            GPIO.output(self.IN4, GPIO.LOW)
            self.LB_Motor.ChangeDutyCycle(speed)
        elif motor == 'RF':
            GPIO.output(self.IN5, GPIO.LOW)
            GPIO.output(self.IN6, GPIO.HIGH)
            self.RF_Motor.ChangeDutyCycle(speed)
        elif motor == 'RB':
            GPIO.output(self.IN7, GPIO.HIGH)
            GPIO.output(self.IN8, GPIO.LOW)
            self.RB_Motor.ChangeDutyCycle(speed)

    # Movement methods using the helper functions
    def move_forward(self):
        self.motor_forward('LF', self.speed)
        self.motor_forward('LB', self.speed)
        self.motor_forward('RF', self.speed)
        self.motor_forward('RB', self.speed)

    def move_backward(self):
        self.motor_backward('LF', self.speed)
        self.motor_backward('LB', self.speed)
        self.motor_backward('RF', self.speed)
        self.motor_backward('RB', self.speed)

    def turn_left(self):
        self.motor_backward('LF', self.speed)
        self.motor_backward('LB', self.speed)
        self.motor_forward('RF', self.speed)
        self.motor_forward('RB', self.speed)

    def turn_right(self):
        self.motor_forward('LF', self.speed)
        self.motor_forward('LB', self.speed)
        self.motor_backward('RF', self.speed)
        self.motor_backward('RB', self.speed)


    def shift_left(self):
        self.motor_backward('LF', self.speed)
        self.motor_forward('LB', self.speed)
        self.motor_forward('RF', self.speed)
        self.motor_backward('RB', self.speed)
        
    
    def shift_right(self):
        self.motor_forward('LF', self.speed)
        self.motor_backward('LB', self.speed)
        self.motor_backward('RF', self.speed)
        self.motor_forward('RB', self.speed)
        
        


    def car_stop(self):
        self.LF_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)

        self.LB_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)

        self.RF_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN5, False)
        GPIO.output(self.IN6, False)

        self.RB_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN7, False)
        GPIO.output(self.IN8, False)