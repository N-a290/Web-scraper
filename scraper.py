import requests
import lxml.html as html

HOME= 'https://www.larepublica.co'

XPATH_LINK_TO_ARTICLE = '//text-fill[not(@class)]/a/@href'
XPATH_TITLE= '//div[@class="html-content"]/p/descendant-or-self::text()'
XPATH_DATE= '//span[@class="date"]/text()'
XPATH_LEAD= '//div[@class="lead"]/p/text()'
XPATH_BODY= '//div[@class="html-content"]/p/descendant-or-self::text()'

def parse_home():
    try:
        response= requests.get(HOME)
        if response.status_code == 200:
            home= response.content.decode('utf-8')
            parsed= html.fromstring(home)
            links_article= parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_article)
        else:
            raise ValueError(f"Error: {response.status_code}")
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__=='__main__':
    run()