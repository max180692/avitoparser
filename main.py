from my_useragent.read_user_agent import UserAgent
from newconnect import GetHtmlPage
from get_url_avito import GetUrl
from generatepages import GeneretePages





def main():
    
    url = 'https://www.avito.ru/gelendzhik/avtomobili/subaru-ASgBAgICAUTgtg2mmSg?cd=1'
    ghp = GetHtmlPage()
    genpages = GeneretePages()
    ghp.open_proxy()
    
    gu = GetUrl()
    source = ghp.get_sourcepage(url)
    
    list_pages  = genpages.generate_pages(ghp,url,source)
    #print(list_pages)
    list_source = []
    for i in range(len(list_pages)):
        for url in gu.get_url(ghp.get_sourcepage(list_pages[i])):
                print('=========================== ',url)
                list_source.append(
                    ghp.get_sourcepage(url,mobile=True,webelement="div.wgLn2")
                )
                print('=========================== ',url)
        

    dict_url = { i:gu.get_url(ghp.get_sourcepage(list_pages[i]))  for i in range(len(list_pages))}
    print(dict_url)

    
    #source = ghp.get_sourcepage(dict_url[0][1],mobile=True,webelement="div.wgLn2")
    #print(source)
    
    

    for k in dict_url:
        print('=========================== ',k)
        source = [ ghp.get_sourcepage(url,mobile=True,webelement="div.wgLn2") for url in dict_url[k]]
        print('+++++++++++++++++++++++++++ ',k)
   
    
    #gu.get_url(source)
    
    
if __name__ == '__main__':
    main()