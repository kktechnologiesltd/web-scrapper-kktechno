from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import uuid
browser = webdriver.Chrome()
browser.get('https://facebook.com')
elem = browser.find_element_by_name("email")
elem.clear()
elem.send_keys("01758403758")

elem2 = browser.find_element_by_name("pass")
elem2.clear()
elem2.send_keys("kandksons")
elem2.send_keys(Keys.RETURN)

time.sleep(2.4)
elem3 = browser.find_element_by_name("q")
elem3.clear()
elem3.send_keys("reporters")
elem3.send_keys(Keys.RETURN)

#browser.get('https://www.facebook.com/search/videos/?q=jwelery&epa=SERP_TAB')
browser.get('https://www.facebook.com/search/pages/?q=raspberry pi&epa=SERP_TAB')
#browser.get('https://www.facebook.com/Men-Watch-109721994057939/');


# Get scroll height
i=1

while True:
    #print browser.execute_script("return document.body")
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    print  browser.page_source


    i=i+1
    id = uuid.uuid1()
    f = open("./contents/"+id.hex+".txt", 'w')
    f.write( browser.page_source.encode('ascii', 'ignore'))
    f.close()
    time.sleep(2.4)
#     if i==10:
#         break




