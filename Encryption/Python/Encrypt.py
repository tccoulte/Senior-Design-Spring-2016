import math

def key32to16(string32):
	output = ""
	for x in range(16):
		hexDigits = string32[2*x] + string32[2*x+1]
		output = output + (chr(int("0x" + hexDigits,16)))
	return output

def data32to16(string32):
	tempState = [[0 for x in range(4)] for y in range(4)]
	for col in range(4):
		for row in range(4):
			hexDigits = string32[2*(row+col*4)] + string32[2*(row+col*4)+1]
			tempState[row][col] = int("0x" + hexDigits, 16)
	return tempState

def encrypt(cardNumber, keyInput):
	key = createState(keyInput)
	expandedKey = expandKey(key)
	state = createState(cardNumber)
	state = addRoundKey(state, expandedKey, 0)
	for roundNumber in range(1,9):
		state = subBytes(state)
		state = shiftRows(state)
		state = addRoundKey(state,expandedKey,roundNumber)
	output = ""
	for col in range(4):
		for row in range(4):
			output = output + format(state[row][col],'02X')
	return output

def decrypt(state, keyInput):
	key = createState(keyInput)
	expandedKey = expandKey(key)
	for roundNumber in range(8,0,-1):
		state = addRoundKey(state,expandedKey,roundNumber)
		state = invShiftRows(state)
		state = invSubBytes(state)
	state = addRoundKey(state,expandedKey,0)
	output = ""
	for col in range(4):
		for row in range(4):
			output = output + chr(state[row][col])
	return output

def addRoundKey(state, key, roundNumber):
	tempState = [[0 for x in range(4)] for y in range(4)]
	for row in range(4):
		for col in range(4):
			tempState[row][col] = state[row][col]^key[row][col+roundNumber*4]
	return tempState


def createState(cardNumber):
	state = [[0 for x in range(4)] for y in range(4)]
	for col in range(4):
		for row in range(4):
			state[row][col] = int(format(ord(cardNumber[row + col*4]), '02X'),16)
	return state

def printState(state):
	for row in range(4):
		for col in range(4):
			print format(state[row][col],'02X'),
		print ''
	print ''

def printKey(key):
	for row in range(4):
		for col in range(36):
			print format(key[row][col],'02X'),
		print ''
	print ''

def shiftRows(state):
	tempState = state
	for row in range(4):
		for shifter in range(row):
			temp = state[row][0]
			for col in range(3):
				tempState[row][col] = state[row][col+1]
			tempState[row][3] = temp
	return tempState

def subBytes(state):
	tempState = [[0 for x in range(4)] for y in range(4)]
	for row in range(4):
		for col in range(4):
			tempState[row][col] = subB(state[row][col])
	return tempState

def expandKey(key):
	expandedKey = [[0 for x in range(36)] for y in range(4)]
	for row in range(4):
		for col in range(4):
			expandedKey[row][col] = key[row][col]
	prevColumn = [expandedKey[0][3], expandedKey[1][3], expandedKey[2][3], expandedKey[3][3]]
	for keyColumn in range(4,36):
		column = [prevColumn[0], prevColumn[1], prevColumn[2], prevColumn[3]]
		for row in range(4):
			column[row] = subB(column[row])
		tempVal = column[0]
		for row in range(3):
			column[row] = column[row+1]
		column[3] = tempVal
		i = (keyColumn/4)-1
		rCon = math.pow(2,i)
		column[0] = column[0]^int(rCon)
		for row in range(4):
			column[row] = column[row]^int(expandedKey[row][keyColumn-4])
			expandedKey[row][keyColumn] = column[row]
		for x in range(4):
			prevColumn[x] = column[x]
	return expandedKey

def invShiftRows(state):
	tempState = [[0 for x in range(4)] for y in range(4)]
	for row in range(4):
		for col in range(4):
			tempState[row][col] = state[row][col]
	for row in range(4):
		for shifter in range(row):
			tempVal = tempState[row][3]
			for col in range(3,0,-1):
				tempState[row][col] = tempState[row][col-1]
			tempState[row][0] = tempVal
	return tempState

def invSubBytes(state):
	tempState = [[0 for x in range(4)] for y in range(4)]
	for row in range(4):
		for col in range(4):
			tempState[row][col] = invSubB(state[row][col])
	return tempState

