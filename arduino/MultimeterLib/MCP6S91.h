/*
  MCP6S91.h - Library for interacting with the Microchip MCP6S91
              Single-Ended, Rail-to-Rail I/O, Low-Gain PGA
  Created by Craig Wm. Versek, 2012-05-18
  Released into the public domain.
 */

#ifndef _MCP6S91_H_INCLUDED
#define _MCP6S91_H_INCLUDED

#include <Arduino.h>
//#include <avr/pgmspace.h>


class MCP6S91Class {
public:
  MCP6S91Class(int slaveSelectLowPin);
  //Configuration methods
  void begin(); // Default
  void end();
  //Functionality methods
  int setGain(int gain);
private:
  int _slaveSelectLowPin;
};


#endif //_MCP6S91_H_INCLUDED
