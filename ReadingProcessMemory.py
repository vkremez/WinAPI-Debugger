from winappdbg import Process
def process_read( pid, address, length ):
    # Instance a Process object.
process = Process( pid )
# Read the process memory.
data = process.read( address, length )
# You can also change the process memory.
    # process.write( address, "example data" )
    # Return a Python string with the memory contents.
return data
