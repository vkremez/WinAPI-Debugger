from winappdbg import Process, HexDump 

def print_threads_and_modules( pid ):
    # Instance a Process object.
  process = Process( pid )
  print "Process %d" % process.get_pid()
    # Now we can enumerate the threads in the process...
  print "Threads:"
  for thread in process.iter_threads():
    print "\t%d" % thread.get_tid()
    # ...and the modules in the process.
  print "Modules:"
  bits = process.get_bits()
  for module in process.iter_modules():
    print "\t%s\t%s" % (
       HexDump.address( module.get_base(), bits ), module.get_filename()
    )