def invSubB(value):
	if value == int('63',16):
		tempVal = int('00',16)
	elif value == int('7c',16):
		tempVal = int('01',16)
	elif value == int('77',16):
		tempVal = int('02',16)
	elif value == int('7b',16):
		tempVal = int('03',16)
	elif value == int('f2',16):
		tempVal = int('04',16)
	elif value == int('6b',16):
		tempVal = int('05',16)
	elif value == int('6f',16):
		tempVal = int('06',16)
	elif value == int('c5',16):
		tempVal = int('07',16)
	elif value == int('30',16):
		tempVal = int('08',16)
	elif value == int('01',16):
		tempVal = int('09',16)
	elif value == int('67',16):
		tempVal = int('0a',16)
	elif value == int('2b',16):
		tempVal = int('0b',16)
	elif value == int('fe',16):
		tempVal = int('0c',16)
	elif value == int('d7',16):
		tempVal = int('0d',16)
	elif value == int('ab',16):
		tempVal = int('0e',16)
	elif value == int('76',16):
		tempVal = int('0f',16)
	elif value == int('ca',16):
		tempVal = int('10',16)
	elif value == int('82',16):
		tempVal = int('11',16)
	elif value == int('c9',16):
		tempVal = int('12',16)
	elif value == int('7d',16):
		tempVal = int('13',16)
	elif value == int('fa',16):
		tempVal = int('14',16)
	elif value == int('59',16):
		tempVal = int('15',16)
	elif value == int('47',16):
		tempVal = int('16',16)
	elif value == int('f0',16):
		tempVal = int('17',16)
	elif value == int('ad',16):
		tempVal = int('18',16)
	elif value == int('d4',16):
		tempVal = int('19',16)
	elif value == int('a2',16):
		tempVal = int('1a',16)
	elif value == int('af',16):
		tempVal = int('1b',16)
	elif value == int('9c',16):
		tempVal = int('1c',16)
	elif value == int('a4',16):
		tempVal = int('1d',16)
	elif value == int('72',16):
		tempVal = int('1e',16)
	elif value == int('c0',16):
		tempVal = int('1f',16)
	elif value == int('b7',16):
		tempVal = int('20',16)
	elif value == int('fd',16):
		tempVal = int('21',16)
	elif value == int('93',16):
		tempVal = int('22',16)
	elif value == int('26',16):
		tempVal = int('23',16)
	elif value == int('36',16):
		tempVal = int('24',16)
	elif value == int('3f',16):
		tempVal = int('25',16)
	elif value == int('f7',16):
		tempVal = int('26',16)
	elif value == int('cc',16):
		tempVal = int('27',16)
	elif value == int('34',16):
		tempVal = int('28',16)
	elif value == int('a5',16):
		tempVal = int('29',16)
	elif value == int('e5',16):
		tempVal = int('2a',16)
	elif value == int('f1',16):
		tempVal = int('2b',16)
	elif value == int('71',16):
		tempVal = int('2c',16)
	elif value == int('d8',16):
		tempVal = int('2d',16)
	elif value == int('31',16):
		tempVal = int('2e',16)
	elif value == int('15',16):
		tempVal = int('2f',16)
	elif value == int('04',16):
		tempVal = int('30',16)
	elif value == int('c7',16):
		tempVal = int('31',16)
	elif value == int('23',16):
		tempVal = int('32',16)
	elif value == int('c3',16):
		tempVal = int('33',16)
	elif value == int('18',16):
		tempVal = int('34',16)
	elif value == int('96',16):
		tempVal = int('35',16)
	elif value == int('05',16):
		tempVal = int('36',16)
	elif value == int('9a',16):
		tempVal = int('37',16)
	elif value == int('07',16):
		tempVal = int('38',16)
	elif value == int('12',16):
		tempVal = int('39',16)
	elif value == int('80',16):
		tempVal = int('3a',16)
	elif value == int('e2',16):
		tempVal = int('3b',16)
	elif value == int('eb',16):
		tempVal = int('3c',16)
	elif value == int('27',16):
		tempVal = int('3d',16)
	elif value == int('b2',16):
		tempVal = int('3e',16)
	elif value == int('75',16):
		tempVal = int('3f',16)
	elif value == int('09',16):
		tempVal = int('40',16)
	elif value == int('83',16):
		tempVal = int('41',16)
	elif value == int('2c',16):
		tempVal = int('42',16)
	elif value == int('1a',16):
		tempVal = int('43',16)
	elif value == int('1b',16):
		tempVal = int('44',16)
	elif value == int('6e',16):
		tempVal = int('45',16)
	elif value == int('5a',16):
		tempVal = int('46',16)
	elif value == int('a0',16):
		tempVal = int('47',16)
	elif value == int('52',16):
		tempVal = int('48',16)
	elif value == int('3b',16):
		tempVal = int('49',16)
	elif value == int('d6',16):
		tempVal = int('4a',16)
	elif value == int('b3',16):
		tempVal = int('4b',16)
	elif value == int('29',16):
		tempVal = int('4c',16)
	elif value == int('e3',16):
		tempVal = int('4d',16)
	elif value == int('2f',16):
		tempVal = int('4e',16)
	elif value == int('84',16):
		tempVal = int('4f',16)
	elif value == int('53',16):
		tempVal = int('50',16)
	elif value == int('d1',16):
		tempVal = int('51',16)
	elif value == int('00',16):
		tempVal = int('52',16)
	elif value == int('ed',16):
		tempVal = int('53',16)
	elif value == int('20',16):
		tempVal = int('54',16)
	elif value == int('fc',16):
		tempVal = int('55',16)
	elif value == int('b1',16):
		tempVal = int('56',16)
	elif value == int('5b',16):
		tempVal = int('57',16)
	elif value == int('6a',16):
		tempVal = int('58',16)
	elif value == int('cb',16):
		tempVal = int('59',16)
	elif value == int('be',16):
		tempVal = int('5a',16)
	elif value == int('39',16):
		tempVal = int('5b',16)
	elif value == int('4a',16):
		tempVal = int('5c',16)
	elif value == int('4c',16):
		tempVal = int('5d',16)
	elif value == int('58',16):
		tempVal = int('5e',16)
	elif value == int('cf',16):
		tempVal = int('5f',16)
	elif value == int('d0',16):
		tempVal = int('60',16)
	elif value == int('ef',16):
		tempVal = int('61',16)
	elif value == int('aa',16):
		tempVal = int('62',16)
	elif value == int('fb',16):
		tempVal = int('63',16)
	elif value == int('43',16):
		tempVal = int('64',16)
	elif value == int('4d',16):
		tempVal = int('65',16)
	elif value == int('33',16):
		tempVal = int('66',16)
	elif value == int('85',16):
		tempVal = int('67',16)
	elif value == int('45',16):
		tempVal = int('68',16)
	elif value == int('f9',16):
		tempVal = int('69',16)
	elif value == int('02',16):
		tempVal = int('6a',16)
	elif value == int('7f',16):
		tempVal = int('6b',16)
	elif value == int('50',16):
		tempVal = int('6c',16)
	elif value == int('3c',16):
		tempVal = int('6d',16)
	elif value == int('9f',16):
		tempVal = int('6e',16)
	elif value == int('a8',16):
		tempVal = int('6f',16)
	elif value == int('51',16):
		tempVal = int('70',16)
	elif value == int('a3',16):
		tempVal = int('71',16)
	elif value == int('40',16):
		tempVal = int('72',16)
	elif value == int('8f',16):
		tempVal = int('73',16)
	elif value == int('92',16):
		tempVal = int('74',16)
	elif value == int('9d',16):
		tempVal = int('75',16)
	elif value == int('38',16):
		tempVal = int('76',16)
	elif value == int('f5',16):
		tempVal = int('77',16)
	elif value == int('bc',16):
		tempVal = int('78',16)
	elif value == int('b6',16):
		tempVal = int('79',16)
	elif value == int('da',16):
		tempVal = int('7a',16)
	elif value == int('21',16):
		tempVal = int('7b',16)
	elif value == int('10',16):
		tempVal = int('7c',16)
	elif value == int('ff',16):
		tempVal = int('7d',16)
	elif value == int('f3',16):
		tempVal = int('7e',16)
	elif value == int('d2',16):
		tempVal = int('7f',16)
	elif value == int('cd',16):
		tempVal = int('80',16)
	elif value == int('0c',16):
		tempVal = int('81',16)
	elif value == int('13',16):
		tempVal = int('82',16)
	elif value == int('ec',16):
		tempVal = int('83',16)
	elif value == int('5f',16):
		tempVal = int('84',16)
	elif value == int('97',16):
		tempVal = int('85',16)
	elif value == int('44',16):
		tempVal = int('86',16)
	elif value == int('17',16):
		tempVal = int('87',16)
	elif value == int('c4',16):
		tempVal = int('88',16)
	elif value == int('a7',16):
		tempVal = int('89',16)
	elif value == int('7e',16):
		tempVal = int('8a',16)
	elif value == int('3d',16):
		tempVal = int('8b',16)
	elif value == int('64',16):
		tempVal = int('8c',16)
	elif value == int('5d',16):
		tempVal = int('8d',16)
	elif value == int('19',16):
		tempVal = int('8e',16)
	elif value == int('73',16):
		tempVal = int('8f',16)
	elif value == int('60',16):
		tempVal = int('90',16)
	elif value == int('81',16):
		tempVal = int('91',16)
	elif value == int('4f',16):
		tempVal = int('92',16)
	elif value == int('dc',16):
		tempVal = int('93',16)
	elif value == int('22',16):
		tempVal = int('94',16)
	elif value == int('2a',16):
		tempVal = int('95',16)
	elif value == int('90',16):
		tempVal = int('96',16)
	elif value == int('88',16):
		tempVal = int('97',16)
	elif value == int('46',16):
		tempVal = int('98',16)
	elif value == int('ee',16):
		tempVal = int('99',16)
	elif value == int('b8',16):
		tempVal = int('9a',16)
	elif value == int('14',16):
		tempVal = int('9b',16)
	elif value == int('de',16):
		tempVal = int('9c',16)
	elif value == int('5e',16):
		tempVal = int('9d',16)
	elif value == int('0b',16):
		tempVal = int('9e',16)
	elif value == int('db',16):
		tempVal = int('9f',16)
	elif value == int('e0',16):
		tempVal = int('a0',16)
	elif value == int('32',16):
		tempVal = int('a1',16)
	elif value == int('3a',16):
		tempVal = int('a2',16)
	elif value == int('0a',16):
		tempVal = int('a3',16)
	elif value == int('49',16):
		tempVal = int('a4',16)
	elif value == int('06',16):
		tempVal = int('a5',16)
	elif value == int('24',16):
		tempVal = int('a6',16)
	elif value == int('5c',16):
		tempVal = int('a7',16)
	elif value == int('c2',16):
		tempVal = int('a8',16)
	elif value == int('d3',16):
		tempVal = int('a9',16)
	elif value == int('ac',16):
		tempVal = int('aa',16)
	elif value == int('62',16):
		tempVal = int('ab',16)
	elif value == int('91',16):
		tempVal = int('ac',16)
	elif value == int('95',16):
		tempVal = int('ad',16)
	elif value == int('e4',16):
		tempVal = int('ae',16)
	elif value == int('79',16):
		tempVal = int('af',16)
	elif value == int('e7',16):
		tempVal = int('b0',16)
	elif value == int('c8',16):
		tempVal = int('b1',16)
	elif value == int('37',16):
		tempVal = int('b2',16)
	elif value == int('6d',16):
		tempVal = int('b3',16)
	elif value == int('8d',16):
		tempVal = int('b4',16)
	elif value == int('d5',16):
		tempVal = int('b5',16)
	elif value == int('4e',16):
		tempVal = int('b6',16)
	elif value == int('a9',16):
		tempVal = int('b7',16)
	elif value == int('6c',16):
		tempVal = int('b8',16)
	elif value == int('56',16):
		tempVal = int('b9',16)
	elif value == int('f4',16):
		tempVal = int('ba',16)
	elif value == int('ea',16):
		tempVal = int('bb',16)
	elif value == int('65',16):
		tempVal = int('bc',16)
	elif value == int('7a',16):
		tempVal = int('bd',16)
	elif value == int('ae',16):
		tempVal = int('be',16)
	elif value == int('08',16):
		tempVal = int('bf',16)
	elif value == int('ba',16):
		tempVal = int('c0',16)
	elif value == int('78',16):
		tempVal = int('c1',16)
	elif value == int('25',16):
		tempVal = int('c2',16)
	elif value == int('2e',16):
		tempVal = int('c3',16)
	elif value == int('1c',16):
		tempVal = int('c4',16)
	elif value == int('a6',16):
		tempVal = int('c5',16)
	elif value == int('b4',16):
		tempVal = int('c6',16)
	elif value == int('c6',16):
		tempVal = int('c7',16)
	elif value == int('e8',16):
		tempVal = int('c8',16)
	elif value == int('dd',16):
		tempVal = int('c9',16)
	elif value == int('74',16):
		tempVal = int('ca',16)
	elif value == int('1f',16):
		tempVal = int('cb',16)
	elif value == int('4b',16):
		tempVal = int('cc',16)
	elif value == int('bd',16):
		tempVal = int('cd',16)
	elif value == int('8b',16):
		tempVal = int('ce',16)
	elif value == int('8a',16):
		tempVal = int('cf',16)
	elif value == int('70',16):
		tempVal = int('d0',16)
	elif value == int('3e',16):
		tempVal = int('d1',16)
	elif value == int('b5',16):
		tempVal = int('d2',16)
	elif value == int('66',16):
		tempVal = int('d3',16)
	elif value == int('48',16):
		tempVal = int('d4',16)
	elif value == int('03',16):
		tempVal = int('d5',16)
	elif value == int('f6',16):
		tempVal = int('d6',16)
	elif value == int('0e',16):
		tempVal = int('d7',16)
	elif value == int('61',16):
		tempVal = int('d8',16)
	elif value == int('35',16):
		tempVal = int('d9',16)
	elif value == int('57',16):
		tempVal = int('da',16)
	elif value == int('b9',16):
		tempVal = int('db',16)
	elif value == int('86',16):
		tempVal = int('dc',16)
	elif value == int('c1',16):
		tempVal = int('dd',16)
	elif value == int('1d',16):
		tempVal = int('de',16)
	elif value == int('9e',16):
		tempVal = int('df',16)
	elif value == int('e1',16):
		tempVal = int('e0',16)
	elif value == int('f8',16):
		tempVal = int('e1',16)
	elif value == int('98',16):
		tempVal = int('e2',16)
	elif value == int('11',16):
		tempVal = int('e3',16)
	elif value == int('69',16):
		tempVal = int('e4',16)
	elif value == int('d9',16):
		tempVal = int('e5',16)
	elif value == int('8e',16):
		tempVal = int('e6',16)
	elif value == int('94',16):
		tempVal = int('e7',16)
	elif value == int('9b',16):
		tempVal = int('e8',16)
	elif value == int('1e',16):
		tempVal = int('e9',16)
	elif value == int('87',16):
		tempVal = int('ea',16)
	elif value == int('e9',16):
		tempVal = int('eb',16)
	elif value == int('ce',16):
		tempVal = int('ec',16)
	elif value == int('55',16):
		tempVal = int('ed',16)
	elif value == int('28',16):
		tempVal = int('ee',16)
	elif value == int('df',16):
		tempVal = int('ef',16)
	elif value == int('8c',16):
		tempVal = int('f0',16)
	elif value == int('a1',16):
		tempVal = int('f1',16)
	elif value == int('89',16):
		tempVal = int('f2',16)
	elif value == int('0d',16):
		tempVal = int('f3',16)
	elif value == int('bf',16):
		tempVal = int('f4',16)
	elif value == int('e6',16):
		tempVal = int('f5',16)
	elif value == int('42',16):
		tempVal = int('f6',16)
	elif value == int('68',16):
		tempVal = int('f7',16)
	elif value == int('41',16):
		tempVal = int('f8',16)
	elif value == int('99',16):
		tempVal = int('f9',16)
	elif value == int('2d',16):
		tempVal = int('fa',16)
	elif value == int('0f',16):
		tempVal = int('fb',16)
	elif value == int('b0',16):
		tempVal = int('fc',16)
	elif value == int('54',16):
		tempVal = int('fd',16)
	elif value == int('bb',16):
		tempVal = int('fe',16)
	elif value == int('16',16):
		tempVal = int('ff',16)
	return tempVal



