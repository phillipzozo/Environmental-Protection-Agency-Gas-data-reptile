#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
'''
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'en,zh-TW;q=0.8,zh;q=0.6',
        'Cache-Control':'max-age=0',
        #'Host':'www.xxx.com',   #此處為氣體網站的主頁
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    }
response = requests.get("https://taqm.epa.gov.tw/taqm/tw/default.aspx", headers=headers) #請求的地址
soup = BeautifulSoup(response.content, 'html.parser')  #返回的html信息用soup解析
PM25_text = soup.find(id='lb_PAQIPM25')
print(PM25_text)
#print(response.status_code)  #請求狀態碼
print(soup.prettify())  #以格式輸出html
'''
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver')
#driver.get('https://taqm.epa.gov.tw/taqm/tw/default.aspx')
#driver.maximize_window()


url = 'https://taqm.epa.gov.tw/taqm/tw/default.aspx'
driver.get(url)
title = driver.title
print(title)

iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)

############ get CO value ############
gas_name = '一氧化碳(CO)'
CO_value = driver.find_element_by_id('lb_CO')
print(CO_value.text)
############ get CO value ############

############ get PM2.5 value ############
gas_name = '懸浮微粒(PM2.5)'
PM25_value = driver.find_element_by_id('lb_PM25')
print(PM25_value.text)
############ get PM2.5 value ############

