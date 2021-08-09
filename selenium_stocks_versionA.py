# -*- coding: utf-8 -*-
"""
Created on Sat jun 5 20:57:51 2021

@author: kwan
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
 
stockList = ['BNB', 'BTC', 'ETH']
len (stockList)
 
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

i = 0

while i <3:
    
   Chrome = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver', chrome_options=options)

   Chrome.get("https://finance.yahoo.com/")

   time.sleep(3)

   SB = Chrome.find_element_by_id('yfin-usr-qry')

   SB.send_keys("{0}".format(stockList[i]))

   time.sleep(5)

   stockPg = SB.send_keys(Keys.RETURN)

   time.sleep(5)
   
   histData = Chrome.find_element(By.XPATH,'//span[text()="Historical Data"]').click()
   
   time.sleep(5)
   
   grabTimePeriod = Chrome.find_element_by_css_selector('[data-icon=CoreArrowDown]').click()
   
   ClickMax = Chrome.find_element_by_css_selector('[data-value="5_Y"]').click() 
   
   #Outdate clickDone= Chrome.find_element(By.XPATH, '//span[text()="Done"]').click()
   
   clickApply = Chrome.find_element(By.XPATH, '//span[text()="Apply"]').click()
   
   downloadData = Chrome.find_element(By.XPATH, '//span[text()="Download"]').click()
   
   time.sleep(5)
   
   Chrome.close()
   
   i +=1
   
   
             

