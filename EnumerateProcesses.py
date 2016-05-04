from winappdbg import System # Create a system snaphot.
system = System()
# Now we can enumerate the running processes.
for process in system:
  print "%d:\t%s" % ( process.get_pid(), process.get_filename() )
