from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import *
import time

options = Options()
options.headless = True

class Browser:
    def __init__(self,link,STREAMER_NAME):
        self.link = link
        self.stname = STREAMER_NAME
        self.browser = webdriver.Chrome(options=options)

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
            root = Tk()
            root.geometry("640x400+100+100")
            aaa1 = f"| ->{self.stname} total views: {allViews} |"
            aaa2 = f"| ->{self.stname} total time: {totalTime} |"
            firstLabel = Label(root, text=aaa1)
            firstLabel.pack()
            secondLabel = Label(root, text=aaa2)
            secondLabel.pack()

            def closeProgram(event):
                exit(1)
            def reloadTexts(event):
                allViewsR = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/p").text
                totalTimeR = self.browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span").text
                aaa1R = f"| ->{self.stname} total views: {allViewsR} |"
                aaa2R = f"| ->{self.stname} total time: {totalTimeR} |"
                firstLabel.config(text=aaa1R)
                secondLabel.config(text=aaa2R)
                print(f"""
                ---------------------------------
                |->{self.stname} total views: {allViews} |
                |->{self.stname} total time: {totalTime} |
                ---------------------------------
                """)

            btn1 = Button(root, text="EXIT")
            btn1.bind("<Button-1>", closeProgram)
            btn1.pack()
            btn2 = Button(root, text="RELOAD")
            btn2.bind("<Button-1>", reloadTexts)
            btn2.pack()
            root.mainloop()