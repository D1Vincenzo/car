from flask import Flask, render_template, request
from carcontrol import CarControl
import RPi.GPIO as GPIO


app = Flask(__name__)
car = CarControl()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control/<direction>', methods=['POST'])
def control(direction):
    if direction == 'up':
        car.turn_up()
    elif direction == 'down':
        car.turn_back()
    elif direction == 'left':
        car.turn_left()
    elif direction == 'right':
        car.turn_right()
    elif direction == 'stop':
        car.car_stop()
    return '', 204

if __name__ == '__main__':
    car.LF_Motor.start(car.speed)
    car.LB_Motor.start(car.speed)
    car.RF_Motor.start(car.speed)
    car.RB_Motor.start(car.speed)
    app.run(host='0.0.0.0', port=5000)

    GPIO.cleanup()
