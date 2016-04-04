import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design

def main():
    tb = Top_Block_Senior_Design(file_source_t = "file_source", 
                                file_sink_t = "file_sink, 
                                disconnect_transmit = True)
    tb.start()
    snr_list = list()
    
    # Measure SNR
    while True:
        snr = tb.SNR() 
        snr_list.append(snr)
        if len(snr_list) is 100:
            print 'Avergage snr is: %f' % snr 
            snr_list = []
        time.sleep(.005)


# END MAIN

if __name__ == "__main__":
    main_1()
