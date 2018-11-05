from lpc import Device


if __name__ == "__main__":
    microcontroller = Device("/dev/ttyUSB0", 9600, 50000)
    microcontroller.sync()
    print("hello world")
