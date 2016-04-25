#include <iostream>
#include "invSubB.h"

using namespace std;

int invSubB(int val)
{
	int tempVal = 0;
	switch(val)
	{
		case 0x63 :
		tempVal = 0x00;
		break;
		case 0x7c :
		tempVal = 0x01;
		break;
		case 0x77 :
		tempVal = 0x02;
		break;
		case 0x7b :
		tempVal = 0x03;
		break;
		case 0xf2 :
		tempVal = 0x04;
		break;
		case 0x6b :
		tempVal = 0x05;
		break;
		case 0x6f :
		tempVal = 0x06;
		break;
		case 0xc5 :
		tempVal = 0x07;
		break;
		case 0x30 :
		tempVal = 0x08;
		break;
		case 0x01 :
		tempVal = 0x09;
		break;
		case 0x67 :
		tempVal = 0x0a;
		break;
		case 0x2b :
		tempVal = 0x0b;
		break;
		case 0xfe :
		tempVal = 0x0c;
		break;
		case 0xd7 :
		tempVal = 0x0d;
		break;
		case 0xab :
		tempVal = 0x0e;
		break;
		case 0x76 :
		tempVal = 0x0f;
		break;
		case 0xca :
		tempVal = 0x10;
		break;
		case 0x82 :
		tempVal = 0x11;
		break;
		case 0xc9 :
		tempVal = 0x12;
		break;
		case 0x7d :
		tempVal = 0x13;
		break;
		case 0xfa :
		tempVal = 0x14;
		break;
		case 0x59 :
		tempVal = 0x15;
		break;
		case 0x47 :
		tempVal = 0x16;
		break;
		case 0xf0 :
		tempVal = 0x17;
		break;
		case 0xad :
		tempVal = 0x18;
		break;
		case 0xd4 :
		tempVal = 0x19;
		break;
		case 0xa2 :
		tempVal = 0x1a;
		break;
		case 0xaf :
		tempVal = 0x1b;
		break;
		case 0x9c :
		tempVal = 0x1c;
		break;
		case 0xa4 :
		tempVal = 0x1d;
		break;
		case 0x72 :
		tempVal = 0x1e;
		break;
		case 0xc0 :
		tempVal = 0x1f;
		break;
		case 0xb7 :
		tempVal = 0x20;
		break;
		case 0xfd :
		tempVal = 0x21;
		break;
		case 0x93 :
		tempVal = 0x22;
		break;
		case 0x26 :
		tempVal = 0x23;
		break;
		case 0x36 :
		tempVal = 0x24;
		break;
		case 0x3f :
		tempVal = 0x25;
		break;
		case 0xf7 :
		tempVal = 0x26;
		break;
		case 0xcc :
		tempVal = 0x27;
		break;
		case 0x34 :
		tempVal = 0x28;
		break;
		case 0xa5 :
		tempVal = 0x29;
		break;
		case 0xe5 :
		tempVal = 0x2a;
		break;
		case 0xf1 :
		tempVal = 0x2b;
		break;
		case 0x71 :
		tempVal = 0x2c;
		break;
		case 0xd8 :
		tempVal = 0x2d;
		break;
		case 0x31 :
		tempVal = 0x2e;
		break;
		case 0x15 :
		tempVal = 0x2f;
		break;
		case 0x04 :
		tempVal = 0x30;
		break;
		case 0xc7 :
		tempVal = 0x31;
		break;
		case 0x23 :
		tempVal = 0x32;
		break;
		case 0xc3 :
		tempVal = 0x33;
		break;
		case 0x18 :
		tempVal = 0x34;
		break;
		case 0x96 :
		tempVal = 0x35;
		break;
		case 0x05 :
		tempVal = 0x36;
		break;
		case 0x9a :
		tempVal = 0x37;
		break;
		case 0x07 :
		tempVal = 0x38;
		break;
		case 0x12 :
		tempVal = 0x39;
		break;
		case 0x80 :
		tempVal = 0x3a;
		break;
		case 0xe2 :
		tempVal = 0x3b;
		break;
		case 0xeb :
		tempVal = 0x3c;
		break;
		case 0x27 :
		tempVal = 0x3d;
		break;
		case 0xb2 :
		tempVal = 0x3e;
		break;
		case 0x75 :
		tempVal = 0x3f;
		break;
		case 0x09 :
		tempVal = 0x40;
		break;
		case 0x83 :
		tempVal = 0x41;
		break;
		case 0x2c :
		tempVal = 0x42;
		break;
		case 0x1a :
		tempVal = 0x43;
		break;
		case 0x1b :
		tempVal = 0x44;
		break;
		case 0x6e :
		tempVal = 0x45;
		break;
		case 0x5a :
		tempVal = 0x46;
		break;
		case 0xa0 :
		tempVal = 0x47;
		break;
		case 0x52 :
		tempVal = 0x48;
		break;
		case 0x3b :
		tempVal = 0x49;
		break;
		case 0xd6 :
		tempVal = 0x4a;
		break;
		case 0xb3 :
		tempVal = 0x4b;
		break;
		case 0x29 :
		tempVal = 0x4c;
		break;
		case 0xe3 :
		tempVal = 0x4d;
		break;
		case 0x2f :
		tempVal = 0x4e;
		break;
		case 0x84 :
		tempVal = 0x4f;
		break;
		case 0x53 :
		tempVal = 0x50;
		break;
		case 0xd1 :
		tempVal = 0x51;
		break;
		case 0x00 :
		tempVal = 0x52;
		break;
		case 0xed :
		tempVal = 0x53;
		break;
		case 0x20 :
		tempVal = 0x54;
		break;
		case 0xfc :
		tempVal = 0x55;
		break;
		case 0xb1 :
		tempVal = 0x56;
		break;
		case 0x5b :
		tempVal = 0x57;
		break;
		case 0x6a :
		tempVal = 0x58;
		break;
		case 0xcb :
		tempVal = 0x59;
		break;
		case 0xbe :
		tempVal = 0x5a;
		break;
		case 0x39 :
		tempVal = 0x5b;
		break;
		case 0x4a :
		tempVal = 0x5c;
		break;
		case 0x4c :
		tempVal = 0x5d;
		break;
		case 0x58 :
		tempVal = 0x5e;
		break;
		case 0xcf :
		tempVal = 0x5f;
		break;
		case 0xd0 :
		tempVal = 0x60;
		break;
		case 0xef :
		tempVal = 0x61;
		break;
		case 0xaa :
		tempVal = 0x62;
		break;
		case 0xfb :
		tempVal = 0x63;
		break;
		case 0x43 :
		tempVal = 0x64;
		break;
		case 0x4d :
		tempVal = 0x65;
		break;
		case 0x33 :
		tempVal = 0x66;
		break;
		case 0x85 :
		tempVal = 0x67;
		break;
		case 0x45 :
		tempVal = 0x68;
		break;
		case 0xf9 :
		tempVal = 0x69;
		break;
		case 0x02 :
		tempVal = 0x6a;
		break;
		case 0x7f :
		tempVal = 0x6b;
		break;
		case 0x50 :
		tempVal = 0x6c;
		break;
		case 0x3c :
		tempVal = 0x6d;
		break;
		case 0x9f :
		tempVal = 0x6e;
		break;
		case 0xa8 :
		tempVal = 0x6f;
		break;
		case 0x51 :
		tempVal = 0x70;
		break;
		case 0xa3 :
		tempVal = 0x71;
		break;
		case 0x40 :
		tempVal = 0x72;
		break;
		case 0x8f :
		tempVal = 0x73;
		break;
		case 0x92 :
		tempVal = 0x74;
		break;
		case 0x9d :
		tempVal = 0x75;
		break;
		case 0x38 :
		tempVal = 0x76;
		break;
		case 0xf5 :
		tempVal = 0x77;
		break;
		case 0xbc :
		tempVal = 0x78;
		break;
		case 0xb6 :
		tempVal = 0x79;
		break;
		case 0xda :
		tempVal = 0x7a;
		break;
		case 0x21 :
		tempVal = 0x7b;
		break;
		case 0x10 :
		tempVal = 0x7c;
		break;
		case 0xff :
		tempVal = 0x7d;
		break;
		case 0xf3 :
		tempVal = 0x7e;
		break;
		case 0xd2 :
		tempVal = 0x7f;
		break;
		case 0xcd :
		tempVal = 0x80;
		break;
		case 0x0c :
		tempVal = 0x81;
		break;
		case 0x13 :
		tempVal = 0x82;
		break;
		case 0xec :
		tempVal = 0x83;
		break;
		case 0x5f :
		tempVal = 0x84;
		break;
		case 0x97 :
		tempVal = 0x85;
		break;
		case 0x44 :
		tempVal = 0x86;
		break;
		case 0x17 :
		tempVal = 0x87;
		break;
		case 0xc4 :
		tempVal = 0x88;
		break;
		case 0xa7 :
		tempVal = 0x89;
		break;
		case 0x7e :
		tempVal = 0x8a;
		break;
		case 0x3d :
		tempVal = 0x8b;
		break;
		case 0x64 :
		tempVal = 0x8c;
		break;
		case 0x5d :
		tempVal = 0x8d;
		break;
		case 0x19 :
		tempVal = 0x8e;
		break;
		case 0x73 :
		tempVal = 0x8f;
		break;
		case 0x60 :
		tempVal = 0x90;
		break;
		case 0x81 :
		tempVal = 0x91;
		break;
		case 0x4f :
		tempVal = 0x92;
		break;
		case 0xdc :
		tempVal = 0x93;
		break;
		case 0x22 :
		tempVal = 0x94;
		break;
		case 0x2a :
		tempVal = 0x95;
		break;
		case 0x90 :
		tempVal = 0x96;
		break;
		case 0x88 :
		tempVal = 0x97;
		break;
		case 0x46 :
		tempVal = 0x98;
		break;
		case 0xee :
		tempVal = 0x99;
		break;
		case 0xb8 :
		tempVal = 0x9a;
		break;
		case 0x14 :
		tempVal = 0x9b;
		break;
		case 0xde :
		tempVal = 0x9c;
		break;
		case 0x5e :
		tempVal = 0x9d;
		break;
		case 0x0b :
		tempVal = 0x9e;
		break;
		case 0xdb :
		tempVal = 0x9f;
		break;
		case 0xe0 :
		tempVal = 0xa0;
		break;
		case 0x32 :
		tempVal = 0xa1;
		break;
		case 0x3a :
		tempVal = 0xa2;
		break;
		case 0x0a :
		tempVal = 0xa3;
		break;
		case 0x49 :
		tempVal = 0xa4;
		break;
		case 0x06 :
		tempVal = 0xa5;
		break;
		case 0x24 :
		tempVal = 0xa6;
		break;
		case 0x5c :
		tempVal = 0xa7;
		break;
		case 0xc2 :
		tempVal = 0xa8;
		break;
		case 0xd3 :
		tempVal = 0xa9;
		break;
		case 0xac :
		tempVal = 0xaa;
		break;
		case 0x62 :
		tempVal = 0xab;
		break;
		case 0x91 :
		tempVal = 0xac;
		break;
		case 0x95 :
		tempVal = 0xad;
		break;
		case 0xe4 :
		tempVal = 0xae;
		break;
		case 0x79 :
		tempVal = 0xaf;
		break;
		case 0xe7 :
		tempVal = 0xb0;
		break;
		case 0xc8 :
		tempVal = 0xb1;
		break;
		case 0x37 :
		tempVal = 0xb2;
		break;
		case 0x6d :
		tempVal = 0xb3;
		break;
		case 0x8d :
		tempVal = 0xb4;
		break;
		case 0xd5 :
		tempVal = 0xb5;
		break;
		case 0x4e :
		tempVal = 0xb6;
		break;
		case 0xa9 :
		tempVal = 0xb7;
		break;
		case 0x6c :
		tempVal = 0xb8;
		break;
		case 0x56 :
		tempVal = 0xb9;
		break;
		case 0xf4 :
		tempVal = 0xba;
		break;
		case 0xea :
		tempVal = 0xbb;
		break;
		case 0x65 :
		tempVal = 0xbc;
		break;
		case 0x7a :
		tempVal = 0xbd;
		break;
		case 0xae :
		tempVal = 0xbe;
		break;
		case 0x08 :
		tempVal = 0xbf;
		break;
		case 0xba :
		tempVal = 0xc0;
		break;
		case 0x78 :
		tempVal = 0xc1;
		break;
		case 0x25 :
		tempVal = 0xc2;
		break;
		case 0x2e :
		tempVal = 0xc3;
		break;
		case 0x1c :
		tempVal = 0xc4;
		break;
		case 0xa6 :
		tempVal = 0xc5;
		break;
		case 0xb4 :
		tempVal = 0xc6;
		break;
		case 0xc6 :
		tempVal = 0xc7;
		break;
		case 0xe8 :
		tempVal = 0xc8;
		break;
		case 0xdd :
		tempVal = 0xc9;
		break;
		case 0x74 :
		tempVal = 0xca;
		break;
		case 0x1f :
		tempVal = 0xcb;
		break;
		case 0x4b :
		tempVal = 0xcc;
		break;
		case 0xbd :
		tempVal = 0xcd;
		break;
		case 0x8b :
		tempVal = 0xce;
		break;
		case 0x8a :
		tempVal = 0xcf;
		break;
		case 0x70 :
		tempVal = 0xd0;
		break;
		case 0x3e :
		tempVal = 0xd1;
		break;
		case 0xb5 :
		tempVal = 0xd2;
		break;
		case 0x66 :
		tempVal = 0xd3;
		break;
		case 0x48 :
		tempVal = 0xd4;
		break;
		case 0x03 :
		tempVal = 0xd5;
		break;
		case 0xf6 :
		tempVal = 0xd6;
		break;
		case 0x0e :
		tempVal = 0xd7;
		break;
		case 0x61 :
		tempVal = 0xd8;
		break;
		case 0x35 :
		tempVal = 0xd9;
		break;
		case 0x57 :
		tempVal = 0xda;
		break;
		case 0xb9 :
		tempVal = 0xdb;
		break;
		case 0x86 :
		tempVal = 0xdc;
		break;
		case 0xc1 :
		tempVal = 0xdd;
		break;
		case 0x1d :
		tempVal = 0xde;
		break;
		case 0x9e :
		tempVal = 0xdf;
		break;
		case 0xe1 :
		tempVal = 0xe0;
		break;
		case 0xf8 :
		tempVal = 0xe1;
		break;
		case 0x98 :
		tempVal = 0xe2;
		break;
		case 0x11 :
		tempVal = 0xe3;
		break;
		case 0x69 :
		tempVal = 0xe4;
		break;
		case 0xd9 :
		tempVal = 0xe5;
		break;
		case 0x8e :
		tempVal = 0xe6;
		break;
		case 0x94 :
		tempVal = 0xe7;
		break;
		case 0x9b :
		tempVal = 0xe8;
		break;
		case 0x1e :
		tempVal = 0xe9;
		break;
		case 0x87 :
		tempVal = 0xea;
		break;
		case 0xe9 :
		tempVal = 0xeb;
		break;
		case 0xce :
		tempVal = 0xec;
		break;
		case 0x55 :
		tempVal = 0xed;
		break;
		case 0x28 :
		tempVal = 0xee;
		break;
		case 0xdf :
		tempVal = 0xef;
		break;
		case 0x8c :
		tempVal = 0xf0;
		break;
		case 0xa1 :
		tempVal = 0xf1;
		break;
		case 0x89 :
		tempVal = 0xf2;
		break;
		case 0x0d :
		tempVal = 0xf3;
		break;
		case 0xbf :
		tempVal = 0xf4;
		break;
		case 0xe6 :
		tempVal = 0xf5;
		break;
		case 0x42 :
		tempVal = 0xf6;
		break;
		case 0x68 :
		tempVal = 0xf7;
		break;
		case 0x41 :
		tempVal = 0xf8;
		break;
		case 0x99 :
		tempVal = 0xf9;
		break;
		case 0x2d :
		tempVal = 0xfa;
		break;
		case 0x0f :
		tempVal = 0xfb;
		break;
		case 0xb0 :
		tempVal = 0xfc;
		break;
		case 0x54 :
		tempVal = 0xfd;
		break;
		case 0xbb :
		tempVal = 0xfe;
		break;
		case 0x16 :
		tempVal = 0xff;
		break;
	}
	return tempVal;
}