import RPi.GPIO as GPIO
import time

class SpeedDetector:
    def __init__(self, pin):
        self.SENSOR_PIN = pin
        self.last_time = None
        GPIO.setup(self.SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.SENSOR_PIN, GPIO.FALLING, callback=self.sensor_callback, bouncetime=100)

    def sensor_callback(self, channel):
        if self.last_time is None:
            self.last_time = time.time()
            return

        time_elapsed = time.time() - self.last_time
        speed = 1 / time_elapsed  # assuming each detection represents one unit of distance
        print(f"Speed: {speed:.2f} units per second")
        
        self.last_time = time.time()

def main():
    GPIO.setmode(GPIO.BOARD)
    detector = SpeedDetector(pin=7)

    try:
        while True:
            time.sleep(1)  # main loop can do other work or simply wait
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
