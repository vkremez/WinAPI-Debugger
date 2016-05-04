from winappdbg import Process 
def show_command_line( pid ):
    # Instance a Process object.
  process = Process( pid )
# Print the process command line.
  print process.get_command_line()
    # The same thing could be done with the environment variables.
    #import pprint
    #pprint.pprint( process.get_environment() )
