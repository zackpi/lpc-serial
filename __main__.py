from lpc import Device

if __name__ == "__main__":
  with Device("/dev/ttyUSB0", 9600, 50000) as uc:
    print(uc.read_uid())
    uc.write_to_ram(Device.RAM_BEGIN, b"test")
