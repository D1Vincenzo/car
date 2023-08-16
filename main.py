import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

pwm = GPIO.PWM(2, 80)
pwm.start(90)
GPIO.output(3, True)
GPIO.output(4, False)

def cleanup():
    pwm.stop()
    GPIO.cleanup()