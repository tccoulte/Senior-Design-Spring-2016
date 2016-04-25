#ifndef Encrypt_h
#define Encrypt_h

using namespace std;

struct stateType
{
	int array[4][4];
};

struct keyType
{
	int array[4][36];
};

void printState(stateType state);
stateType subBytes(stateType state); 
stateType shiftRows(stateType state);
stateType createState(string cardNumber);
keyType expandKey(stateType key);
stateType addRoundKey(stateType state, keyType key, int roundNumber);
stateType Encryption(string cardNumber, string keyInput);

#endif