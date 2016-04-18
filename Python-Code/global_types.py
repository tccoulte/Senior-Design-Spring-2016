from enum import enum

global class_state = enum('TIMEOUT','RECEIVED','TRANSMITTED','KILLED','IDLE','NOT_RECEIVED')

global phone_state = enum('INCREMENT_AND_WAIT','CHECK_AND_WAIT','REQUEST_AND_WAIT','ERROR_CHECK','ENCRYPT_AND_WAIT')

global station_state = enum()

