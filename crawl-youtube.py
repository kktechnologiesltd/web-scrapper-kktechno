from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import uuid
import redis
import datetime
import threading
import schedule
# browser = webdriver.Firefox()
# browser.get('https://www.youtube.com/results?search_query=fitness&sp=CAESAhAC')
# i=1
# r = redis.Redis()
# count = -1

# while(True):

#     #names = browser.find_element(By.CSS_SELECTOR,"ytd-channel-name")
#     names = browser.find_elements_by_xpath('//div[contains(@class, "ytd-channel-name")]')
#     info = browser.find_elements_by_xpath('//div[contains(@class, "ytd-channel-renderer")]')
#     d = [["1","1"]]
#     j = 0
#     for n in names:
#         val = info[j].text.encode("ascii", "replace").replace(u'\xe2','a')
        
#         visitors = (n.text, val)
#         today = datetime.date.today()
#         stoday = today.isoformat() 
#         if len(n.text) > 5:
#             r.sadd(stoday,*visitors)
#             print(stoday,n.text,val)
#         j = j +1 
        


#     browser.execute_script("return document.body")
#     browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2.4)
#     print d    
#     i=i+1
def setTopics():
    r = redis.Redis()
    r.set("topic_1","fitness")
    r.set("topic_2","health")
    r.set("topic_2","gym")
    r.set("topic_2","weight loss")

def crawl():
    r = redis.Redis()
    setTopics()
    key = r.randomkey()
    print key
    topic = r.get(key)
    browser = webdriver.Firefox()
    browser.get('https://www.youtube.com/results?search_query='+topic+'&sp=CAESAhAC')
    i=1
    
    count = -1
    
    while(True):
 
        #names = browser.find_element(By.CSS_SELECTOR,"ytd-channel-name")
        names = browser.find_elements_by_xpath('//div[contains(@class, "ytd-channel-name")]')
        info = browser.find_elements_by_xpath('//div[contains(@class, "ytd-channel-renderer")]')
        d = [["1","1"]]
        j = 0
        for n in names:
            val = info[j].text #.encode("ascii", "replace").replace(u'\xe2','a')
            
            visitors = (n.text, val)
            today = datetime.date.today() 
            stoday = topic + "-"+today.isoformat() 
            if len(n.text) > 5:
                r.sadd(stoday,*visitors)
                print(stoday,n.text,val)
            j = j +1 
            


        browser.execute_script("return document.body")
        browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2.4)
        print d    
        i=i+1


import time

def wait_timeout(proc, seconds):
    """Wait for a process to finish, or raise exception after timeout"""
    start = time.time()
    end = start + seconds
    interval = min(seconds / 1000.0, .25)

    while True:
        result = proc()
        if result is not None:
            return result
        if time.time() >= end:
            raise RuntimeError("Process timed out")
        time.sleep(interval)
    
def main():  
     
    while(True):
        wait_timeout(crawl,5)    
        time.sleep(1)

if __name__ == "__main__":
    main()
