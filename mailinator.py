from selenium import webdriver
from time import sleep
import time
import unicodedata
import requests
from random_username.generate import generate_username
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="C://Users//gunee//Desktop//TinderBot//chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://www.mailinator.com/v3/#/#inboxpane")
driver.implicitly_wait(10)

def main():
    random = int(input('Enter random text you want:'))
    file1 = open("usr.csv","w")
    file2 = generate_username(random)
    str1 = '\n'.join(map(str, file2))
    file1.write(str1)
    print(str1)
    file1.close()
    with open('usr.csv','r') as usr:
      while (True):
        username = usr.readline()
        print("Line: {}".format(username.strip()))       
        if username == "":
            print("::DONE::")
            break
        # When a newline is returned, the line is empty.
        if username == "\n":
            print("::EMPTY LINE::")
            continue
        driver.implicitly_wait(10)      
        email = driver.find_element_by_xpath('//*[@id="inbox_field"]')
        slow_typing(email,username)
        # driver.save_screenshot('image.png')
        driver.implicitly_wait(10)
        go = driver.find_element_by_xpath('//*[@id="go_inbox"]')            
        go.click()
        
        driver.find_element_by_xpath('//*[@id="inbox_field"]').clear()
        driver.implicitly_wait(10)
         

def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.5)        

if __name__ == '__main__':
   main()