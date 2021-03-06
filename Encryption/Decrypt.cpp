#include <iostream>
#include <string>
#include <math.h>
#include "Decrypt.h"
#include "subB.h"
#include "invSubB.h"
#include <time.h>
using namespace std;


int main()
{
	clock_t t1,t2;
	t1 = clock();

	string keyInput = "0123456789012345";
	stateType state;

	state.array[0][0] = 0x51;
	state.array[1][0] = 0x20;
	state.array[2][0] = 0xa0;
	state.array[3][0] = 0x4a;
	state.array[0][1] = 0x75;
	state.array[1][1] = 0x85;
	state.array[2][1] = 0xd2;
	state.array[3][1] = 0xb2;
	state.array[0][2] = 0x51;
	state.array[1][2] = 0xe8;
	state.array[2][2] = 0xa7;
	state.array[3][2] = 0x56;
	state.array[0][3] = 0xcd;
	state.array[1][3] = 0x88;
	state.array[2][3] = 0xcf;
	state.array[3][3] = 0xf5;

	string stringOut;
	stringOut = Decrypt(state,keyInput);
	cout << endl;
	cout << stringOut;
	cout << endl;
	
	t2 = clock();
	float diff = ((float)t2-(float)t1)/CLOCKS_PER_SEC;
	cout << endl;
	cout << diff;
	cout << endl;
	cout << endl;
} //end main






string Decrypt(stateType state, string keyInput)
{
	stateType key = createState(keyInput);
	keyType expandedKey = expandKey(key);

	int roundNumber = 0;

	for(roundNumber = 8; roundNumber > 0; roundNumber--)
		{
			state = addRoundKey(state,expandedKey,roundNumber);
			state = invShiftRows(state);
			state = invSubBytes(state);
		} // end rounds

	state = addRoundKey(state,expandedKey,0);

	char outputChars[16] = {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '};
	int col = 0;
	int row = 0;
	for(col = 0; col < 4; col++)
	{
		for(row = 0; row < 4; row++)
		{
			outputChars[row+col*4] = (char)state.array[row][col];
		}
	}
	string outputString = outputChars;
	return outputString;
}

stateType addRoundKey(stateType state, keyType key, int roundNumber)
{
	int row = 0;
	int col = 0;
	stateType tempState;

	for(row = 0; row < 4; row++)
	{
		for(col = 0; col < 4; col++)
		{
			tempState.array[row][col] = state.array[row][col]^key.array[row][col + roundNumber*4];
		}
	}
	return tempState;
}




keyType expandKey(stateType key)
{
	int row = 0;
	int col = 0;
	keyType extendedKey;
	for (row = 0; row < 4; row++)
	{
		for(col = 0; col < 4; col++)
		{
			extendedKey.array[row][col] = key.array[row][col];
		}
	}  // initialize first 16 bytes

	int keyColumn = 0;
	int prevColumn[4] = {extendedKey.array[0][3],extendedKey.array[1][3],extendedKey.array[2][3],extendedKey.array[3][3]};

	//printState(key); // delete this
	//cout << endl;  // delete this

	for (keyColumn = 4; keyColumn < 36; keyColumn++)  // start creating new columns
	{
		int column[4] = {prevColumn[0], prevColumn[1], prevColumn[2], prevColumn[3]};

		int tempVal = column[0];  // start rotation
		for(row = 0; row < 3; row++)
		{
			column[row] = column[row+1];
			
		}
		column[3] = tempVal; // complete rotation

		for(row = 0; row < 4; row++) // start sub
		{
			column[row] = subB(column[row]);
		}	// complete substitution
		 
		//create Rcon pointer value
		int i = (keyColumn/4) - 1;

		//createRcon value
		int rCon = pow(2,i);

		//XOR with rCon
		column[0] = (column[0]^(rCon));

		for(row = 0; row < 4; row++)
		{
			column[row] = (column[row]^extendedKey.array[row][keyColumn-4]);
			extendedKey.array[row][keyColumn] = column[row];
		}

		int x = 0;
		for(x = 0; x < 4; x++)
		{
			prevColumn[x] = column[x];
		}
			
	}	

	/*
	stateType printer;

	for (row = 0; row < 4; row++)
	{
		for(col = 4; col < 8; col++)
		{
			printer.array[row][col-4] = extendedKey.array[row][col];
		}
	}  // initialize first 16 bytes

	printState(printer);
	*/

	return extendedKey;
} // end expandKey


stateType invShiftRows(stateType state)
{
	int col;
	int row;
	int shifter;
	int temp;
	stateType tempState = state;
	for(row = 1; row < 4; row++)
	{
		for (shifter = 0; shifter < row; shifter++)
		{
			temp = tempState.array[row][3];
			for(col = 3; col > 0; col--)
				{	
				tempState.array[row][col] = tempState.array[row][col-1];
				}
			tempState.array[row][0] = temp;
		}
	}
	return tempState;
}

void printState(stateType state)
{
	cout << endl;
	cout << hex << state.array[0][0] << " " << hex << state.array[0][1] << " " << hex << state.array[0][2] << " " << hex << state.array[0][3] << endl;
	cout << hex << state.array[1][0] << " " << hex << state.array[1][1] << " " << hex << state.array[1][2] << " " << hex << state.array[1][3] << endl;
	cout << hex << state.array[2][0] << " " << hex << state.array[2][1] << " " << hex << state.array[2][2] << " " << hex << state.array[2][3] << endl;
	cout << hex << state.array[3][0] << " " << hex << state.array[3][1] << " " << hex << state.array[3][2] << " " << hex << state.array[3][3] << endl;
	cout << endl;
}

stateType createState(string cardNumber)
{
	int row = 0;
	int col = 0;
	stateType state;
	for (col = 0; col < 4; col++)
	{
		for (row = 0; row < 4; row++)
		{
			state.array[row][col] = (int) cardNumber[4*col+row];
		}
	}
	return state;
}

stateType invSubBytes(stateType state)
{
	stateType tempState; 
	int col = 0;
	int row = 0;
	for (row = 0; row < 4; row++)
	{
		for (col = 0; col < 4; col++)
		{
			tempState.array[row][col] = invSubB(state.array[row][col]);
		}
	}
	return tempState;
}
