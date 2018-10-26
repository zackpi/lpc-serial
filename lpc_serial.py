import serial as ser


###############
# DEBUG TOOLS #

EOL = b"\r\n"

def debug_log(s, verbose=False):
  if verbose:
    print(s)


###################
# PORT MANAGEMENT #

def open_port(serial, baud):
  debug_log(f"Serial communication opened on port {serial} at {baud} baud.", True)
  return ser.Serial(serial, baud, timeout=1)

def sync_port(serial, khz, verbose=False):

  serial.write(b"?")
  debug_log("synchronization handshake initiated... ", verbose)

  if serial.readline() == b"Synchronized" + EOL:
    serial.write(b"Synchronized" + EOL)
  else:
    debug_log("Synchronization failed. No response from target device.", verbose)
    return False

  clk = str(khz).encode('UTF-8')   
  if serial.readline() == b"Synchronized\rOK" + EOL:
    debug_log("Synchronized with target device.", verbose)
    debug_log("Setting device clock freq... ", verbose)

    serial.write(clk + EOL)
  else:
     
    debug_log("Synchronization failed. Target aborted synchronization.", verbose)
    return False

  if serial.readline() == clk + b"\rOK" + EOL:
    debug_log("Clock frequency set at %.3f Mhz" % (khz / 1000.0), verbose)
  else:
    debug_log("Failed to set clock frequency to %.3f Mhz" % (khz / 1000.0), verbose)
    return False
  
  debug_log("Communications setup with target device succeeded.", verbose)
  return True

def close_port(serial):
  serial.close()


#####################
# UART ISP COMMANDS #

def unlock(serial):
  serial.write(b"U\r\n")
  # CHECK THAT IT WORKED

def set_baud_rate(serial):
  pass

def echo(serial):
  pass

def write_to_ram(serial):
  pass

def read_memory(serial):
  pass

def prepare_write(serial):
  #prepare secotrs for write operation boi thats a mouth full
  pass

def write_to_flash(serial):
  pass

def exec(serial):
  pass

def erase(serial):
  pass

def check_blank(serial):
  pass

def read_part_id(serial):
  pass

def read_boo_code_version(serial):
  pass

def compare(serial):
  pass

def read_uid(serial):
  pass


if __name__=="__main__":
  port = open_port("/dev/ttyUSB0", 9600)
  sync_port(port, 50000, verbose=True)
  close_port(port)

