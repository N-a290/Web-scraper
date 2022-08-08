import requests
import lxml.html as html
import os
import datetime

HOME= 'https://www.larepublica.co'

XPATH_LINK_TO_ARTICLE = '//text-fill[not(@class)]/a/@href'
XPATH_TITLE='//div[@class="mb-auto"]/descendant-or-self::text()'
XPATH_DATE= '//span[@class="date"]/text()'
XPATH_LEAD= '//div[@class="lead"]/p/text()'
XPATH_BODY= '//div[@class="html-content"]/p/descendant-or-self::text()'

def parse_notice(link,today):
    try:
        response= requests.get(link)
        if response.status_code == 200:
            notice= response.content.decode('utf-8')
            parsed= html.fromstring(notice)
            try:
                title= parsed.xpath(XPATH_TITLE)[4]
                title= title.replace('\"','').strip()
                date= parsed.xpath(XPATH_DATE)[0]
                summary= parsed.xpath(XPATH_LEAD)[0]
                body= parsed.xpath(XPATH_BODY)
                

            except IndexError:
                return

            with open(f'07-08-2022/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(date)
                f.write('\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}. Sucedó un error llamando un link')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response= requests.get(HOME)
        if response.status_code == 200:
            home= response.content.decode('utf-8')
            parsed= html.fromstring(home)
            links_article= parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #print(links_article)
            
            today= datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)
                
            for link in links_article:
                parse_notice(link,today)
        else:
            raise ValueError(f"Error: {response.status_code}. No se pudo llamar los links de la página")
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__=='__main__':
    run()