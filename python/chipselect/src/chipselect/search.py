################################################################################
#  search.py - utilities for searching component database 
#  Created by Craig Wm. Versek, 2012-05-27
#  Released into the public domain.
################################################################################
import re
import unicodedata
from collections import OrderedDict

KEYWORD_REGEX = re.compile("[a-zA-Z0-9_]+")

def keywordize(text):
    #convert unicode text
    text = unicode(text)
    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    matches  = re.finditer(KEYWORD_REGEX, text)
    kws  = ( m.group(0).upper() for m in matches )
    return kws
    


################################################################################
# TEST CODE
################################################################################
if __name__ == "__main__":
    pass
