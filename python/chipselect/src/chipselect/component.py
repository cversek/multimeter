################################################################################
#  component.py - class for handling information about cicuit components
#  Created by Craig Wm. Versek, 2012-05-27
#  Released into the public domain.
################################################################################
from collections import OrderedDict

from chipselect.search import keywordize


class Component(object):
    def __init__(self, 
                 mfg_partnumber, 
                 mfg_desc,
                 info         = None, 
                 categories   = None, 
                 distributors = None,
                ):
        self.mfg_partnumber = mfg_partnumber
        self.mfg_desc       = unicode(mfg_desc)
        if info  is None:
            info  = OrderedDict()
        self.info = OrderedDict(info)
        if categories is None:
            categories = set()
        self.categories = set(categories)
        if distributors is None:
            distributors = {}
        self.distributors = dict(distributors)
    def keywords(self):
        "return a set of keywords that can be used to search for this component"
        kws = set()
        #add the whole partnumber
        kws.add(self.mfg_partnumber)
        #decompose the partnumber on hyphens
        kws.update(self.mfg_partnumber.split('-'))
        #break up the description into words
        kws.update(keywordize(self.mfg_desc))
        #add info fields and values to keywords
        for key,val in self.info.items():
            kws.update(keywordize(key))
            kws.update(keywordize(val))
        #add categories
        for cat in self.categories:
            kws.update(keywordize(cat))
        return kws

################################################################################
# TEST CODE
################################################################################
if __name__ == "__main__":
    c1 = Component('MCP4801-E/P', 
                   'MICROCHIP - MCP4801-E/P - IC, DAC, 8BIT, DIP-8',
                   categories = ['Digital to Analog Converter']
                  ) 
