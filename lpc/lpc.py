from serial import Serial
from lpc.enums import ReturnCode

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
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def close(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        self.serial.close()

    def compare(serial):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def echo(self, on):
        '''
        whether ISP command handler sends the received serial data back to host

        Args:
            on (bool): whether echo is set to on or off

        Raises:
            <Some exception if not successful>        
        '''
        #page number: 426
        pass

    def erase(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def exec(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def prepare_write(self, start, end):
        '''
        must be executed before copying ram to flash or erasing sectors; the boot block cannot
        be prepared by this command; to prepare a single sector use the same start and end sector
        numbers
 
        Args:
            start (int): starting sector number
            end (int): ending sector number (end >= start)
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 428
        pass    

    def readline(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2

        Returns:
            (string): the line that was read
    
        Raises:
            <Some exception if not successful>
        '''
        raw = self.serial.readline()
        line = raw.decode()
        line = "".join(line.split(self.eol)[:-1])
        return line

    def read_boo_code_version(serial):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def read_memory(self):
        '''
        reads data from RAM or flash memory. This command is blocked when code read protection
        is enabled
 
        Args:
            start_address (int): address from where data bytes are to be read, this address
                should be a word boundary
            number_of_bytes (int): number of bytes to be read, count should be a multiple of 4
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 428
        pass

    def read_part_id(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def read_uid(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def set_baud_rate(self, baud_rate, stop_bit):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        #page number: 426
        pass

    def sync(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
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
        '''
        command used to unlock flash write, erase and go commands

        Raises:
            <Some exception if not successful>
        '''
        #page number 426
        pass

    def write_command(self, data):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        eol_data = f"{data}{self.eol}"
        serial.write(eol_data.encode("UTF-8"))
    
    def write_to_flash(self):
        '''
        command used to change baud rate
 
        Args:
            baud_rate (int): bits per second rounded down 9600, 19200, 38400, 57600, 115200
            stop_bit (int): number of special bits at end of data can be 1 or 2
    
        Raises:
            <Some exception if not successful>
        '''
        pass

    def write_to_ram(self):
        '''
        downloads data to Ram. Data should be in UU-encoded format. This command is blocked 
        when code read protection is enabled.
        
 
        Args:
            start_address (int): RAM address where data bytes are to  written. This address
                should be a word boundary
            number_of_bytes (int): number of bytes to be written, count should be a multiple of 4
    
        Raises:
            <Some exception if not successful>
        '''
        # Page Number: 427
        pass
