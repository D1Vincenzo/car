from control.carcontrol import CarControl
import os
import sys
import time
import RPi.GPIO as GPIO

def main_control_loop(car):
    print("Control your car!")
    print("w: Forward, s: Backward, a: Left, d: Right, e:Stop, q: Quit")

    while True:
        os.system('stty raw')
        command = sys.stdin.read(1)
        os.system('stty sane')

        if command == 'w':
            car.move_forward()
            time.sleep(1)
            car.car_stop()

        elif command == 's':
            car.move_backward()
            time.sleep(1)
            car.car_stop()

        elif command == 'a':
            car.turn_left()
            time.sleep(0.4)
            car.car_stop()

        elif command == 'd':
            car.turn_right()
            time.sleep(0.4)
            car.car_stop()

        elif command == 'e':
            car.car_stop()

        elif command == 'z':
            car.shift_left()
            time.sleep(1)
            car.car_stop()
            
        elif command == 'c':
            car.shift_right()
            time.sleep(1)
            car.car_stop()
        
        elif command == 'q':
            print("\nExiting...")
            car.car_stop()
            break
        
        else:
            print("Invalid command!")

if __name__ == "__main__":
    car = CarControl()
    car.LF_Motor.start(car.speed)
    car.LB_Motor.start(car.speed)
    car.RF_Motor.start(car.speed)
    car.RB_Motor.start(car.speed)
    '''
    car.turn_left()
    time.sleep(0.5)
    car.turn_right()
    time.sleep(0.5)
    car.car_stop()
    '''
    main_control_loop(car)

    GPIO.cleanup()