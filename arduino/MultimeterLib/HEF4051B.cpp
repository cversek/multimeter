/*
  HEF4051B.cpp - Library for interacting with the the NXP or 
                 Phillips MSI HEF4051B 8-channel analogue 
                 multiplexer/demultiplexer
  Created by Craig Wm. Versek, 2012-06-04
  Released into the public domain.
 */

#include <HEF4051B.h>

#define CHANNEL_SETTING_ERROR -1
#define SWITCH_DELAY_MICROSECONDS 1

HEF4051BClass::HEF4051BClass(int address0Pin, 
                             int address1Pin, 
                             int address2Pin, 
                             int enableLowPin
                            ){
  //initialize the pin mapping
  _address0Pin  = address0Pin; 
  _address1Pin  = address1Pin; 
  _address2Pin  = address2Pin; 
  _enableLowPin = enableLowPin;
}

void HEF4051BClass::begin() {
  // Configure the Arduino pins
  pinMode(_address0Pin, OUTPUT);
  pinMode(_address1Pin, OUTPUT);
  pinMode(_address2Pin, OUTPUT);
  pinMode(_enableLowPin, OUTPUT);
  switchAllOff();
}

void HEF4051BClass::end() {
  //turn all channels off
  switchAllOff();
}

int HEF4051BClass::switchChannel(int chan){
  if( (chan >= 0) && (chan <= 7)){
    digitalWrite(_enableLowPin, HIGH);
    delayMicroseconds(SWITCH_DELAY_MICROSECONDS);
    digitalWrite(_address0Pin, chan & B001);
    digitalWrite(_address1Pin, chan & B010);
    digitalWrite(_address2Pin, chan & B100);
    delayMicroseconds(SWITCH_DELAY_MICROSECONDS);
    digitalWrite(_enableLowPin, LOW);
    return chan;
  }
  else{ 
    switchAllOff();
    return CHANNEL_SETTING_ERROR;
  }
}

void HEF4051BClass::switchAllOff(){
  digitalWrite(_enableLowPin, HIGH);
  delayMicroseconds(SWITCH_DELAY_MICROSECONDS);
  digitalWrite(_address0Pin, LOW);
  digitalWrite(_address1Pin, LOW);
  digitalWrite(_address2Pin, LOW);   
}
