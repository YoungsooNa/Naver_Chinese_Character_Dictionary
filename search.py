from selenium import webdriver
import time
import urllib.parse


class NCSearch:
    def __init__(self):
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
    # Get the chinese character and Return meaning of the character
    def search(self, c: str):
        query = urllib.parse.quote(c, safe='')
        self.driver.get("https://hanja.dict.naver.com/search?query=" + query)
        # this condition can be changed
        time.sleep(2)
        sound = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd/a[1]/span""")
        meaning = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd/div""")
        return sound.text, meaning.text

    def close(self):
        self.driver.close()

