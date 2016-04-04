#!/usr/bin/env python

import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design

def main():
    tb = Top_Block_Senior_Design(file_source_t = <<INSERT INPUT FILE NAME>>, 
                                file_sink_t = <<INSERT OUTPUT FILE NAME>>, 
                                disconnect_recieve = True
                                enable_initial_transmit = True)
    initial_message = "This should be Received Clearly"
    tb.set_ampl_tx(.1)
    tb.send_new_packet(initial_message, 10)
    tb.start()
    time.sleep(.03)
    while tb.get_ampl <= 1:
        tb.set_ampl_tx(increment_ampl(tb.get_ample,.02),True)
        tb.send_new_packet(initial_message, 10)
        time.sleep(.03)
    sys.exit("Loop Ended.... Hopefully Something Received")
# END MAIN

def increment_ampl(ampl, amount):
    ample = ampl+amount
    return ampl

if __name__ == "__main__":
    main()

 