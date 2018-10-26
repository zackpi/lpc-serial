from serial import Serial

class Device:

    def __init__(self, serial, baud, khz):
        self.serial = Serial(serial, baud)
        self.clock = khz
        self.eol = b"\r\n"
        
    def __enter__(self):
        self.sync()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def check_blank(self):
        pass

    def close(self):
        self.serial.close()

    def compare(serial):
        pass

    def echo(self):
        pass

    def erase(self):
        pass

    def exec(self):
        pass

    def prepare_write(self):
        pass    

    def readline(self):
        raw = self.serial.readline()
        line = raw.decode()
        line = "".join(line.split(self.eol)[:-1])
        return line

    def read_boo_code_version(serial):
        pass

    def read_memory(self):
        pass

    def read_part_id(self):
        pass

    def read_uid(self):
        pass

    def set_baud_rate(self):
        pass

    def sync(self):
        self.serial.write(b"?") #does not have eol attached to it

        if self.readline() == "Synchronized":
            self.write_command("Synchronized")
        else:
            raise Exception("no response from device")
        
        if self.readline() == "Synchronized\rOK":
            self.write_command(self.clock)
        else:
            raise Exception("synchronized failed")

        if self.readline() == f"{self.clock}\rOK":
            raise Exception("Failed to set clock frequency")
        
    def unlock(self):
        pass

    def write_command(self, data):
        eol_data = f"{data}{self.eol}"
        serial.write(eol_data.encode("UTF-8"))
    
    def write_to_flash(self):
        pass

    def write_to_ram(self):
        pass
