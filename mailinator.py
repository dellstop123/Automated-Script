from selenium import webdriver
from time import sleep
import time
import unicodedata
import requests
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="C://Users//gunee//Desktop//TinderBot//chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://www.mailinator.com/v3/#/#inboxpane")
driver.implicitly_wait(10)

def main():

    with open('usr.csv','r') as usr:
      while (True):
        username = usr.readline()
        cnt = 1
        # for name in username:
        print("Line {}: {}".format(cnt, username.strip()))
            # name = usr.readline()
        cnt += 1
        if username == "":
            print("::DONE::")
            break
        # When a newline is returned, the line is empty.
        if username == "\n":
            print("::EMPTY LINE::")
            continue
        driver.implicitly_wait(20)      
        email = driver.find_element_by_xpath('//*[@id="inbox_field"]')
        slow_typing(email,username)
        # driver.save_screenshot('image.png')
        driver.implicitly_wait(10)
        go = driver.find_element_by_xpath('//*[@id="go_inbox"]')            
        go.click()
        driver.implicitly_wait(10)
        email.clear()
      print(cnt)    

def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)        

if __name__ == '__main__':
   main()