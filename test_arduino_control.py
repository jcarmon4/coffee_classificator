from arduino_control import ArduinoControl
import sys
from time import sleep


arduino_control = ArduinoControl()
arduino_control.establish_arduino_connection()

while True:
    try:
        response = arduino_control.write_to_arduino('l')
        print(response)
        sleep(1)
        response = arduino_control.write_to_arduino('r')
        print(response)
        sleep(1)
    except:
        sys.exit(1)