from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
import time, json

class Parse_urls(object):

    def __init__(self):
        self.list_urls ={}
        self.error_url =[]
        self.nps_list = [u'Zion National Park', u'Yellowstone national Park', u'Acadia National Park', u'Yosemite National Park', u'Sequoia National Park', u'Crater Lake National Park', u'Grand Canyon National Park', u'Great Smoky Mountains national Park', u'Death Valley National Park', u'Redwood National Park', u'Olympic National Park', u'Grand Teton national Park', u'Everglades National Park', u'Big Bend National Park', u'Joshua Tree National Park', u'Bryce Canyon national Park', u'North Cascades National Park', u'Arches National Park', u'Great Sand Dunes National Park', u'Dry Tortugas National Park ', u'Mammoth Cave national Park', u'Petrified Forest National Park', u'Biscayne National Park', u'Mount Rainer national park', u'Virgin Islands National Park', u'shenandoah national park', u'Carlsbad Caverns National Park', u'Cuyahoga National Park', u'Guadalupe Mountains National Park', u'Congaree National Park', u'Saguaro National Park', u'Kings Canyon National Park', u'Great Basin National Park', u'Isle Royale National Park', u'Glacier Bay National Park', u'Kenai Fjords National Park', u'Voyageurs National Park', u'Denali National Park', u'Katmai National Park', u'Wrangell St. Elias National Park', u'Hot Springs National Park', u'Canyonlands National Park', u'Kobuk Valley National Park', u'Rocky Mountain National Park', u'Gates of The Arctic national park', u'Lake Clark National Park', u'Badlands National Park', u'Glacier National Park', u'Wind Cave National Park', u'Black Canyon of the Gunnison National Park', u'Volcanoes National Park', u'Mesa Verde National Park', u'Theodore Roosevelt National Park', u'haleakala national park', u'Capitol Reef National Park', u'National Park of American Samoa', u'Channel islands national park', u'lassen volcanic national park', u'pinnacles national park']

    def send_search(self):
        current_url =''
        for item in self.nps_list:
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get('http://tripadvisor.com/Attractions/')
            time.sleep(2)
            try:
                current_url = self.fetch_url(driver, item)
                if(self.check_error_url(item, current_url) == False):
                    print item
                    print current_url
                    self.list_urls[item]= current_url
                driver.close()
            except Exception:
                print('can not get item: ' + item + 'and url: '+ current_url)
                self.error_url.append({item: current_url})
            finally:
                pass
        return self.list_urls, self.error_url

    def fetch_url(self, driver, item):
        search = driver.find_element_by_class_name('typeahead_input')
        search.click()
        search.clear()
        search.send_keys(item)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.SPACE)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        button = driver.find_element_by_class_name('form_submit')
        button.click()
        time.sleep(1)
        current_url = driver.current_url
        return current_url

    def check_error_url(self,item, url):
        if ('Review' in url or 'AttractionProductDetail' in url):
            self.error_url.append({item:url})
            return True
        else:
            return False

if __name__ =="__main__":
    obj = Parse_urls()
    list_urls, error_url = obj.send_search()
    full_file = open('./nps_url.json1','w')
    json.dump(list_urls, full_file)
    print('done')
    error_file = open('./error_url.json1','w')
    json.dump(error_url, error_file)
