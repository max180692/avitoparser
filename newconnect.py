from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import lxml
from my_useragent.read_user_agent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium




class GetHtmlPage:
    def __init__(self):
        self.__options = None
        self.__ua = UserAgent()
        self.__start_cicle = True
        self.__lst_proxy = None
        self.__proxy = None
        self.__url = None

    def open_proxy(self):
        with open('proxy5000.txt','r') as file:
            self.__lst_proxy = file.readlines()
        

    def __setpropertise(self,mobile):
        
        window = '1280,800'
        
        if mobile:
            window = '400,500'
        
        '''
        PROXY=self.__lst_proxy.pop(0).replace('\n','')
        print(PROXY)
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "proxyType": "MANUAL",

        }

        webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
        '''
        self.__options = webdriver.ChromeOptions()
        
        print(self.__ua.get_user_agent(mobile=mobile))
        prefs = {'profile.default_content_setting_values': {'images': 2,'javascript': 2}}
        self.__options.add_experimental_option('prefs', prefs)
        self.__options.add_argument(f"window-size={window}")
        self.__options.add_argument('--headless')
        #self.__options.add_argument('--no-sandbox')
        self.__options.add_argument('--disable-dev-shm-usage')
        self.__options.add_argument('--disable-blink-features=AutomationControlled')
        self.__options.add_argument("--ignore-certificate-errors")
        self.__options.add_argument("--disable-gpu")
        self.__options.add_argument("--dns-prefetch-disable")
        self.__options.add_argument("--disable-extensions")
        self.__options.add_argument(f'user-agent={self.__ua.get_user_agent(mobile=mobile)}')
        #self.__options.add_argument('--proxy-server=188.254.0.59:80')

    def get_sourcepage(self,url=None,mobile=False,webelement=None):
        if url:
            self.__url = url
            self.__setpropertise(mobile)
            CROMEPATH = 'selen\chromedriver.exe'
            driver = webdriver.Chrome(CROMEPATH,options=self.__options)
            driver.get(url)
            try:
                div_element = ".index-content-_KxNP"
                if webelement:
                    div_element = webelement
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, div_element)))
                if element:
                    elements = element.get_attribute('outerHTML')
                    #print(elements)
                    driver.quit()
                    return elements
            except selenium.common.exceptions.TimeoutException:
                self.get_sourcepage(url,mobile)
            except selenium.common.exceptions.WebDriverException:
                self.get_sourcepage(url,mobile)
            except :
                self.get_sourcepage(url,mobile)
        else:
            url = self.__url
            self.get_sourcepage(url,mobile)
        
        
        '''
        try:
            driver.get(url)
            source_page = driver.page_source
            driver.close()
            return source_page
        except:
            self.get_sourcepage(url,mobile)
        '''