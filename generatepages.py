from bs4 import BeautifulSoup as bs


class GeneretePages:

    def __init__(self):
        self.__ghp = None
    
    def generate_pages(self,ghp,url,source):
        self.__ghp = ghp
        if source:
            soup = bs(source,'lxml')
            list_pages = [url + f'&p={i}'  for i in range(1,int(soup.select('span.pagination-item-JJq_j')[-2].text) + 1)]
            return list_pages
        
        self.repeat_connect()

    def repeat_connect(self):
        self.__ghp.get_sourcepage()
        
