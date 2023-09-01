import RPi.GPIO as GPIO
import time

# 设置GPIO模式
GPIO.setmode(GPIO.BOARD)

# 定义光电传感器连接的GPIO引脚
SENSOR_PIN = 7

# 设置引脚为输入，并启用上拉电阻（假设传感器在检测到标记时输出高电平）
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_time = None

def sensor_callback(channel):
    global last_time
    if last_time is None:
        last_time = time.time()
        return

    # 计算两次回调之间的时间差
    time_elapsed = time.time() - last_time

    # 假设每次标记通过时我们测量1单位的距离，根据实际情况调整
    speed = 1 / time_elapsed  # 速度 = 距离 / 时间
    print(f"Speed: {speed:.2f} units per second")

    last_time = time.time()

# 设置事件检测
GPIO.add_event_detect(SENSOR_PIN, GPIO.FALLING, callback=sensor_callback, bouncetime=100)

try:
    while True:
        time.sleep(1)  # 主循环可以做其他的工作或仅仅等待

except KeyboardInterrupt:
    GPIO.cleanup()