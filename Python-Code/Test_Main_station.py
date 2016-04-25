import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design
from Senior_Design import Senior_Design
from global_types import class_state,phone_state,station_state
from collections import Counter
import logging
import re


#////////////////////////////////////////////////////
################# SEND/RECEIVE TESTS #######################
#////////////////////////////////////////////////////

def sender():
    transmitter = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 1)
    transmitter.run()
    raw_input("Press Enter to continue...")
    transmitter.send_message( "This is the first message",40)
    time.sleep(.8)
    # transmitter.send_message(self, "This is the second message",10)
    time.sleep(2)
    sys.exit("Sent...")

def receive_known():
    receiver = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 1.5)
    receiver.run()
    raw_input("Press Enter to continue...")
    receiver.receive_message(time_out = 10,message = "This is ")
    if receiver.get_state() == class_state.RECEIVED:
        sys.exit("Message Received Properly")
    elif receiver.get_state() == class_state.NOT_RECEIVED:
        sys.exit("SNR threshold met, but Message not received")
    elif receiver.get_state() == class_state.TIMEOUT:
        sys.exit("SNR threshold not met")
    else: 
        sys.exit("EPIC FAIL.... State is: "+ str(receiver.get_state()) + "   ... See Log")

def receive_unknown():
    receiver = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 1)
    receiver.run()
    raw_input("Press Enter to continue...")
    receiver.receive_message(time_out = 10)
    if receiver.get_state() == class_state.RECEIVED:
        sys.exit("Message Received Properly")
    elif receiver.get_state() == class_state.NOT_RECEIVED:
        sys.exit("SNR threshold met, but Message not received")
    elif receiver.get_state() == class_state.TIMEOUT:
        sys.exit("SNR threshold not met")
    else: 
        sys.exit("EPIC FAIL.... State is: "+ str(receiver.get_state()) + "   ... See Log")

#////////////////////////////////////////////////////
################# PHONE VERSION #######################
#////////////////////////////////////////////////////

def back_and_forth_p():
    amplitude = 1
    phone = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 4)
    phone.run()
    raw_input("Press Enter to continue...")
    phone.send_message("This is the first message",10)
    phone.receive_message(time_out = .6)
    if phone.get_state() != class_state.RECEIVED:
        sys.exit(" message 2 not Received at Phone")
    phone.send_message("This is the third message",10)
    sys.exit("COMPLETED SUCCESSFULLY")

def SNR_p():
    amp_min = .2
    amp_increment = .2
    received_message = True
    phone = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 4)
    phone.run()
    raw_input("Press Enter to continue...")
    phone.set_amplitude(1)
    while received_message and phone.get_amplitude() <= amp_min:
        #message_to_send = ''.join([(phone.get_amplitude() + " ") for x in xrange(10)])
        message_to_send = "Fuck this project"
        phone.send_message(message_to_send,20)
        phone.receive_message(time_out = 4)
        if phone.get_state() == class_state.RECEIVED:
            if phone.get_message() == "The message was received":
                phone.set_amplitude(decrement_ampl(amp_increment))
            elif phone.get_message() == "not received not received":
                sys.exit("worked")
            else:
                sys.exit("received message not expected")
        else:
            sys.exit("failed")

def decrement_ampl(ampl, amount):
    ampl = ampl-amount
    return ampl

#////////////////////////////////////////////////////
################# STATION VERSION #######################
#////////////////////////////////////////////////////


def back_and_forth_s():
    amplitude = 1
    station = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 4)
    station.set_amplitude(amplitude)
    station.run()
    raw_input("Press Enter to continue...")
    station.receive_message(time_out = 20)
    time.sleep(.5)
    if station.get_state() != class_state.RECEIVED:
        sys.exit("message 1 not Received at Station")
    station.send_message("This is the second message", 20)
    time.sleep(.5)
    station.receive_message(time_out = 3)
    time.sleep(.3)
    if station.get_state() != class_state.RECEIVED:
        sys.exit("message 3 not Received at Station")
    sys.exit("COMPLETED SUCCESSFULLY")

def SNR_s():
    station = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 4)
    station.run()
    raw_input("Press Enter to continue...")
    station.set_amplitude(1)
    received_message = True
    while received_message:
        station.receive_message(time_out = 10)
        time.sleep(1)
        if station.get_state() != class_state.RECEIVED:
            received_message = False
            station.send_message("not received not received",20)
            time.sleep(.8)
        else:
            station.send_message("The message was received",20)
            time.sleep(.8)
       
########## USEFUL FUNCTIONS #############

def parse_amplitude_message(message):
     return (Counter(re.findall(r"[-+]?\d*\.\d+|\d+", message)).most_common(1))[0][0]

############# MAIN ######################

if __name__ == '__main__':
    logging.basicConfig(filename='Logging/test.log', 
        level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
    # add filemode = 'w' if you want to overwrite log file
    #Call Test
    SNR_s()
    logging.info("Application Finished")

