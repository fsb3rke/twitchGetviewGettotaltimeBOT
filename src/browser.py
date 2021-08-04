from selenium import webdriver
from tkinter import *
import time





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
            root = Tk()
            root.geometry("640x400+100+100")
            aaa1 = f"| ->{self.stname} total views: {allViews} |"
            aaa2 = f"| ->{self.stname} total time: {totalTime} |"
            firstLabel = Label(root, text=aaa1)
            firstLabel.pack()
            secondLabel = Label(root, text=aaa2)
            secondLabel.pack()

            def key(event):
                print("pressed", repr(event.char))

            def callback(event):
                print("clicked at", event.x, event.y)

            def closeProgram(event):
                exit(1)

            btn1 = Button(root, text="EXIT")
            btn1.bind("<Button-1>", closeProgram)
            btn1.pack()
            root.mainloop()

            time.sleep(2)