#!/usr/bin/env python2

from gnuradio import filter
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
import time



# ////////////////////////////////////////////////////////////////////////
#                           Top Block
# ////////////////////////////////////////////////////////////////////////




class Top_Block_Senior_Design(gr.top_block):
	def __init__(self,file_source_t, file_sink_t, disconnect_transmit=False, disconnect_receive=False, enable_initial_transmit=False):
		gr.top_block.__init__(self, "Top Block Senior Design")

		##################################################
		# Variables
		##################################################
		tx_gain_t = 5
		samps_per_sym_t = 4
		samp_rate_t = 1E6
		rx_gain_t = 5
		pay_len_t = 15
		freq_t = 13.56E6
		ampl_t = 1

		# holds amplitude if transmiter or receiver isn't going

		self.ampl = ampl_t

		##################################################
		# Transmit And Recieve Blocks
		##################################################
		self.tx_path = transmit_path(tx_gain = tx_gain_t, samps_per_sym = samps_per_sym_t,
									pay_len = pay_len_t, freq = freq_t, 
									samp_rate = samp_rate_t, ampl = ampl_t, file_source = file_source_t)
		self.rx_path = receive_path(samps_per_sym = samps_per_sym_t, 
									samp_rate = samp_rate_t, freq = freq_t, file_sink = file_sink_t,
									ampl = ampl_t)


		# Connect Blocks
		self.connect_tx()
		self.connect_rx()


		#only receive or transmit option
		if disconnect_transmit:
			self.disconnect_tx();
		if disconnect_receive:
			self.disconnect_rx();

		#initial decision to transmit or receive
		if enable_initial_transmit:
			self.set_transmit(True)  
		else:
			self.set_transmit(False)
		

	# Choose to trasnmit or receive 

	def set_transmit(self, enabled):
		if enabled:
			self.set_ampl_rx(0)
			self.set_ampl_tx(self.get_ampl())
			# self.rx_path.set_ampl(0)
			# self.tx_path.set_ampl(self.get_ampl())
		else:
			# self.tx_path.set_ampl(0)
			# self.rx_path.set_ampl(self.get_ampl())
			self.set_ampl_rx(1)
			self.set_ampl_tx(0)

	# Send New data from File
	# TODO: see if this even works
	def send_new_packet(self, message_string, repeat_number, repeat_bool = False):
		"""Locks graph, closes file and then writes new message to be sent. The file is then opened
		and the flow graph is unlocked
		"""

		self.lock_tx()
		self.set_transmit(False)
		self.close_file_source()
		self.write_new_data_to_file(message_string, repeat_number)
		self.open_file_source(repeat_bool)
		self.set_transmit(True)
		self.unlock_tx()
	

	def write_new_data_to_file(self, message_string , repeat_number):
		"""Helper for new_packet that writes to the file source"""
		self.tx_path.write_to_file(message_string, repeat_number)

	# Get SNR
	def SNR(self):
		return self.rx_path.get_SNR()

	# Clear file
	def clear_file_sink(self):
		self.lock_rx()
		self.rx_path.clear_file()
		self.unlock_rx()
	
	#  Close/Open Receive File
	def close_file_sink(self):
		self.rx_path.close_file()

	def open_file_sink(self):
		self.rx_path.open_file()
		
	# Close/Open Transmit File
	def close_file_source(self):
		self.tx_path.close_file()

	def open_file_source(self,repeat):
		self.tx_path.open_file(repeat)

	# Disconnect, Connect, Lock and Unlock Functions
	def lock_tx(self):
		self.tx_path.lock()

	def lock_rx(self):
		self.rx_path.lock()

	def unlock_tx(self):
		self.tx_path.unlock()

	def unlock_rx(self):
		self.rx_path.unlock()

	def disconnect_tx(self):
		self.disconnect(self.tx_path)

	def disconnect_rx(self):
		self.disconnect(self.rx_path)

	def connect_tx(self):
		self.connect(self.tx_path)

	def connect_rx(self):
		self.connect(self.rx_path)


	# Getters and Setters
	def get_tx_gain(self):
		return self.tx_path.get_tx_gain()

	def set_tx_gain(self, tx_gain):
		self.tx_path.set_tx_gain(tx_gain)

	def get_samps_per_sym(self):
		return self.tx_path.get_samps_per_sym()

	def set_samps_per_sym(self, samps_per_sym):
		self.tx_path.set_samps_per_sym(samps_per_sym)
		self.rx_path.set_samps_per_sym(samps_per_sym)

	def get_samp_rate(self):
		return self.tx_path.get_samp_rate()

	def set_samp_rate(self, samp_rate):
		self.tx_path.set_samp_rate(samp_rate)
		self.rx_path.set_samp_rate(samp_rate)

	def get_rx_gain(self):
		return self.rx_path.get_rx_gain()

	def set_rx_gain(self, rx_gain):
		self.rx_path.set_rx_gain(rx_gain)

	def get_pay_len(self):
		return self.tx_path.get_pay_len()

	def set_pay_len(self, pay_len):
		self.tx_path.set_pay_len(pay_len)

	def get_freq(self):
		return self.tx_path.get_freq()

	def set_freq(self, freq):
		self.tx_path.set_freq(freq)
		self.rx_path.set_freq(freq)

	def get_ampl(self):
		return self.ampl
	
	#globl variable used to set Top_block amplitude at the same time
	def set_ampl_rx(self, ampl,globl = False):
		self.rx_path.set_ampl(ampl)
		if globl is True:
			self.ampl = ampl 

	def set_ampl_tx(self, ampl,globl = False):
		self.tx_path.set_ampl(ampl)
		if globl is True:
			self.ampl = ampl

