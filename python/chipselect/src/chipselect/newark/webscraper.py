import urllib
import urllib2
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import HTMLParser     # html.parser in Python 3
import unicodedata


from collections import OrderedDict
from BeautifulSoup import BeautifulSoup

USER_AGENT  = ''
BASE_URL    = "http://www.newark.com"
SEARCH_PAGE = 'jsp/search/browse.jsp'

HTML_PARSER = HTMLParser.HTMLParser()

def unescape_html(text):
    return HTML_PARSER.unescape(text)
    
def clean_text(text):
    text = unescape_html(text)
    text = unicode(text)
    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    return text

class WebScraper(object):
    def __init__(self, 
                 user_agent = USER_AGENT, 
                 base_url = BASE_URL, 
                 search_page = SEARCH_PAGE
                ):
        self.user_agent = USER_AGENT
        self.base_url   = BASE_URL
        self.search_page = SEARCH_PAGE
        #Create a CookieJar object to hold the cookies
        self.cookie_jar = cookielib.CookieJar()
        #Create an opener to open pages using the http protocol and to process cookies.
        self.http_opener = build_opener(HTTPCookieProcessor(self.cookie_jar), HTTPHandler())
        self.http_opener.addheaders = [('User-agent', self.user_agent)]

        

    def cookie_match(self, attr, value = None):
        matching_cookies = []
        for cookie in self.cookie_jar:
            if hasattr(cookie,attr):
                if getattr(cookie, attr, None) == value:
                    matching_cookies.append(cookie)
        return matching_cookies
        
    def home_page(self):
        headers = { 'User-Agent' : self.user_agent}
        values = OrderedDict()
        #values['_requestid'] = 161352
        data = urllib.urlencode(values)
        request = Request(self.base_url, data, headers)
        response = self.http_opener.open(request)
        the_page = response.read()
        soup = BeautifulSoup(the_page)
        return soup
        
    def scrape_product_page(self,url):
        headers = { 'User-Agent' : self.user_agent}
        values = OrderedDict()
        data = urllib.urlencode(values)
        request = Request(url, data, headers)
        response = self.http_opener.open(request)
        the_page = response.read()
        #scrape information
        soup = BeautifulSoup(the_page)
        info = OrderedDict()
        #sweep up the breadcrumbs
        div_tag = soup.find(id='breadcrumbs_hidden')
        li_tag  = div_tag.findNext('li')
        breadcrumbs = []
        for sib in li_tag.findNextSiblings('li'):
            a_tag = sib.a
            if not a_tag is None:
                text = clean_text(a_tag.text)
                breadcrumbs.append(text)
        info['breadcrumbs'] = breadcrumbs
        info['mfg_desc']    = clean_text(soup.h1.text)
        #scrape the product details
        dl_tag = soup.find('dl', attrs={'class':"pd_details"})
        dt_tags = dl_tag.findChildren('dt')
        dd_tags = dl_tag.findChildren('dd')
        info['mfg']                 = clean_text(dd_tags[0].text) 
        info['newark_partnumber']   = clean_text(dd_tags[1].text)
        info['mfg_partnumber']      = clean_text(dd_tags[2].text)
        info['datasheet_link']      = dd_tags[3].a.get('href')
        #scrape more product information
        div_tag = soup.find('div', attrs={'class':"pdInformation"})
        ul_tag   = div_tag.findChild('ul',attrs={'class':"bull"})
        span_tag = ul_tag.findChild('span',attrs={'class':"prodAttrSingle"})
        prod_info = OrderedDict()
        prod_info['keywords'] = clean_text(span_tag.text).split(',')
        span_tags1 = ul_tag.findChildren('span',attrs={'class':"prodAttrName"}) 
        span_tags2 = ul_tag.findChildren('span',attrs={'class':"prodAttrValue"})
        for st1, st2 in zip(span_tags1,span_tags2): 
            name = clean_text(st1.text).strip(":")
            val  = clean_text(st2.text)
            prod_info[name] = val
        info['product_information'] = prod_info
        #scrape availability and pricing information
        div_tag = soup.find('div', attrs={'class':"availability"})
        div_tag = div_tag.findChild('div', attrs={'class':"stockDetail"})
        info['availability'] = clean_text(div_tag.text)
        div_tag = soup.find('div', attrs={'class':"price"})
        price_table = OrderedDict()
        table_tag = div_tag.table
        tr_tags   = table_tag.findChildren('tr')
        for tr_tag in tr_tags[1:-1]: #skip the first and last rows
            td_tags = tr_tag.findChildren('td')
            key = clean_text(td_tags[0].text).strip()
            val = clean_text(td_tags[1].text).strip()
            price_table[key] = val
        info['price_table'] = price_table
        return info
        
    def product_search(self, query):
        headers = { 'User-Agent' : self.user_agent}
        #extract the session ID from the cookies
        cookies = self.cookie_match('name', 'JSESSIONID')
        if len(cookies) == 0: #matching cookie not found
            #try going to the homepage
            self.home_page()
            cookies = self.cookie_match('name', 'JSESSIONID')
        jsessionid = cookies[0].value    
        url = '/'.join((self.base_url,self.search_page))
        url += ";jsessionid=%s?" % jsessionid
        #load up the request
        values = OrderedDict()
        values['N']   = 422
        values['Ntk'] = 'gensearch' 
        values['Ntt'] = query
        values['Ntx'] = 'mode+matchallpartial'
        values['exposeLevel2Refinement'] = 'true'
        values['suggestions'] = 'false'
        values['ref'] = 'globalsearch'
        #values['_requestid'] = 161352
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data, headers)
        print url
        print "request:", request
        response = urllib2.urlopen(request)
        print "response:", response
        the_page = response.read()
        print "the_page:", the_page
        pool = BeautifulSoup(the_page)
        return pool
        
        
################################################################################
#
################################################################################
if __name__ == "__main__":
    WS = WebScraper()
