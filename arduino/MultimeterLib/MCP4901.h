/*
  MCP4901.h - Library for interacting with the Microchip MCP4901 
              8-Bit Voltage Output Digital-to-Analog Converter
              with SPI Interface.
  Created by Craig Wm. Versek, 2012-05-13
  Released into the public domain.
 */

#ifndef _MCP4901_H_INCLUDED
#define _MCP4901_H_INCLUDED

#include <Arduino.h>
//#include <avr/pgmspace.h>

#define VREF 2.048
#define RES8BIT 256

class MCP4901Class {
public:
  MCP4901Class(int slaveSelectLowPin,
               int ldacLowPin,
               int shutdownLowPin
              );
  //Configuration methods
  void begin(); // Default
  void end();
  //Functionality methods
  int setVoltageOutput(float voltage);
private:
  int _shutdownLowPin;
  int _slaveSelectLowPin;
  int _ldacLowPin;
};


#endif //_MCP4901_H_INCLUDED
