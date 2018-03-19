from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

class Parse_location(object):

    def __init__(self):
        self.result=[]
        self.errors =[]

    def send_search(self):
        current_url =''
        time.sleep(2)
        result =[]
        full_file = open('./file_w_loc.json','w')
        data_file = json.loads(open('./data.json').read())
        for item in data_file:
            driver = webdriver.Chrome()
            driver.get('http://latitude.to/')
            title = item['data']['title']
            try:
                loc = self.fetching(driver, title)
                item['data']['loc']=loc
                result.append(item)
            except Exception:
                print 'error happens in title '+ title

            finally:
                driver.close()
            json.dump(result, full_file)
        return

    def fetching(self, driver, title):
        search = driver.find_element_by_class_name('g-search')
        search.click()
        search.clear()
        search.send_keys(title)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        return self.fetchCorrdinate(driver, title)

    def fetchCorrdinate(self, driver, title):
        loc = driver.find_element_by_id('home-DD')
        value = loc.get_attribute('value')
        corrdinate = value.split(" ")
        return corrdinate

if __name__ =="__main__":
    obj = Parse_location()
    obj.send_search()
