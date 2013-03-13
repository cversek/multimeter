/*
  HEF4051B_test.ino - Arduino Library Example sketch for the NXP  
                      or Phillips MSI HEF4051B
                      8-channel analogue multiplexer/demultiplexer
  Created by Craig Wm. Versek, 2012-06-04
  Released into the public domain.
*/

#include <HEF4051B.h>

#define DELAY_ms 2000
//configure the PGA chip
HEF4051B_Class MUX(2,3,4,5);   //slaveSelectLowPin


void setup() {
  
  //start controlling the multiplexer
  MUX.begin();
}

void loop() {
  //loop through the gain settings
  delay(DELAY_ms);
}
