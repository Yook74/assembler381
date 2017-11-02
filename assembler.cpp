/*
Acts as an assembler for the subset of MIPS used in COS 381
Created by Andrew Blomenberg for Computer Architeture 
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main(int argc, char* argv[])
{

	ifstream inFile;
	string line;
	int lineCount=0;

	if (argc<3) 
		return 0;	
	inFile.open(argv[1]);
	
//	cout<<"Crawling";

	while(!inFile.eof())
	{	
		lineCount++;
//		if(lineCount % 10000 ==0)
//			cout<<"."<<flush; //status printed to screen
		

		inFile.ignore(256,','); //config
		inFile>>seconds;
	}		
//	cout<<"Done!"<<endl;
	inFile.close();
}
