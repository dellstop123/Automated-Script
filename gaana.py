from selenium import webdriver
from time import sleep
import unicodedata
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome(executable_path="C://Users//gunee//Desktop//TinderBot//chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://djpunjab.fm//")
x = 6

def main():
        global x
        search = driver.find_element_by_xpath('/html/body/p[14]/a')
        search.click()
        # driver.implicitly_wait(2)
        google = driver.find_element_by_xpath('/html/body/p[3]/a')
        google.click()
        # driver.implicitly_wait(1)
        sidhu = driver.find_element_by_xpath('/html/body/p[4]/a')
        sidhu.click()
        # driver.implicitly_wait(1)             
        svg = driver.find_element_by_xpath('/html/body/p['+ str(x) +']/a')
        svg.click()
        # driver.implicitly_wait(1)
        download = driver.find_element_by_xpath('//*[@id="b"]/p[2]/a')
        download.click()
        # driver.implicitly_wait(1)
        # download.quit()
        download = driver.find_element_by_xpath('//*[@id="b"]/p[2]/a')
        download.click()
        # driver.implicitly_wait(1)
        x = x+1
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(3)
        home = driver.find_element_by_xpath('/html/body/p[6]/a')
        home.click()
        # driver.implicitly_wait(1)
        main()

            

if __name__ == '__main__':
   
    main()