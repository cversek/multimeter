################################################################################
#  chip.py - class for handling information about integrated circuits 
#  Created by Craig Wm. Versek, 2012-05-27
#  Released into the public domain.
################################################################################
import re
import unicodedata
from collections import OrderedDict

from chipselect.component import Component

class Chip(Component):
    def __init__(self, 
                 mfg_partnumber, 
                 mfg_desc,
                 package,
                 pins,
                 info         = None, 
                 categories   = None, 
                 distributors = None,
                ):
        Component.__init__(self,
                           mfg_partnumber = mfg_partnumber, 
                           mfg_desc       = mfg_desc,
                           info           = info, 
                           categories     = categories, 
                           distributors   = distributors
                          )
        self.package = package
        self.pins    = int(pins) 
        self.categories.add('IC')

    def keywords(self):
        "return a set of keywords that can be used to search for this component"
        kws = Component.keywords(self)
        kws.add(self.package)
        return kws
        
################################################################################
# TEST CODE
################################################################################
if __name__ == "__main__":
    c1 = Chip('MCP4801-E/P', 
              'MICROCHIP - MCP4801-E/P - IC, DAC, 8BIT, DIP-8',
               package = 'DIP',
               pins = 8,
               categories = ['Digital to Analog Converter']
             ) 
