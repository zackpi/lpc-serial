from lpc import Device

if __name__ == "__main__":
  with Device("/dev/ttyUSB0", 9600, 50000) as uc:
    print(uc.read_uid())
    code = str(23130).encode('UTF-8')
    uc.serial.write(b"U " + code + uc.eol)
    print(uc.serial.readline())
    #uc.unlock()
    #uc.write_to_ram()
