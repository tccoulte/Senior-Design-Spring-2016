#!/usr/bin/env python
import time
import os
from Transmit_Receive_Blocks import Top_Block_Senior_Design
from extra_functions import enum
from Timeout import Timeout

"""
functions needed:

get_credit_card_number
send_message
    args: message,repetition
receive_message
    args: message,repetition,number_correct,time_out_value

receive_unkown_message
    args: message_length,repetition,nunber_correct,time_out_value
"""



class Phone_Senior_Design:
    def __init__(self, file_sink, file_soure,credit_card_nunber):
        self.GNU_Radio_Block = Top_Block_Senior_Design(file_source_t = file_source, 
                                file_sink_t = file_sink)
        #TODO more class variables
        self.credit_card_nunber = credit_card_nunber
        self.read_file = file_sink
        self.SNR_threshold = <<FIND ME>>
        self.state_enum = enum('TIMEOUT','RECEIVED','TRANSMITTED','KILLED','IDLE','NOT_RECEIVED')
        self.state_message = state_enum.IDLE
        self.amplitude = 0


    def run(self):
        self.GNU_Radio_Block.start()
    
    def send_message(self, message,repetition):
        self.GNU_Radio_Block.send_new_packet(message,repetition)
        self.set_state(self.state_enum.TRANSMITTED)

    def receive_message(self,time_out, message,repetition,number_correct):
        try:
            with Timeout(time_out):
                self.GNU_Radio_Block.set_transmit(false)
                self.GNU_Radio_Block.clear_file_sink()
                self.poll_SNR(self.SNR_threshold)
                if self.verify_transmission(message,repetition,number_correct):
                    self.set_state(self.state_enum.RECEIVED)
                else:
                    self.set_state(self.state_enum.NOT_RECEIVED)
        except TimeoutError:
            self.set_state(self.state_enum.TIMEOUT)
            

    def receive_unkown_message(self, message_length, repetition, number_correct):
        #TODO
        pass

    def set_state(self,state):
        self.state_message = state

    def get_credit_card_number(self):
        return self.credit_card_nunber

    def encrypt_card_number(self,credit_card_number):
        pass
        #Vinny Stuff

    def poll_SNR(self,threshold):
        high_SNR_bool = False
        while high_SNR_bool is False: 
            snr = self.GNU_Radio_Block.SNR()
            if snr >= theshold:
                high_SNR_bool = True
            time.sleep(.0008)


    def verify_transmission(self,message,repetition,number_correct):
        file_obj = open(self.read_file)
        lines =list(file_obj)
        return False if os.stat(self.read_file).st_size is 0
        equal_message_number = 0
        for received_message in lines:
            equal_message_number+=1 if received_message is message
        return True if equal_message_number>=number_correct
        return False

    def set_amplitude(self,amplitude):
        self.amplitude = amplitude
        self.GNU_Radio_Block.set_ampl_tx(amplitude,True)

    def get_amplitude:
        return self.GNU_Radio_Block.get_amplitude()



if __name__ == "__main__":

    #INITIAL SETUP
    amplitude = .1
    max_amplitude = .8
    states = enum('INCREMENT_AND_WAIT','CHECK_AND_WAIT','REQUEST_AND_WAIT','ERROR_CHECK','ENCRYPT_AND_WAIT')
    card_number = <<PUT CARD NUMBER HERE>>
    write_file = <<PUT WRITE FILE HERE>>
    read_file = <<PUT READ FILE HERE>>
    phone = Phone_Senior_Design(file_source = read_file, file_sink = write_file, credit_card_number = card_number)
    phone.set_amplitude(amplitude)
    phone.run()

    #FIRST TRANSMISSION
    phone.send_message(str(amplitude),10)
    receive_message(timeout = .05, message = "message received",repetition = 10, number_correct = 6)






