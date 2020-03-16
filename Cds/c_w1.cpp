/* Requests DS18B20 address, and prints current temperature to terminal.
Requires TeraHz's DS18B20 C++ library from here; https://github.com/TeraHz/DS18B20.git
To compile enter; 
g++ -Wall c_w1.cpp DS18B20.cpp -o run_w1
To run; ./run_w1                                                                                               
*/
#include <iostream>
#include <string>
#include "DS18B20.h"
#include <ctime>
#include <thread>         
#include <chrono>         
using namespace std;

int main() {
    double tempNow;
    char w1_address[16]="28-00000484b7e5";

    while(1){
      DS18B20 w1Device1 (w1_address);
      tempNow = w1Device1.getTemp();
      
      time_t now = time(0);
      char* dt = ctime(&now);
      cout <<dt<<   " T=" << tempNow << " C" <<endl;
      this_thread::sleep_for(std::chrono::seconds(60));
    }

}
