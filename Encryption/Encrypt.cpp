#include <iostream>
#include <math.h>
#include <string>
#include "Encrypt.h"
#include "subB.h"

using namespace std;

int main()
{

	string cardNumber = "HelloHowAreYou??";
	string keyInput = "0123456789012345";

	
	stateType str = Encryption(cardNumber, keyInput);
	cout << endl;
	printState(str);
	cout << endl;
	

	/*
	stateType key = createState(keyInput);
	keyType expandedKey = expandKey(key);

	cout << endl;
	int x2 = 0;
	for(x2 = 0; x2 <16; x2++)
	{
		cout << cardNumber[x2];
	}
	cout << endl;
	stateType state = createState(cardNumber);
	printState(state);
	int roundNumber = 0;

	state = addRoundKey(state,expandedKey,0);
	//printState(state);

	int x = 0;
	for(roundNumber = 1; roundNumber < 9; roundNumber++)
	{
		state = subBytes(state);
		state = shiftRows(state);
		state = addRoundKey(state,expandedKey,roundNumber);		
	} // end rounds

	printState(state);
	*/
} // end main


stateType Encryption(string cardNumber, string keyInput)
{
	stateType key = createState(keyInput);
	keyType expandedKey = expandKey(key);

	stateType state = createState(cardNumber);

	int roundNumber = 0;
	state = addRoundKey(state,expandedKey,0);

	for(roundNumber = 1; roundNumber < 9; roundNumber++)
	{
		state = subBytes(state);
		state = shiftRows(state);
		state = addRoundKey(state,expandedKey,roundNumber);		
	} // end rounds

	return state;
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




stateType shiftRows(stateType state)
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
			temp = tempState.array[row][0];
			for(col = 0; col < 3; col++)
			{	
				tempState.array[row][col] = tempState.array[row][col+1];
			}
			tempState.array[row][3] = temp;

		}
	}
	return tempState;
}

stateType subBytes(stateType state)
{
	stateType tempState; 
	int col = 0;
	int row = 0;
	for (row = 0; row < 4; row++)
	{
		for (col = 0; col < 4; col++)
		{
			tempState.array[row][col] = subB(state.array[row][col]);
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
