from selenium import webdriver
from selenium.webdriver.common.by import By
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
# """ elem3 = browser.find_element_by_name("q")
# elem3.clear()
# elem3.send_keys("sunglasses")
# elem3.send_keys(Keys.RETURN) """

#browser.get('https://www.facebook.com/search/videos/?q=jwelery&epa=SERP_TAB')
browser.get('https://www.facebook.com/search/pages/?q=web hosting company&epa=SERP_TAB')
#browser.get('https://www.facebook.com/Men-Watch-109721994057939/');


# Get scroll height
i=1

while True:
    #print browser.execute_script("return document.body")
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    eles = browser.find_element(By.XPATH, '//*[@id="BrowseResultsContainer"]')

    # e = browser.find_element_by_xpath(//*[@id="u_1a_i"]/div/div[2]/div/div[1]/div[1]/div/div/div/div/a/span)
    print eles.getAttribute("innerHTML")

    i=i+1
    id = uuid.uuid1()

    time.sleep(2.4)
#     if i==10:
#         break

print  browser.page_source



