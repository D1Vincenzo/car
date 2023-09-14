from flask import Flask, render_template, request, Response
from carcontrol import CarControl
import RPi.GPIO as GPIO
import picamera
import io


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

def generate():
    with picamera.PiCamera(resolution='640x480', framerate=60) as camera:
        camera.rotation = 180  # Adjust this if your video is upside down
        camera.resolution = (320, 240)
        camera.vflip = True
        camera.hflip = True
        while True:
            output = io.BytesIO()
            camera.capture(output, format='jpeg')
            frame = output.getvalue()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            output.flush()

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    car.LF_Motor.start(car.speed)
    car.LB_Motor.start(car.speed)
    car.RF_Motor.start(car.speed)
    car.RB_Motor.start(car.speed)
    app.run(host='0.0.0.0', port=5000)

    GPIO.cleanup()
