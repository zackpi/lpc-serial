from serial import Serial
from lpc.enums import ReturnCode
from codecs import encode, decode

class Device:

  EXEC_MODES = ["T"]
  RAM_BEGIN = 268435456 
  RESET_PRGM = b'\x01H\x02I\x01`\xfe\xe7\x0c\xed\x00\xe0\x04\x00\xfa\x05'

  def __init__(self, serial, baud, khz):
    self.serial = Serial(serial, baud, timeout=1)
    self.baud = baud
    self.khz = khz
    self.eol = b"\r\n"
    
  def __enter__(self):
    self.sync()
    self.echo(False)
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()

  def check_blank(self):
    '''
    check if one or more sectors of on-chip flash memory are blank; blank check on sector 0
    always fails as first 64 bytes are re-mapped to flash boot block; when crp is enabled, the
    blank check command returns 0 for the offset and value of sectors which are not blank; blank
    sectors are correct reported irrespective of crp settings

    Args:
      start (int): the starting sector number
      end (int): the ending sector number (start <= end)
  
    Raises:
      <Some exception if not successful>
    '''
    #page number 431
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

  def compare(address_1, address_2, size):
    '''
    compares the memory contents of two locations

    Args:
      address_1 (int): starting flash or ram address of data bytes to be compared.
        should be a word boundary
      address_2 (int): starting flash or ram address of data bytes to be compared. this
        address should be a word boundary
      size (int): number of bytes to be compared; should be a multiple of 4
  
    Raises:
      <Some exception if not successful>
    '''
    #page number: 433
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

    if (on and self.echo) or (not on and not self.echo):
      return

    do_echo = b"1" if on else b"0"
    cmd = b"A " + do_echo
    self.serial.write(cmd + self.eol)

    sol = cmd + b"\r" if self.echo else b"" 
    assert self.serial.readline() == sol + b"0" + self.eol, "Failed to change echo settings."
    self.echo = not self.echo

  def erase(self):
    '''
    erases one or more sectors of on-chip flash memory; the boot block can not be erased using
    this command; this command only allows erasure of all user sectors when code read protection
    is enabled

    Args:
      start (int): the start sector number
      end (int): the end sector number (end >= start)
  
    Raises:
      <Some exception if not successful>
    '''
    #page number: 430
    pass

  def exec(self, address, mode="T"):
    '''
    aka go; executes a program residing in ram or flash memory; it may not be possible to
    return to the isp command handler once this command is successfully executed; this command
    is blocked when code read protection is enabled; this command must be used with an address
    of 0x0000 0200 or greater.

    Args:
      address (int): flash or ram address from which the code execution is to be started; this
       address should be on a word boundary
      mode (int): execute program in thumb mode (tf does that mean???)
  
    Raises:
      ValueError: on invalid input parameters
    '''
    #page number 430
    
    if address < 512:
      raise ValueError("Can not execute from address %s." % hex(address))
    if mode not in Device.EXEC_MODES:
      raise ValueError("Requested execution mode '%s' is not valid." % mode)

    self.write_command("G {address} {mode}")
    # after this command, the LPC will likely no longer be in ISP mode

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

  def read_boot_code_version(serial):
    '''
    reads the boot code version number

    Returns:
      (bytes): the boot code version number

    Raises:
      <Some exception if not successful>
    '''
    #page number: 433
    pass

  def read_memory(self):
    '''
    reads data from RAM or flash memory. This command is blocked when code read protection
    is enabled

    Args:
      start_address (int): address from where data bytes are to be read, this address
        should be a word boundary
      number_of_bytes (int): number of bytes to be read, count should be a multiple of 4

    Returns:
      (bytes): data from memory
  
    Raises:
      <Some exception if not successful>
    '''
    #page number: 428
    

  def read_part_id(self):
    '''
    reads part identification number
  
    Raises:
      <Some exception if not successful>

    Returns:
      (bytes) part identification number
    '''
    #page number: 431
    cmd = b"J"
    self.serial.write(cmd + self.eol)

    sol = cmd + b"\r" if self.echo else b""
    assert self.serial.readline() == sol + b"0" + self.eol, "Unable to read part ID of target device."

    return self.serial.readline() 

  def read_uid(self):
    '''
    reads the unique ID
  
    Raises:
      <Some exception if not successful>

    Returns:
      (bytes) unique id of lpc
    '''
    #page number: 434
    cmd = b"N"
    self.serial.write(cmd + self.eol)

    sol = cmd + b"\r" if self.echo else b""
    assert self.serial.readline() == sol + b"0" + self.eol, "Unable to read UID of target device."

    return self.serial.readline() 

  def reset(self):
    self.serial.write(b"U 23130" + self.eol)
    self.serial.write(b"W " + str(Device.RAM_BEGIN).encode('UTF-8') + b" " + self.eol)
    self.serial.write(b"0`4@\"20%@_N<,[0#@!`#Z!0``" + self.eol)
    self.serial.write(b"1462" + self.eol)
    self.serial.write(b"G " + str(Device.RAM_BEGIN).encode('UTF-8') + b" T" + self.eol)

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

    self.serial.write(b"?")

    assert self.serial.readline() == b"Synchronized" + self.eol, "Synchronization failed. No response from target device."
    self.serial.write(b"Synchronized" + self.eol)

    clk = str(self.khz).encode('UTF-8')   
    assert self.serial.readline() == b"Synchronized\rOK" + self.eol, "Synchronization failed. Target aborted synchronization."
    self.serial.write(clk + self.eol)

    assert self.serial.readline() == clk + b"\rOK" + self.eol, "Failed to set clock frequency to %.3f Mhz" % (self.khz / 1000.0)

  def unlock(self):
    '''
    command used to unlock flash write, erase and go commands

    Raises:
      <Some exception if not successful>
    '''
    #page number 426
    cmd = b"U 23130"
    self.serial.write(cmd + self.eol)

    sol = cmd if self.echo else b""
    ret = self.serial.readline()
    print("unlock", ret)
    assert ret == sol + b"0" + self.eol, "Unable to unlock target device." 

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
    self.serial.write(eol_data.encode("UTF-8"))
  
  def write_to_flash(self):
    '''
    programs flash memory; the prepare_write command should precede this command; the affected
    sectors are automatically protected again once the copy command is successfully executed; 
    the boot block cannot be written by this command; this command is blocked when code read
    protection is enabled; there are limitations specified in the pdf

    Args:
      flash_address (int): destination flash address where data bytes are to be written;
        the destination address should be a 256 byte boundary
      ram_address (int): source ram address from where data bytes are to be read
      number_of_bytes (int): number of bytes to be written 256, 512, 1024, 4096
  
    Raises:
      <Some exception if not successful>
    '''
    #page number 429
    pass

  def write_to_ram(self, address, data):
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
    if address < Device.RAM_BEGIN: # or address + len(bytes) > (limit that depends on device)	
      raise ValueError("Can't write %d bytes to RAM address %s", len(data), hex(address))
    if address % 4 > 0:
      raise ValueError("RAM write address must be at a word line (multiple of 4 bytes)")
    if len(data) % 4 > 0:
      raise ValueError("RAM write data must be a multiple of 4 bytes")

    nbytes = len(data)

    nbytes_str = str(nbytes).encode('UTF-8')
    addr_str = str(address).encode('UTF-8')
    cmd = b"W " + addr_str + b" " + nbytes_str
    self.serial.write(cmd + self.eol)

    sol = cmd + b"\r" if self.echo else b""
    ret = serial.readline()
    print(ret)
    assert ret == sol + "0" + self.eol, "Unable to initiate write to RAM."

    ret = self.readline()
    print("stop: ", ret)
    assert int(ret) == ReturnCode.CMD_SUCCESS, "Return code was not CMD_SUCCESS"

    pointer = 0
    while pointer < len(data):
      checksum = 0
      for byte in data[pointer : min(len(data), pointer+20)]: 
        self.serial.write(byte)
        checksum += byte

      self.serial.write(checksum)
      ret = self.readline()
      assert ret == "OK", "Invalid checksum"

      pointer += 20

    # add in functionality to not clear the <4 bytes at the end
    # if len(data) is not a multiple of 4 

