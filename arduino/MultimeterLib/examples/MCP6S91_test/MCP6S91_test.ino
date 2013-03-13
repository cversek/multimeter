/*
  MCP6S91_test.ino - Arduino Library Example sketch for the Microchip MCP6S91 
                     Single-Ended, Rail-to-Rail I/O, Low-Gain PGA
  Created by Craig Wm. Versek, 2012-05-18
  Released into the public domain.
*/

#include <SPI.h>
#include <MCP6S91.h>

#define DELAY_ms  2000
#define NUM_GAINS 8

//these are ALL the valid gain settings
const int GAINS[NUM_GAINS] = {1,2,4,5,8,10,16,32}; 

//configure the PGA chip
MCP6S91Class PGA(7);   //slaveSelectLowPin


void setup() {
  //start up the SPI bus                   
  SPI.begin();
  SPI.setBitOrder(MSBFIRST);
  SPI.setDataMode(SPI_MODE0);
  //start controlling the amplifier
  PGA.begin();
}

void loop() {
  //loop through the gain settings
  for (int i=0; i < NUM_GAINS; i++){
    int gain = GAINS[i];
    PGA.setGain(gain);
    delay(DELAY_ms);
  }  
}
