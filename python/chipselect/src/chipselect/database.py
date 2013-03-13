################################################################################
#  database.py - database for components 
#  Created by Craig Wm. Versek, 2012-05-27
#  Released into the public domain.
################################################################################
import shelve

from chipselect.search import keywordize

class Database(object):
    def __init__(self, filepath):
        self.db = shelve.open(filepath)
        self.keyword_index      = self.db.get('keyword_index',{})
        self.components         = self.db.get('components',[])
        self.components_lookup  = self.db.get('components_lookup',{})
        
    def add_component(self, component):
        lookup_key = component.mfg_partnumber
        id_num     = len(self.components)
        #enter the component into the database
        self.components.append(component)
        self.components_lookup[lookup_key] = id_num
        #update the keyword index
        kws = component.keywords()
        for kw in kws:
            index = self.keyword_index.get(kw,set()) #start a new index if it doesn't already exist
            index.add(id_num)
            self.keyword_index[kw] = index
            
    def search(self, query):
        components = self.components
        kws = keywordize(query)
        hits = []
        for kw in kws:
            index = self.keyword_index.get(kw,set())
            hits.extend(list(index))
        found   = list(set(hits))
        counts  = [hits.count(c) for c in found]
        results = zip(counts,found)
        results.sort()
        results = [components[r[1]] for r in results]
        return results
    def __del__(self):
        self.db.close()
        
        

################################################################################
# TEST CODE
################################################################################
if __name__ == "__main__":
    from chipselect.chip import Chip
    DB = Database('test.db')
    c1 = Chip('MCP4801-E/P', 
              'MICROCHIP - MCP4801-E/P - IC, DAC, 8BIT, DIP-8',
               package = 'DIP',
               pins = 8,
               categories = ['Digital to Analog Converter']
             ) 
    c2 = Chip('MCP4901-E/P', 
              'MICROCHIP - MCP4901-E/P - IC, DAC, 8BIT, DIP-8 ',
               package = 'DIP',
               pins = 8,
               categories = ['Digital to Analog Converter']
             )
    print "keyword index:", DB.keyword_index
    DB.add_component(c1)
    print "keyword index:", DB.keyword_index
    DB.add_component(c2)
    print "keyword index:", DB.keyword_index
