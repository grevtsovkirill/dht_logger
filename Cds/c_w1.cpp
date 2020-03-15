/* Requests DS18B20 address, and prints current temperature to terminal.
Requires TeraHz's DS18B20 C++ library from here; https://github.com/TeraHz/DS18B20.git
To compile enter; 
g++ -Wall c_w1.cpp DS18B20.cpp -o run_w1
To run; ./DS18B20Test                                                                                                                                                                                             
*/
#include <iostream>
#include <string>
#include "DS18B20.h"
using namespace std;

int main() {
    double tempNow;
    char w1_address[16];

    cout << "Enter 1-Wire device address, including the '28-': ";
    //cin >> w1_address;
    //w1_address="/sys/bus/w1/devices/28-00000484b7e5/w1_slave";
    w1_address="28-00000484b7e5";
    //snprintf(w1_address , "/sys/bus/w1/devices/28-00000484b7e5/w1_slave");
    cout << "The address you entered was " << w1_address << endl;

    DS18B20 w1Device1 (w1_address);
    tempNow = w1Device1.getTemp();

    cout << "The current temperature is " << tempNow << " degrees Celsius" <<endl;

    return 0;
}