# END TOP_BLOCK_SENIOR_DESIGN



# ////////////////////////////////////////////////////////////////////////
#                           Transmit Path
# ////////////////////////////////////////////////////////////////////////

class transmit_path(gr.hier_block2):
	def __init__(self, tx_gain, samps_per_sym, pay_len, freq, samp_rate, ampl, file_source):
		gr.hier_block2.__init__(self, "transmit_path",
				gr.io_signature(0, 0, 0), # Input signature
				gr.io_signature(0, 0, 0)) # Output signature

		##################################################
		# Variables
		##################################################
		self.file_source = file_source
		self.tx_gain = tx_gain
		self.samps_per_sym = samps_per_sym
		self.samp_rate = samp_rate
		self.pay_len = pay_len
		self.freq = freq
		self.ampl = ampl


		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_sink_0 = uhd.usrp_sink(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
		self.uhd_usrp_sink_0.set_center_freq(freq, 0)
		self.uhd_usrp_sink_0.set_gain(tx_gain, 0)


		self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
				interpolation=125,
				decimation=4,
				taps=None,
				fractional_bw=None,
		)

		self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
				samples_per_symbol=samps_per_sym,
				bits_per_symbol=1,
				preamble="",
				access_code="",
				pad_for_usrp=True,
			),
			payload_length=pay_len,
		)

		self.digital_dxpsk_mod_0 = digital.dbpsk_mod(
			samples_per_symbol=samps_per_sym,
			excess_bw=0.35,
			mod_code="gray",
			verbose=False,
			log=False)

		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((ampl, ))

		self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, file_source, False)

		##################################################
		# Connections
		##################################################
		self.connect((self.digital_dxpsk_mod_0, 0), (self.rational_resampler_xxx_0,0))
		self.connect((self.rational_resampler_xxx_0,0),(self.blocks_multiply_const_vxx_0,0))
		self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))
		self.connect((self.blks2_packet_encoder_0, 0), (self.digital_dxpsk_mod_0, 0))
		self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))

	# File IO
	def close_file(self):
		self.blocks_file_source_0.close()

	def open_file(self, repeat):
		self.blocks_file_source_0.open(self.file_source,repeat)

	def write_to_file(self, message_string, repeat_number):
		file_obj = open(self.file_source, 'w')
		message = message_string
		for i in range(0,repeat_number-2):
			message = message + '\n' + message_string
		file_obj.write(message)
		file_obj.close()
	
	# Getters and Setters

	def get_tx_gain(self):
		return self.tx_gain

	def set_tx_gain(self, tx_gain):
		self.tx_gain = tx_gain
		self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)

	def get_samps_per_sym(self): 
		return self.samps_per_sym

	def set_samps_per_sym(self, samps_per_sym):
		self.samps_per_sym = samps_per_sym

	def get_samp_rate(self):  
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
	
	def get_pay_len(self):
		return self.pay_len

	def set_pay_len(self, pay_len):
		self.pay_len = pay_len

	def get_ampl(self):
		return self.ampl

	def set_ampl(self, ampl):
		self.ampl = ampl
		self.blocks_multiply_const_vxx_0.set_k((self.ampl, ))

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)


