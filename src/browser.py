from selenium import webdriver
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

class Browser:
    def __init__(self,link,STREAMER_NAME):
        self.link = link
        self.stname = STREAMER_NAME
        self.browser = webdriver.Chrome()

        Browser.goTwitch(self)
    def goTwitch(self):
        self.browser.get(self.link)
        time.sleep(3)
        while True:
            allViews = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/p").text
            totalTime = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span").text
            print(f"""
            ---------------------------------
            |->{self.stname} total views: {allViews} |
            |->{self.stname} total time: {totalTime} |
            ---------------------------------
            """)
            time.sleep(2)
