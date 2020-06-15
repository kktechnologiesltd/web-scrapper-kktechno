from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import uuid
browser = webdriver.Firefox()
browser.get('https://facebook.com')
elem = browser.find_element_by_name("email")
elem.clear()
elem.send_keys("<fb_email>")

elem2 = browser.find_element_by_name("pass")
elem2.clear()
elem2.send_keys("<fb_password>")
elem2.send_keys(Keys.RETURN)

time.sleep(2.4)


browser.get('https://www.facebook.com/pg/Golden-Life-Fashion-Light-House-1346537318758044/posts/?ref=page_internal')

i=1

while True:
    #print browser.execute_script("return document.body")
    #browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    eles = browser.find_element(By.XPATH, '//*[@id="content_container"]')
    print eles.get_attribute("innerHTML")



    if i==10:
        id = uuid.uuid1()
        f = open("./contents/pages/"+id.hex+".txt", 'w')
        f.write( eles.get_attribute("innerHTML").encode('ascii', 'ignore'))
        f.close()
        print  browser.page_source

    time.sleep(2.4)
    i=i+1
#     if i==10:
#         break




