/*
  HEF4051B.h - Library for interacting with the the NXP or Phillips MSI HEF4051B
               8-channel analogue multiplexer/demultiplexer
  Created by Craig Wm. Versek, 2012-06-04
  Released into the public domain.
 */

#ifndef _HEF4051B_H_INCLUDED
#define _HEF4051B_H_INCLUDED

#include <Arduino.h>
//#include <avr/pgmspace.h>


class HEF4051BClass {
public:
  HEF4051BClass(int address0Pin, 
                int address1Pin, 
                int address2Pin, 
                int enableLowPin
               );
  //Configuration methods
  void begin(); // Default
  void end();
  //Functionality methods
  int  getState();
  int  switchChannel(int chan);
  void switchAllOff();
private:
  int _address0Pin; 
  int _address1Pin; 
  int _address2Pin; 
  int _enableLowPin;
  int _state;
};


#endif //_HEF4051B_H_INCLUDED