# END TRANSMIT_PATH


# ////////////////////////////////////////////////////////////////////////
#                           Receive Path
# ////////////////////////////////////////////////////////////////////////

class receive_path(gr.hier_block2):
	def __init__(self, samps_per_sym, samp_rate, freq, file_sink, ampl):
		gr.hier_block2.__init__(self, "receive_path",
				gr.io_signature(0, 0, 0), # Input signature
				gr.io_signature(0, 0, 0)) # Output signature

		##################################################
		# Variables
		##################################################
		self.file_sink = file_sink
		self.rx_gain = rx_gain = 5
		self.samps_per_sym = samps_per_sym
		self.samp_rate = samp_rate
		self.freq = freq
		self.ampl = ampl 

		##################################################
		# Blocks
		##################################################
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(freq, 0)
		self.uhd_usrp_source_0.set_gain(rx_gain, 0)


		self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
				interpolation=4,
				decimation=125,
				taps=None,
				fractional_bw=None,
		)

		self.digital_dxpsk_demod_0 = digital.dbpsk_demod(
			samples_per_symbol=samps_per_sym,
			excess_bw=0.35,
			freq_bw=6.28/100.0,
			phase_bw=6.28/100.0,
			timing_bw=6.28/100.0,
			mod_code="gray",
			verbose=False,
			log=False)

		self.digital_mpsk_snr_est_cc_0 = digital.mpsk_snr_est_cc(2, 10000, 0.0001)

		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((ampl, ))

		self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, file_sink, True)
		self.blocks_file_sink_0.set_unbuffered(False)

		self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
				access_code="",
				threshold=-1,# END TRANSMIT_PATH

				callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
			),
		)

		##################################################
		# Connections
		##################################################
		self.connect((self.blocks_multiply_const_vxx_0, 0),(self.digital_mpsk_snr_est_cc_0, 0))
		self.connect((self.digital_mpsk_snr_est_cc_0, 0), (self.digital_dxpsk_demod_0, 0))
		self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
		self.connect((self.digital_dxpsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
		self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0))
		self.connect((self.rational_resampler_xxx_0,0),(self.blocks_multiply_const_vxx_0,0))
		#self.set_ampl(1)

	# Get SNR 
	def get_SNR(self):
		return self.digital_mpsk_snr_est_cc_0.snr()
	# File IO

	def clear_file(self):
		open(self.file_sink, 'w').close()

	def close_file(self):
		self.blocks_file_source_0.close()

	def open_file(self):
		self.blocks_file_source_0.open(self.file_sink)


	# Getters and Setters 
	
	def get_rx_gain(self):
		return self.rx_gain

	def set_rx_gain(self, rx_gain):
		self.rx_gain = rx_gain
		self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)

	def get_samps_per_sym(self): 
		return self.samps_per_sym

	def set_samps_per_sym(self, samps_per_sym):
		self.samps_per_sym = samps_per_sym

	def get_samp_rate(self):  
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

	def get_ampl(self):
		return self.ampl

	def set_ampl(self, ampl):
		self.ampl = ampl 
		self.blocks_multiply_const_vxx_0.set_k((self.ampl, ))

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

# END RECEIVE_PATH
