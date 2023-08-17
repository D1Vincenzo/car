import RPi.GPIO as GPIO
import time
from tkinter import *

class CarControl:
    def __init__(self):
        # Identify GPIO
        self.PWMA = 16
        self.PWMB = 18
        self.IN1 = 11
        self.IN2 = 13
        self.IN3 = 15
        self.IN4 = 12
        self.speed = 50
        self.init_gpio()
        self.L_Motor = GPIO.PWM(self.PWMA, 100)
        self.R_Motor = GPIO.PWM(self.PWMB, 100)

    def init_gpio(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.PWMB, GPIO.OUT)
        pwm = GPIO.PWM(self.PWMA, 1000)
        pwm.start(0)

    def set_speed(self, val):
        self.speed = int(val)

    def turn_up(self, t_time):
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)
        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3, GPIO.HIGH)
        GPIO.output(self.IN4, GPIO.LOW)
        time.sleep(t_time)


    def turn_back(self, t_time):
        self.L_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN1,GPIO.LOW)
        GPIO.output(self.IN2,GPIO.HIGH)

        self.R_Motor.ChangeDutyCycle(self.speed)
        GPIO.output(self.IN3,GPIO.LOW)
        GPIO.output(self.IN4,GPIO.HIGH)
        time.sleep(t_time)

    def turn_left(self, t_time):
        self.L_Motor.ChangeDutyCycle(self.speed)
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

    def car_stop(self):
        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)

        self.L_Motor.ChangeDutyCycle(0)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)
    
    def ConInterface(self):
        root = Tk()
        root.title("Control")
        root.geometry("1080x720")
        root['bg'] = "#333333"
        root.resizable(width=False, height=False)

        videof = Frame(root, height=360, width=675, cursor="cross")
        videof.place(x=199, y=0)

        f1 = Frame(root, height=270, width=540, cursor="circle", bg="#333333")
        f1.place(x=269, y=359)

        f2 = Frame(root, height=180, width=540, cursor="plus", bg="#333333")
        f2.place(x=269, y=629)

        speed_slider = Scale(f2, from_=0, to=100, orient=HORIZONTAL, label="Speed", command=self.set_speed)
        speed_slider.set(self.speed)
        speed_slider.place(x=100, y=5)

        up = Button(f1, text="前进", command=lambda: self.turn_up(1), activeforeground="green", activebackground="yellow", height=1, width=4)
        up.place(x=267, y=39)

        left=Button(f1,text="左转",command=lambda: self.turn_left(1), activeforeground="green",activebackground="yellow",height=1,width=4)
        left.place(x=132,y=134)

        right=Button(f1,text="右转",command=lambda: self.turn_right(1), activeforeground="green",activebackground="yellow",height=1,width=4)
        right.place(x=412,y=134)

        back=Button(f1,text="后退",command=lambda: self.turn_back(1), activeforeground="green",activebackground="yellow",height=1,width=4)
        back.place(x=267,y=230)

        stop=Button(f1,text="停止",command=self.car_stop, activeforeground="green",activebackground="yellow",height=1,width=4)
        stop.place(x=267,y=134)

        root.mainloop()

if __name__ == "__main__":
    car = CarControl()
    car.L_Motor.start(car.speed)
    car.R_Motor.start(car.speed)

    try:
        car.ConInterface()

    except KeyboardInterrupt:
        GPIO.cleanup()
