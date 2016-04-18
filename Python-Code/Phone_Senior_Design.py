#!/usr/bin/env python
import time
import os
from Transmit_Receive_Blocks import Top_Block_Senior_Design
from Timeout import Timeout
from global_types import class_state,phone_state,station_state

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
        self.credit_card_nunber = credit_card_nunber
        self.read_file = file_sink
        self.SNR_threshold = <<FIND ME>>
        self.state_message = class_state.IDLE
        self.amplitude = 0


    def run(self):
        """Starts the program. Call this after initial variables have been set up"""
        self.GNU_Radio_Block.start()
    
    def send_message(self, message,repetition):
        """Sends new message with specified repetition"""
        self.GNU_Radio_Block.send_new_packet(message,repetition)
        self.set_state(class_state.TRANSMITTED)

    def receive_message(self,time_out, message,repetition,number_correct):
        """Try to listen for a message with SNR of at least SNR_threshold. Send TIMEOUT state message 
        if there is a timeout before the SNR is high enough. Send RECEIVED state message if the message is verified
        in the file sink. If the output is not received properly in the output send a NOT_RECEIVED state message.
        """
        try:
            with Timeout(time_out):
                self.GNU_Radio_Block.set_transmit(false)
                self.GNU_Radio_Block.clear_file_sink()
                self.poll_SNR(self.SNR_threshold)
                if self.verify_transmission(message,repetition,number_correct):
                    self.set_state(class_state.RECEIVED)
                else:
                    self.set_state(class_state.NOT_RECEIVED)
        except TimeoutError:
            self.set_state(class_state.TIMEOUT)
            

    def receive_unkown_message(self, message_length, repetition, number_correct):
        #TODO
        pass

    def set_state(self,state):
        self.state_message = state

    def get_credit_card_number(self):
        return self.credit_card_nunber

    def poll_SNR(self,threshold, poll_time):
        """polls SNR every certain number of seconds. NEEDS TO BE PAIRED
        WITH TIMEOUT!!! It will run until it sees high SNR
        """
        high_SNR_bool = False
        while high_SNR_bool is False: 
            snr = self.GNU_Radio_Block.SNR()
            if snr >= theshold:
                high_SNR_bool = True
            time.sleep(poll_time)


    def verify_transmission(self,message,repetition,number_correct):
        """Returns true if the file sink contains a message with a certain repetition and number_correct
                ex. Sent message : "Hello
                                    Hello
                                    Hello"
                If the file sink contains:  "elewl
                                            Hello
                                            Hello"
                and the number_correct needs to be 2 than the function would return true
        """
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
    states = phone_state.IDLE
    card_number = <<PUT CARD NUMBER HERE>>
    write_file = <<PUT WRITE FILE HERE>>
    read_file = <<PUT READ FILE HERE>>
    phone = Phone_Senior_Design(file_source = read_file, file_sink = write_file, credit_card_number = card_number)
    phone.set_amplitude(amplitude)
    phone.run()

    #FIRST TRANSMISSION
    phone.send_message(str(amplitude),10)
    receive_message(timeout = .05, message = "message received",repetition = 10, number_correct = 6)






