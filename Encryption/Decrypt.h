#ifndef Decrypt_h
#define Decrypt_h

using namespace std;

struct stateType
{
	int array[4][4];
};

struct keyType
{
	int array[4][36];
};

stateType invSubBytes(stateType state);
stateType addRoundKey(stateType state, keyType key, int roundNumber);
keyType expandKey(stateType key);
stateType invShiftRows(stateType state);
void printState(stateType state);
stateType createState(string cardNumber);
string Decrypt(stateType state, string keyInput);

#endif