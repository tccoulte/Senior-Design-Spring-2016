#!/usr/bin/env python
import time
import os
from collections import Counter
from Transmit_Receive_Blocks import Top_Block_Senior_Design
from Timeout import Timeout,TimeoutError
from global_types import class_state,phone_state,station_state
import logging
import math



class Senior_Design:
    def __init__(self, file_sink, file_source, SNR_threshold):
        self.GNU_Radio_Block = Top_Block_Senior_Design(file_source_t = file_source, 
                                file_sink_t = file_sink)
        self.read_file = file_sink
        self.SNR_threshold = SNR_threshold
        self.state_message = class_state.IDLE
        self.amplitude = 1
        self.current_message = ''

    def run(self):
        """Starts the program. Call this after initial variables have been set up"""
        self.GNU_Radio_Block.start()
        logging.info("---------------------------")
        logging.info("New Application Started")
        logging.info("---------------------------")
    
    def send_message(self, message,repetition):
        """Sends new message with specified repetition"""
        self.GNU_Radio_Block.send_new_packet(message,repetition)
        self.set_state(class_state.TRANSMITTED)
        time.sleep(.3)
        logging.info("Message Sent: " + message + "  Amplitude: " + str(self.get_amplitude()))

    def receive_message(self,time_out,message = ''):
        try:
            with Timeout(time_out):
                self.GNU_Radio_Block.set_transmit(False)
                self.GNU_Radio_Block.clear_file_sink()
                self.poll_SNR(self.SNR_threshold)
                logging.info("SNR Threshold met")
                logging.info ("SNR Treshold: " + str(self.get_SNR_threshold()))
                time.sleep(.3)
                if self.verify_transmission(message):
                    self.set_state(class_state.RECEIVED)
                else:
                    self.set_state(class_state.NOT_RECEIVED)
        except TimeoutError:
            logging.error("Timeout! Message could not be received")
            self.set_state(class_state.TIMEOUT)

    def set_state(self,state):
        self.state_message = state

    def get_state(self):
        return self.state_message

    def poll_SNR(self,threshold):
        """polls SNR every certain number of seconds. NEEDS TO BE PAIRED
        WITH TIMEOUT!!! It will run until it sees high SNR
        """
        snr_list = list()
        snrMaxlist = []
        high_SNR_bool = False
        while high_SNR_bool is False: 
            snr = self.GNU_Radio_Block.SNR()
            if not math.isnan(float(snr)):
                snr_list.append(snr)
            if snr >= threshold:
                high_SNR_bool = True
            if len(snr_list) is 100:
                print max(snr_list)
                snr_list = []
            

    def verify_transmission(self,message):
        file_obj = open(self.read_file)
        lines =file_obj.read().splitlines()
        file_obj.close()
        if  not lines:
            logging.warning("File was empty")
            return False
        message_tuple = ((Counter(lines)).most_common(1))[0]
        if message_tuple[1] > 4:
            if message == '':
                self.current_message = message_tuple[0]
                logging.info("Message Received")
                logging.info("Message_Tuple: " + str(message_tuple))
                return True
            elif message_tuple[0] == message:
                self.current_message = message_tuple[0]
                logging.info("Message Received")
                logging.info("Message_Tuple: " + str(message_tuple))
                return True
        logging.warning("Message Not Properly")
        logging.info("Message_Tuple: " + str(message_tuple)) 
        return False
        
    def set_amplitude(self,amplitude):
        logging.info("Amplitude has been set to: " + str(amplitude))
        self.amplitude = amplitude
        self.GNU_Radio_Block.set_ampl_tx(amplitude,True)

    def get_amplitude(self):
        return self.GNU_Radio_Block.get_ampl()

    def set_SNR_threshold(self, threshold):
        self.SNR_threshold = threshold;

    def get_SNR_threshold(self):
        return self.SNR_threshold

    def get_message(self):
        return self.current_message




