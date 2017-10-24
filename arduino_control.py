from time import sleep
import serial

class ArduinoControl:
    ARDUINO_PORT = "/dev/ttyACM0"
    #ARDUINO_PORT = "COM8"
    RATE = 9600

    def __init__(self):
        self.arduino = serial.Serial(self.ARDUINO_PORT, self.RATE)

    # Establishes the connection between Arduino and Python before starting the processing.
    def establish_arduino_connection(self):
        # self.arduino.readline()
        print("Arduino connection established.")

    # Sends the given parameter to Arduino and returns it response.
    def write_to_arduino(self, param):
        self.arduino.write(param.encode())
        sleep(0.1)
        arduino_respone = self.arduino.readline()
        return arduino_respone.rstrip().decode()