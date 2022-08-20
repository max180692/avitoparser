from bs4 import BeautifulSoup as bs
import lxml

class GetUrl:
    def __init__(self):
        self.__list_url = None

    def get_url(self, content):
        soup = bs(content,'lxml')
        self.__list_url = [f"https://m.avito.ru{div.a['href']}" for div in soup.find('div',{'data-marker':'catalog-serp'}).find_all('div',{'data-marker':'item'})]
        print(len(self.__list_url))
        return self.__list_url