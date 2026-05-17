/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <cstdlib>
#include <ctime>
using std::cout;
using std::cin;
using std::endl;

void revisarTemperatura(int temperatura){
    cout<<"revisando temperatura. Temperatura actual "<<temperatura<<"Cº"<<endl;
    if(temperatura >= 30){
        cout<<"Alerta temperatura alta"<<endl;
    }
    else{
        cout<<"temperatura normal"<<endl;
    }
}


int main()
{
   srand(time(0));
   int tempSimulada1 = (rand()%26) + 15;
   int tempSimulada2 = (rand()%26) + 15;
   revisarTemperatura(tempSimulada1);
   revisarTemperatura(tempSimulada2);

    return 0;
}