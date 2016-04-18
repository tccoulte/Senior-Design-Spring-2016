#!/usr/bin/env python
import time
import os
from Transmit_Receive_Blocks import Top_Block_Senior_Design
from Timeout import Timeout
from global_types import class_state,phone_state,station_state



class Station_Senior_Design:
    def __init__(self, file_sink, file_soure):
        self.GNU_Radio_Block = Top_Block_Senior_Design(file_source_t = file_source, 
                                file_sink_t = file_sink)
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
    states = station_state.IDLE
    write_file = <<PUT WRITE FILE HERE>>
    read_file = <<PUT READ FILE HERE>>
    station = Station_Senior_Design(file_source = read_file, file_sink = write_file)
    station.set_amplitude(amplitude)
    station.run()
