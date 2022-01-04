import requests
from bs4 import BeautifulSoup
import pandas

nykaa_url='https://www.nykaa.com/makeup/eyes/eyeshadow/c/242?page_no={}&sort=popularity&eq=desktop'
page_num=3

scraped_info_list=[]


for i in range(1,page_num):
    req=requests.get(nykaa_url.format(page_num))
    content = req.content
    
    soup = BeautifulSoup(content, 'html.parser')
    
    all_products = soup.find_all('div',{'class':'css-1ehyqrt'})
    
    
    
    for product in all_products:
        product_dict={}
        product_dict['Name'] = product.find('div',{'class':'css-10zjw4o'}).text
        product_dict['Price'] = product.find('div',{'class':'css-1c4e1zl'}).text
        
        try:
            product_dict['Reviews'] = product.find('div',{'class':'css-y7j3zx'}).text
        except AttributeError:
            pass
        
        try:
            product_dict['Featured'] = product.find('div',{'class':'css-wkluxr'}).text
        except AttributeError:
            pass
        
        scraped_info_list.append(product_dict)
        
dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv('Nykaa.csv')