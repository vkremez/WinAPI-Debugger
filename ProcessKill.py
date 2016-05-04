from winappdbg import Process 
def process_kill( pid ):
    # Instance a Process object.
    process = Process( pid )
    # Kill the process.
    process.kill()
