/*
  MCP6S91.cpp - Library for interacting with the Microchip MCP6S91
                Single-Ended, Rail-to-Rail I/O, Low-Gain PGA
  Created by Craig Wm. Versek, 2012-05-18
  Released into the public domain.
 */

#include <SPI.h>
#include "MCP6S91.h"

#define GAIN_SETTING_ERROR -1

MCP6S91Class::MCP6S91Class(int slaveSelectLowPin){
  //initialize the pin mapping
  _slaveSelectLowPin = slaveSelectLowPin;
}

void MCP6S91Class::begin() {
  // Configure the Arduino pins
  pinMode(_slaveSelectLowPin, OUTPUT);
  digitalWrite(_slaveSelectLowPin, HIGH);  //comm. off
}

void MCP6S91Class::end() {
  //turn all pins off
  digitalWrite(_slaveSelectLowPin, LOW);
}

int MCP6S91Class::setGain(int gain){
  word packet = 0;
  byte gain_bits = 0;

  switch(gain){
    case 1:
      gain_bits = B000;
      break;
    case 2:
      gain_bits = B001;
      break;
    case 4:
      gain_bits = B010;
      break;
    case 5:
      gain_bits = B011;
      break;
    case 8:
      gain_bits = B100;
      break;
    case 10:
      gain_bits = B101;
      break;
    case 16:
      gain_bits = B110;
      break;
    case 32:
      gain_bits = B111;
      break;
    default:
      return GAIN_SETTING_ERROR;
  }
  
  packet  = 1 << 14;           //specify "write to register" command
  packet |= gain_bits;         //select gain
  
  digitalWrite(_slaveSelectLowPin, LOW);   //set chip as listener
  SPI.transfer(highByte(packet));          //send packet
  SPI.transfer(lowByte(packet));
  digitalWrite(_slaveSelectLowPin, HIGH);  //release chip select
  
  return 0;
}
