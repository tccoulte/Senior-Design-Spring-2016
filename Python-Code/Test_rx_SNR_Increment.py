#!/usr/bin/env python

import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design

def main():
    tb = Top_Block_Senior_Design(file_source_t = <<INSERT INPUT FILE NAME>>, 
                                file_sink_t = <<INSERT OUTPUT FILE NAME>>, 
                                disconnect_transmit = True)
    tb.start()
    snr_list = list()
    threshold = 4
    found_SNR_above_thresh = False
    while True:
        snr = tb.SNR()
        snr_list.append(snr)
        if snr > threshold and found_SNR_above_thresh is False:
            print 'Greater than threshold'
            snr_list = snr_list[-1]
            found_SNR_above_thresh = True
        if len(snr_list) is 100:
            if found_SNR_above_thresh is True:
                found_SNR_above_thresh = False
                time.sleep(.05)
                tb.close_file_sink()
                print 'SNR average for above threshold + 100 values'
                print sum(snr_list)/len(snr_list)
                sys.exit("Received Message -- code will now exit")
            print sum(snr_list)/len(snr_list)
            snr_list = []
    tb.Wait()

# END MAIN

if __name__ == "__main__":
    main()
