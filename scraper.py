import requests
import lxml.html as html

XPATH_LINK_TO_ARTICLE = '//div[@class="html-content"]/p/descendant-or-self::text()'
XPATH_TITLE= '//div[@class="html-content"]/p/descendant-or-self::text()'
XPATH_DATE= '//span[@class="date"]/text()'
XPATH_LEAD= '//div[@class="lead"]/p/text()'
XPATH_BODY= '//div[@class="html-content"]/p/descendant-or-self::text()'

def parse_home():
    pass

def run():
    parse_home()

if __name__=='__main__':
    run()