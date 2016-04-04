import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design

def main():
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
# END MAIN

if __name__ == "__main__":
    main()

