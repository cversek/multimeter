/*
  MCP4801.h - Library for interacting with the Microchip MCP4801 
              8-Bit Voltage Output Digital-to-Analog Converter
              with Internal VREF and SPI Interface.
  Created by Craig Wm. Versek, 2012-05-13
  Released into the public domain.
 */

#ifndef _MCP4801_H_INCLUDED
#define _MCP4801_H_INCLUDED

#include <Arduino.h>
//#include <avr/pgmspace.h>

#define VREF 2.048
#define RES8BIT 256

class MCP4801Class {
public:
  MCP4801Class(int slaveSelectLowPin,
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


#endif //_MCP4801_H_INCLUDED
