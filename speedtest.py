import RPi.GPIO as GPIO
import time

# 定义SpeedDetector类，接收pin参数
class SpeedDetector:
    def __init__(self, pin):
        # 将pin设置为GPIO的输入模式
        self.SENSOR_PIN = pin
        self.last_time = None
        GPIO.setup(self.SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # 当pin输入模式为FALLING时，设置GPIO的输入触发条件为bouncetime=100
        GPIO.add_event_detect(self.SENSOR_PIN, GPIO.FALLING, callback=self.sensor_callback, bouncetime=100)

    # 定义sensor_callback函数，当pin输入模式为FALLING时，调用SpeedDetector类的sensor_callback函数
    def sensor_callback(self, channel):
        # 如果last_time为None，则记录当前时间
        if self.last_time is None:
            self.last_time = time.time()
            return

        # 计算当前时间与上一次记录的时间的时间差
        time_elapsed = time.time() - self.last_time
        # 计算速度，单位为千米每秒
        speed = 1 / time_elapsed  # assuming each detection represents one unit of distance
        print(f"Speed: {speed:.2f} units per second")
        
        # 将last_time记录下来
        self.last_time = time.time()

# 定义main函数
def main():
    # 设置GPIO的模式为BOARD
    GPIO.setmode(GPIO.BOARD)
    # 实例化SpeedDetector类，接收pin参数
    detector = SpeedDetector(pin=7)

    try:
        # 循环执行
        while True:
            time.sleep(1)  # main loop can do other work or simply wait
    except KeyboardInterrupt:
        # 清除GPIO的输入模式
        GPIO.cleanup()

if __name__ == "__main__":
    main()