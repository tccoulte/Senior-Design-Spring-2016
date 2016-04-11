#!/usr/bin/env python

import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design

def increment_tx():
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

def increment_ampl(ampl, amount):
    ample = ampl+amount
    return ampl

def standard_tx():
    tb = Top_Block_Senior_Design(file_source_t = <<INSERT INPUT FILE NAME>>, 
                                file_sink_t = <<INSERT OUTPUT FILE NAME>>, 
                                disconnect_receive = True,
                                enable_initial_transmit = True)

    #### change ampl ##########

    tb.set_ampl = 1 
    
    ###########################

    initial_mesage = "This is a transmit test"
    repetition = 10
    tb.send_new_packet(initial_message, repetition)
    tb.set_repeat(True)
    tb.run()

if __name__ == "__main__":
    #CHOOSE FUNCTION HERE
 