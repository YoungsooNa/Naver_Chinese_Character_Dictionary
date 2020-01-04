import selenium
from selenium import webdriver
import time
import urllib.parse

from selenium.common.exceptions import NoSuchElementException


class NCSearch:
    def __init__(self):
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
    # Get the chinese character and Return meaning of the character
    def search(self, c:str):
        query = urllib.parse.quote(c, safe='')
        self.driver.get("https://hanja.dict.naver.com/search?query=" + query)
        # this condition can be changed
        time.sleep(2)
        try:
            sound = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd/a[1]/span""")
            meaning = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd/div""")
        except NoSuchElementException:
            return None, None

        return sound.text, meaning.text

    def searchLetters(self, s: str):
        q_string = ""
        for c in s:
            query = urllib.parse.quote(c, safe='')
            q_string += query

        self.driver.get("https://hanja.dict.naver.com/search?query=" + q_string)
        # this condition can be changed
        time.sleep(2)

        try:
            check_word = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/ul/li[2]/a""").text
            if check_word == "고사성어":
                pass
            else:
                return None, None
            sound = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd[1]/a[1]/span""")
            meaning = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd[2]""")
            return sound.text, meaning.text
        except NoSuchElementException:
            try:
                check_word = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/h5/span[1]/span""")
                sound = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd[1]/a[1]/span""")
                meaning = self.driver.find_element_by_xpath("""//*[@id="content"]/div[3]/dl/dd[2]""")
                return sound.text, meaning.text

            except NoSuchElementException:
                print("고사성어 숙어 단어 없음")
                return None, None

    def close(self):
        self.driver.close()