def subB(value):
	if value == (int('00',16)) :
		tempVal = (int('63',16))
	elif value == (int('01',16)) :
		tempVal = (int('7c' ,16))
	elif value == (int('02',16)) :
		tempVal = (int('77',16))
	elif value == (int('03',16)) :
		tempVal = (int('7b',16))
	elif value == (int('04',16)) :
		tempVal = (int('f2',16))
	elif value == (int('05',16)) :
		tempVal = (int('6b',16))
	elif value == (int('06',16)) :
		tempVal = (int('6f',16))
	elif value == (int('07',16)) :
		tempVal = (int('c5',16))
	elif value == (int('08',16)) :
		tempVal = (int('30',16))
	elif value == (int('09',16)) :
		tempVal = (int('01',16))
	elif value == (int('0a',16)) :
		tempVal = (int('67',16))
	elif value == (int('0b',16)) :
		tempVal = (int('2b',16))
	elif value == (int('0c',16)) :
		tempVal = (int('fe',16))
	elif value == (int('0d',16)) :
		tempVal = (int('d7',16))
	elif value == (int('0e',16)) :
		tempVal = (int('ab',16))
	elif value == (int('0f',16)) :
		tempVal = (int('76',16))
	elif value == (int('10',16)) :
		tempVal = (int('ca',16))
	elif value == (int('11',16)) :
		tempVal = (int('82',16))
	elif value == (int('12',16)) :
		tempVal = (int('c9',16))
	elif value == (int('13',16)) :
		tempVal = (int('7d',16))
	elif value == (int('14',16)) :
		tempVal = (int('fa',16))
	elif value == (int('15',16)) :
		tempVal = (int('59',16))
	elif value == (int('16',16)) :
		tempVal = (int('47',16))
	elif value == (int('17',16)) :
		tempVal = (int('f0',16))
	elif value == (int('18',16)) :
		tempVal = (int('ad',16))
	elif value == (int('19',16)) :
		tempVal = (int('d4',16))
	elif value == (int('1a',16)) :
		tempVal = (int('a2',16))
	elif value == (int('1b',16)) :
		tempVal = (int('af',16))
	elif value == (int('1c',16)) :
		tempVal = (int('9c',16))
	elif value == (int('1d',16)) :
		tempVal = (int('a4',16))
	elif value == (int('1e',16)) :
		tempVal = (int('72',16))
	elif value == (int('1f',16)) :
		tempVal = (int('c0',16))
	elif value == (int('20',16)) :
		tempVal = (int('b7',16))
	elif value == (int('21',16)) :
		tempVal = (int('fd',16))
	elif value == (int('22',16)) :
		tempVal = (int('93',16))
	elif value == (int('23',16)) :
		tempVal = (int('26',16))
	elif value == (int('24',16)) :
		tempVal = (int('36',16))
	elif value == (int('25',16)) :
		tempVal = (int('3f',16))
	elif value == (int('26',16)) :
		tempVal = (int('f7',16))
	elif value == (int('27',16)) :
		tempVal = (int('cc',16))
	elif value == (int('28',16)) :
		tempVal = (int('34',16))
	elif value == (int('29',16)) :
		tempVal = (int('a5',16))
	elif value == (int('2a',16)) :
		tempVal = (int('e5',16))
	elif value == (int('2b',16)) :
		tempVal = (int('f1',16))
	elif value == (int('2c',16)) :
		tempVal = (int('71',16))
	elif value == (int('2d',16)) :
		tempVal = (int('d8',16))
	elif value == (int('2e',16)) :
		tempVal = (int('31',16))
	elif value == (int('2f',16)) :
		tempVal = (int('15',16))
	elif value == (int('30',16)) :
		tempVal = (int('04',16))
	elif value == (int('31',16)) :
		tempVal = (int('c7',16))
	elif value == (int('32',16)) :
		tempVal = (int('23',16))
	elif value == (int('33',16)) :
		tempVal = (int('c3',16))
	elif value == (int('34',16)) :
		tempVal = (int('18',16))
	elif value == (int('35',16)) :
		tempVal = (int('96',16))
	elif value == (int('36',16)) :
		tempVal = (int('05',16))
	elif value == (int('37',16)) :
		tempVal = (int('9a',16))
	elif value == (int('38',16)) :
		tempVal = (int('07',16))
	elif value == (int('39',16)) :
		tempVal = (int('12',16))
	elif value == (int('3a',16)) :
		tempVal = (int('80',16))
	elif value == (int('3b',16)) :
		tempVal = (int('e2',16))
	elif value == (int('3c',16)) :
		tempVal = (int('eb',16))
	elif value == (int('3d',16)) :
		tempVal = (int('27',16))
	elif value == (int('3e',16)) :
		tempVal = (int('b2',16))
	elif value == (int('3f',16)) :
		tempVal = (int('75',16))
	elif value == (int('40',16)) :
		tempVal = (int('09',16))
	elif value == (int('41',16)) :
		tempVal = (int('83',16))
	elif value == (int('42',16)) :
		tempVal = (int('2c',16))
	elif value == (int('43',16)) :
		tempVal = (int('1a',16))
	elif value == (int('44',16)) :
		tempVal = (int('1b',16))
	elif value == (int('45',16)) :
		tempVal = (int('6e',16))
	elif value == (int('46',16)) :
		tempVal = (int('5a',16))
	elif value == (int('47',16)) :
		tempVal = (int('a0',16))
	elif value == (int('48',16)) :
		tempVal = (int('52',16))
	elif value == (int('49',16)) :
		tempVal = (int('3b',16))
	elif value == (int('4a',16)) :
		tempVal = (int('d6',16))
	elif value == (int('4b',16)) :
		tempVal = (int('b3',16))
	elif value == (int('4c',16)) :
		tempVal = (int('29',16))
	elif value == (int('4d',16)) :
		tempVal = (int('e3',16))
	elif value == (int('4e',16)) :
		tempVal = (int('2f',16))
	elif value == (int('4f',16)) :
		tempVal = (int('84',16))
	elif value == (int('50',16)) :
		tempVal = (int('53',16))
	elif value == (int('51',16)) :
		tempVal = (int('d1',16))
	elif value == (int('52',16)) :
		tempVal = (int('00',16))
	elif value == (int('53',16)) :
		tempVal = (int('ed',16))
	elif value == (int('54',16)) :
		tempVal = (int('20',16))
	elif value == (int('55',16)) :
		tempVal = (int('fc',16))
	elif value == (int('56',16)) :
		tempVal = (int('b1',16))
	elif value == (int('57',16)) :
		tempVal = (int('5b',16))
	elif value == (int('58',16)) :
		tempVal = (int('6a',16))
	elif value == (int('59',16)) :
		tempVal = (int('cb',16))
	elif value == (int('5a',16)) :
		tempVal = (int('be',16))
	elif value == (int('5b',16)) :
		tempVal = (int('39',16))
	elif value == (int('5c',16)) :
		tempVal = (int('4a',16))
	elif value == (int('5d',16)) :
		tempVal = (int('4c',16))
	elif value == (int('5e',16)) :
		tempVal = (int('58',16))
	elif value == (int('5f',16)) :
		tempVal = (int('cf',16))
	elif value == (int('60',16)) :
		tempVal = (int('d0',16))
	elif value == (int('61',16)) :
		tempVal = (int('ef',16))
	elif value == (int('62',16)) :
		tempVal = (int('aa',16))
	elif value == (int('63',16)) :
		tempVal = (int('fb',16))
	elif value == (int('64',16)) :
		tempVal = (int('43',16))
	elif value == (int('65',16)) :
		tempVal = (int('4d',16))
	elif value == (int('66',16)) :
		tempVal = (int('33',16))
	elif value == (int('67',16)) :
		tempVal = (int('85',16))
	elif value == (int('68',16)) :
		tempVal = (int('45',16))
	elif value == (int('69',16)) :
		tempVal = (int('f9',16))
	elif value == (int('6a',16)) :
		tempVal = (int('02',16))
	elif value == (int('6b',16)) :
		tempVal = (int('7f',16))
	elif value == (int('6c',16)) :
		tempVal = (int('50',16))
	elif value == (int('6d',16)) :
		tempVal = (int('3c',16))
	elif value == (int('6e',16)) :
		tempVal = (int('9f',16))
	elif value == (int('6f',16)) :
		tempVal = (int('a8',16))
	elif value == (int('70',16)) :
		tempVal = (int('51',16))
	elif value == (int('71',16)) :
		tempVal = (int('a3',16))
	elif value == (int('72',16)) :
		tempVal = (int('40',16))
	elif value == (int('73',16)) :
		tempVal = (int('8f',16))
	elif value == (int('74',16)) :
		tempVal = (int('92',16))
	elif value == (int('75',16)) :
		tempVal = (int('9d',16))
	elif value == (int('76',16)) :
		tempVal = (int('38',16))
	elif value == (int('77',16)) :
		tempVal = (int('f5',16))
	elif value == (int('78',16)) :
		tempVal = (int('bc',16))
	elif value == (int('79',16)) :
		tempVal = (int('b6',16))
	elif value == (int('7a',16)) :
		tempVal = (int('da',16))
	elif value == (int('7b',16)) :
		tempVal = (int('21',16))
	elif value == (int('7c',16)) :
		tempVal = (int('10',16))
	elif value == (int('7d',16)) :
		tempVal = (int('ff',16))
	elif value == (int('7e',16)) :
		tempVal = (int('f3',16))
	elif value == (int('7f',16)) :
		tempVal = (int('d2',16))
	elif value == (int('80',16)) :
		tempVal = (int('cd',16))
	elif value == (int('81',16)) :
		tempVal = (int('0c',16))
	elif value == (int('82',16)) :
		tempVal = (int('13',16))
	elif value == (int('83',16)) :
		tempVal = (int('ec',16))
	elif value == (int('84',16)) :
		tempVal = (int('5f',16))
	elif value == (int('85',16)) :
		tempVal = (int('97',16))
	elif value == (int('86',16)) :
		tempVal = (int('44',16))
	elif value == (int('87',16)) :
		tempVal = (int('17',16))
	elif value == (int('88',16)) :
		tempVal = (int('c4',16))
	elif value == (int('89',16)) :
		tempVal = (int('a7',16))
	elif value == (int('8a',16)) :
		tempVal = (int('7e',16))
	elif value == (int('8b',16)) :
		tempVal = (int('3d',16))
	elif value == (int('8c',16)) :
		tempVal = (int('64',16))
	elif value == (int('8d',16)) :
		tempVal = (int('5d',16))
	elif value == (int('8e',16)) :
		tempVal = (int('19',16))
	elif value == (int('8f',16)) :
		tempVal = (int('73',16))
	elif value == (int('90',16)) :
		tempVal = (int('60',16))
	elif value == (int('91',16)) :
		tempVal = (int('81',16))
	elif value == (int('92',16)) :
		tempVal = (int('4f',16))
	elif value == (int('93',16)) :
		tempVal = (int('dc',16))
	elif value == (int('94',16)) :
		tempVal = (int('22',16))
	elif value == (int('95',16)) :
		tempVal = (int('2a',16))
	elif value == (int('96',16)) :
		tempVal = (int('90',16))
	elif value == (int('97',16)) :
		tempVal = (int('88',16))
	elif value == (int('98',16)) :
		tempVal = (int('46',16))
	elif value == (int('99',16)) :
		tempVal = (int('ee',16))
	elif value == (int('9a',16)) :
		tempVal = (int('b8',16))
	elif value == (int('9b',16)) :
		tempVal = (int('14',16))
	elif value == (int('9c',16)) :
		tempVal = (int('de',16))
	elif value == (int('9d',16)) :
		tempVal = (int('5e',16))
	elif value == (int('9e',16)) :
		tempVal = (int('0b',16))
	elif value == (int('9f',16)) :
		tempVal = (int('db',16))
	elif value == (int('a0',16)) :
		tempVal = (int('e0',16))
	elif value == (int('a1',16)) :
		tempVal = (int('32',16))
	elif value == (int('a2',16)) :
		tempVal = (int('3a',16))
	elif value == (int('a3',16)) :
		tempVal = (int('0a',16))
	elif value == (int('a4',16)) :
		tempVal = (int('49',16))
	elif value == (int('a5',16)) :
		tempVal = (int('06',16))
	elif value == (int('a6',16)) :
		tempVal = (int('24',16))
	elif value == (int('a7',16)) :
		tempVal = (int('5c',16))
	elif value == (int('a8',16)) :
		tempVal = (int('c2',16))
	elif value == (int('a9',16)) :
		tempVal = (int('d3',16))
	elif value == (int('aa',16)) :
		tempVal = (int('ac',16))
	elif value == (int('ab',16)) :
		tempVal = (int('62',16))
	elif value == (int('ac',16)) :
		tempVal = (int('91',16))
	elif value == (int('ad',16)) :
		tempVal = (int('95',16))
	elif value == (int('ae',16)) :
		tempVal = (int('e4',16))
	elif value == (int('af',16)) :
		tempVal = (int('79',16))
	elif value == (int('b0',16)) :
		tempVal = (int('e7',16))
	elif value == (int('b1',16)) :
		tempVal = (int('c8',16))
	elif value == (int('b2',16)) :
		tempVal = (int('37',16))
	elif value == (int('b3',16)) :
		tempVal = (int('6d',16))
	elif value == (int('b4',16)) :
		tempVal = (int('8d',16))
	elif value == (int('b5',16)) :
		tempVal = (int('d5',16))
	elif value == (int('b6',16)) :
		tempVal = (int('4e',16))
	elif value == (int('b7',16)) :
		tempVal = (int('a9',16))
	elif value == (int('b8',16)) :
		tempVal = (int('6c',16))
	elif value == (int('b9',16)) :
		tempVal = (int('56',16))
	elif value == (int('ba',16)) :
		tempVal = (int('f4',16))
	elif value == (int('bb',16)) :
		tempVal = (int('ea',16))
	elif value == (int('bc',16)) :
		tempVal = (int('65',16))
	elif value == (int('bd',16)) :
		tempVal = (int('7a',16))
	elif value == (int('be',16)) :
		tempVal = (int('ae',16))
	elif value == (int('bf',16)) :
		tempVal = (int('08',16))
	elif value == (int('c0',16)) :
		tempVal = (int('ba',16))
	elif value == (int('c1',16)) :
		tempVal = (int('78',16))
	elif value == (int('c2',16)) :
		tempVal = (int('25',16))
	elif value == (int('c3',16)) :
		tempVal = (int('2e',16))
	elif value == (int('c4',16)) :
		tempVal = (int('1c',16))
	elif value == (int('c5',16)) :
		tempVal = (int('a6',16))
	elif value == (int('c6',16)) :
		tempVal = (int('b4',16))
	elif value == (int('c7',16)) :
		tempVal = (int('c6',16))
	elif value == (int('c8',16)) :
		tempVal = (int('e8',16))
	elif value == (int('c9',16)) :
		tempVal = (int('dd',16))
	elif value == (int('ca',16)) :
		tempVal = (int('74',16))
	elif value == (int('cb',16)) :
		tempVal = (int('1f',16))
	elif value == (int('cc',16)) :
		tempVal = (int('4b',16))
	elif value == (int('cd',16)) :
		tempVal = (int('bd',16))
	elif value == (int('ce',16)) :
		tempVal = (int('8b',16))
	elif value == (int('cf',16)) :
		tempVal = (int('8a',16))
	elif value == (int('d0',16)) :
		tempVal = (int('70',16))
	elif value == (int('d1',16)) :
		tempVal = (int('3e',16))
	elif value == (int('d2',16)) :
		tempVal = (int('b5',16))
	elif value == (int('d3',16)) :
		tempVal = (int('66',16))
	elif value == (int('d4',16)) :
		tempVal = (int('48',16))
	elif value == (int('d5',16)) :
		tempVal = (int('03',16))
	elif value == (int('d6',16)) :
		tempVal = (int('f6',16))
	elif value == (int('d7',16)) :
		tempVal = (int('0e',16))
	elif value == (int('d8',16)) :
		tempVal = (int('61',16))
	elif value == (int('d9',16)) :
		tempVal = (int('35',16))
	elif value == (int('da',16)) :
		tempVal = (int('57',16))
	elif value == (int('db',16)) :
		tempVal = (int('b9',16))
	elif value == (int('dc',16)) :
		tempVal = (int('86',16))
	elif value == (int('dd',16)) :
		tempVal = (int('c1',16))
	elif value == (int('de',16)) :
		tempVal = (int('1d',16))
	elif value == (int('df',16)) :
		tempVal = (int('9e',16))
	elif value == (int('e0',16)) :
		tempVal = (int('e1',16))
	elif value == (int('e1',16)) :
		tempVal = (int('f8',16))
	elif value == (int('e2',16)) :
		tempVal = (int('98',16))
	elif value == (int('e3',16)) :
		tempVal = (int('11',16))
	elif value == (int('e4',16)) :
		tempVal = (int('69',16))
	elif value == (int('e5',16)) :
		tempVal = (int('d9',16))
	elif value == (int('e6',16)) :
		tempVal = (int('8e',16))
	elif value == (int('e7',16)) :
		tempVal = (int('94',16))
	elif value == (int('e8',16)) :
		tempVal = (int('9b',16))
	elif value == (int('e9',16)) :
		tempVal = (int('1e',16))
	elif value == (int('ea',16)) :
		tempVal = (int('87',16))
	elif value == (int('eb',16)) :
		tempVal = (int('e9',16))
	elif value == (int('ec',16)) :
		tempVal = (int('ce',16))
	elif value == (int('ed',16)) :
		tempVal = (int('55',16))
	elif value == (int('ee',16)) :
		tempVal = (int('28',16))
	elif value == (int('ef',16)) :
		tempVal = (int('df',16))
	elif value == (int('f0',16)) :
		tempVal = (int('8c',16))
	elif value == (int('f1',16)) :
		tempVal = (int('a1',16))
	elif value == (int('f2',16)) :
		tempVal = (int('89',16))
	elif value == (int('f3',16)) :
		tempVal = (int('0d',16))
	elif value == (int('f4',16)) :
		tempVal = (int('bf',16))
	elif value == (int('f5',16)) :
		tempVal = (int('e6',16))
	elif value == (int('f6',16)) :
		tempVal = (int('42',16))
	elif value == (int('f7',16)) :
		tempVal = (int('68',16))
	elif value == (int('f8',16)) :
		tempVal = (int('41',16))
	elif value == (int('f9',16)) :
		tempVal = (int('99',16))
	elif value == (int('fa',16)) :
		tempVal = (int('2d',16))
	elif value == (int('fb',16)) :
		tempVal = (int('0f',16))
	elif value == (int('fc',16)) :
		tempVal = (int('b0',16))
	elif value == (int('fd',16)) :
		tempVal = (int('54',16))
	elif value == (int('fe',16)) :
		tempVal = (int('bb',16))
	elif value == (int('ff',16)) :
		tempVal = (int('16',16))
	else:
		pass
	return tempVal

#station sends key to phone
print "State sends random key to phone"
originalKey = chr(0x2a)+chr(0xfd)+chr(0x11)+chr(0x63)+chr(0x8a)+chr(0x00)+chr(0x9b)+chr(0x64)+chr(0x11)+chr(0xbb)+chr(0xcc)+chr(0xe8)+chr(0xfa)+chr(0xaf)+chr(0xbc)+chr(0x12)
print "Original Key:       " + originalKey
keyToSend = "2afd11638a009b6411bbcce8faafbc12"
print "Key To Send:        " + keyToSend
print ""

#phone receives key and encrypts data
keyInput = key32to16(keyToSend)
cardNumber = "HelloHowAreYou??"
print "Phone receives key and encrypts data"
print "Received Key:       " + keyInput
print "Original Message:   " + cardNumber
encryptedMessage = encrypt(cardNumber,keyInput)
print "Encrypted Message:  " + encryptedMessage
print ""

#state receives and decrypts
print "Phone sends encrypted message to station"
stateForDecrypt = data32to16(encryptedMessage)
print ""
printState(stateForDecrypt)
print ""
originalMessage = decrypt(stateForDecrypt, originalKey)
print "Decrypted Message:  " + originalMessage
print ""


