import requests
import lxml.html as html
import os
import datetime


HOME_URL = 'https://www.larepublica.co/'


XPATH_LINK_TO_ARTICLE = '//div[contains(@class, "V")]/a[contains(@class, "kicker")]/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class = "lead"]/p/text()'
XPATH_BODY = '//div[@class = "html-content"]/p[not (@class)]/text()'

def parse_home():
    # Creamos un bloque try para manejar los errores. Y manejar los Status Code.
    try:
        response = requests.get(HOME_URL)
         # Aqui va la lógica para traer los links.
        
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            # .content trae  el HTML que necesita ser traducido con un decode para que python lo entienda
            # en terminos de caracteres, me devuelve un string que noes más que el HTML crudo.
            
            
            # En esta línea estoy usando el archivo parseado con la función xpath y le paso por parámetro mi constante
            # la cual almacena la expresión Xpath.
    
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(len(links_to_notices))
            print(links_to_notices)
            
        else:
            raise ValueError(f"Error: {response.status_code}")
        #Elevamos el error para ser capturado en el try-except, too lo que sea un error.


    except ValueError as ve: 
        print(ve)

def main():
    parse_home()

if __name__ == '__main__':
    main()