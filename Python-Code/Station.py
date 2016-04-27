import time
import sys
from Transmit_Receive_Blocks import Top_Block_Senior_Design
from Senior_Design import Senior_Design
from global_types import class_state,phone_state,station_state
from collections import Counter
import logging
import re
from random import randint

def main():
	repeated_state = False
	amplitude = 1
	station = Senior_Design(file_sink = 'file_sink', file_source= 'file_source', SNR_threshold = 3)
	state = station_state.IDLE
	while True
		if state == station_state.IDLE:
			station.run()
			time.sleep(10) 
			raw_input("Press Enter to continue...")
			state = station_state.SNR_RECEIVE

		elif state == station_state.SNR_RECEIVE:
			station.set_amplitude(amplitude)
			received_message = True
			amount_transmitted = 0
			receive_sleep = 1.5
			transmit_sleep = 1			
			while received_message:
				amount_transmitted += 1
				if amount_transmitted > 2:   
					station.receive_message(time_out = 10, number_correct = 5)
				else:
					station.receive_message(time_out = 10, number_correct = 2)
				time.sleep(receive_sleep) 
				if station.get_state() == class_state.TIMEOUT: 
					state = station_state.KILL
					received_message = False
				elif station.get_state() == class_state.NOT_RECEIVED:
					station.send_message("NotReceivedNotReceived0123456789", 20) 
					received_message = False
					state = station_state.VERIFY_AMPLITUDE
					time.sleep(transmit_sleep)
				elif station.get_state() == class_state.RECEIVED:
					station.send_message("TheMessageWasReceived01234567890", 20)
					time.sleep(transmit_sleep)
				else:
					state = station_state.KILL
					received_message = False

		elif state == station_state.VERIFY_AMPLITUDE:
			station.receive_message(time_out = 10, number_correct = 2)
			if station.get_state() == class_state.TIMEOUT: 
				state = station_state.KILL
			elif station.get_state() == class_state.NOT_RECEIVED and repeated_state == False:
				station.send_message("NotReceivedInVerificationState12", 20) 
				time.sleep(transmit_sleep)
				repeated_state = True
			elif station.get_state() == class_state.RECEIVED:
				if station.get_message() == "NotReceivedInSendAmplitude012345":
					state = station_state.KILL
				else:		
					new_amplitude = float(parse_amplitude_message(station.get_message()))
					station.set_amplitude(new_amplitude)
					station.send_message("AmplitudeVerification01234567891", 20)
					time.sleep(transmit_sleep)
					state = station_state.SEND_KEY_REQUEST_ENCRYPT
					repeated_state = False
			else:
				state = station_state.KILL

		elif state == station_state.SEND_KEY_REQUEST_ENCRYPT:
			key = key_generator()
			station.receive_message(time_out = 10, number_correct = 2)
			if station.get_state() == class_state.TIMEOUT: 
				state = station_state.KILL
			elif station.get_state() == class_state.NOT_RECEIVED and repeated_state == False:
				station.send_message("NotReceivedInSendKeyState1234567", 20) 
				time.sleep(transmit_sleep)
				repeated_state = True
			elif station.get_state() == class_state.RECEIVED:	
				station.send_message(key, 20)
				time.sleep(transmit_sleep)
				state = station_state.RECEIVE_ENCRYPTED
				repeated_state = False
			else:
				state = station_state.KILL

		elif state == station_state.RECEIVE_ENCRYPTED:
			station.receive_message(time_out = 10, number_correct = 2)
			if station.get_state() == class_state.TIMEOUT: 
				state = station_state.KILL
			elif station.get_state() == class_state.NOT_RECEIVED:
				station.send_message("NotReceivedInDecryptKeyState1234", 20) 
				time.sleep(transmit_sleep)
			elif station.get_state() == class_state.RECEIVED:
				station.send_message("SuccessfullyReceivedEncryptedKey", 20)
				time.sleep(transmit_sleep)
				encrypted_card = station.get_message()
				print "This is the encryped message: " + encrypted_card 
				card = decrypt(encrypted_card)
				print "This is the card information: " + card
				state = station_state.SHUTDOWN
			else:
				state = station_state.KILL
			
		elif state == station_state.SHUTDOWN:
			station.set_amplitude(1)
			station.receive_message(time_out = 10, number_correct = 2)
			if station.get_state() == class_state.TIMEOUT: 
				sys.exit("timeout in Shutdown")
			elif station.get_state() == class_state.NOT_RECEIVED:
				sys.exit("not received in Shutdown")
			elif station.get_state() == class_state.RECEIVED:
				station.send_message("ShutdownActivatedShutdownActivated", 20)
				time.sleep(transmit_sleep)
				sys.exit("worked perfectly")
			else:
				state = station_state.KILL

		elif state == station_state.KILL:
			sys.exit('KILLED')

		else:
			sys.exit('unknown state')

def key_generator():
	output = ""
	for x in range(16): 
		output = output + format(randint(0,255),'02X')
	return output

def parse_amplitude_message(message):
	return (Counter(re.findall(r"[-+]?\d*\.\d+|\d+", message)).most_common(1))[0][0]

if __name__ == '__main__':
	logging.basicConfig(filename='Logging/station.log', 
		level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
	main()
	logging.info("Application Finished")