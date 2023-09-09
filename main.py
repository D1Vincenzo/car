from control.carcontrol import CarControl
from control.GUI_control import ConInterface
from control.keyboard_control import main_control_loop
import RPi.GPIO as GPIO

method = input("Enter the name of the controller, GUI(1) or Keyboard(2): ")
car = CarControl()
car.LF_Motor.start(car.speed)
car.LB_Motor.start(car.speed)
car.RF_Motor.start(car.speed)
car.RB_Motor.start(car.speed)

if method == "1":
    try:
        ConInterface(car)

    except KeyboardInterrupt:
        pass

elif method == "2":
    main_control_loop(car)

else:
    print("Invalid input")

GPIO.cleanup()