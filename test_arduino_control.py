from arduino_control import ArduinoControl
import sys


arduino_control = ArduinoControl()
arduino_control.establish_arduino_connection()

while True:
    try:
        response = arduino_control.write_to_arduino('l')
        print(response)
    except:
        sys.exit(1)