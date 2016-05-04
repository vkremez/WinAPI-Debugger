from winappdbg import System, version
# Show the Windows version and the current architecture.
print "WinAppDbg %s" % version
print "Running on %s for the %s architecture." % (System.os, System.arch) if System.wow64:
print "Running in 32 bit emulation mode."
print "From this Python VM we can attach to %d-bit processes." % System.bits
