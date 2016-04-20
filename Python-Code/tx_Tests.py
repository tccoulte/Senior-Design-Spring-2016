#!/usr/bin/env python

import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design

################################################################
# ---------------------SIMPLE TESTS---------------------------- 
################################################################

#////////// Packet Sending Tests /////////////////////

#Increments ampl by certain amount every 5 miliseconds until the amplitude is 1


def increment_tx():
    tb = Top_Block_Senior_Design(file_source_t = "file_source", 
                                file_sink_t = "file_sink", 
                                disconnect_receive = True,
                                enable_initial_transmit = True)
    initial_message = "This should be Received Clearly"
    tb.set_ampl_tx(.1,True)
    tb.send_new_packet(initial_message, 10)
    tb.start()
    time.sleep(.05)
    while tb.get_ampl <= 1:
        tb.set_ampl_tx(increment_ampl(tb.get_ample,.02),True)
        tb.send_new_packet(initial_message, 10)
        time.sleep(.05)
    sys.exit("Loop Ended.... Hopefully Something Received")

def increment_ampl(ampl, amount):
    ample = ampl+amount
    return ampl

#Send a Packet every 10 miliseconds

def continous_packet_send():
    tb = Top_Block_Senior_Design(file_source_t = "file_source", 
                                file_sink_t = "file_sink", 
                                disconnect_receive = True,
                                enable_initial_transmit = True)
    message = "This is the packet"
    
    ####### Set Amplitude ############ 
    amplitude = 1
    ##################################
    
    tb.set_ampl_tx(amplitude,True)
    tb.send_new_packet(message, 10)
    tb.start()
    while True:
        tb.send_new_packet(message, 10)
        time.sleep(.01)


#Test for being able to send multiple packets. Receiver should get two different messages

def packet_send_test():
    tb = Top_Block_Senior_Design(file_source_t = "file_source", 
                                file_sink_t = "file_sink", 
                                disconnect_receive = True,
                                enable_initial_transmit = True)
    old_message = "Hello I am Tim"
    new_message = "This is a different message"
    tb.set_ampl_tx(1,True)
    tb.start()
    time.sleep(.2)
    tb.send_new_packet(old_message, 5)
    time.sleep(1)
    tb.stop()
    sys.exit("Both Packets Sent...")


#Standard repeating transmitter. Sends packets with repetition of 10.

def standard_tx():
    tb = Top_Block_Senior_Design(file_source_t = "file_source", 
                                file_sink_t = "file_sink", 
                                disconnect_receive = True,
                                enable_initial_transmit = True)

    #### change ampl ##########

    tb.set_ampl_tx(1)
    
    ###########################

    initial_message = "This is a transmit test" + "\n"
    repetition = 1
    tb.send_new_packet(initial_message, repetition, True)
    tb.start()
    time.sleep(2)
    sys.exit('End of program...')




#////////// Top Block Function Tests /////////////////////


#Tests flowgraph locking before running

def lock_test():
    tb = Top_Block_Senior_Design(file_source_t = "file_source", 
                                file_sink_t = "file_sink", 
                                disconnect_receive = True,
                                enable_initial_transmit = True)
    #lock and unlock flowgraph before running to see if there is a problem...
    tb.lock_tx()
    tb.unlock_tx()
    tb.start()
    sys.exit("No Problem Locking")

#See if file is written to

def write_to_file_test():
    tb = Top_Block_Senior_Design(file_source_t = "file_source", 
                                file_sink_t = "file_sink", 
                                disconnect_receive = True,
                                enable_initial_transmit = True)
    tb.write_new_data_to_file("Testing Writting...",5)
    sys.exit("Go Look at File")



################################################################
# ---------------------ADVAMCED TESTS---------------------------- 
################################################################




if __name__ == "__main__":
    standard_tx()