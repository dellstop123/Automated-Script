from selenium import webdriver
# from secrets import username, password
from time import sleep
import unittest


driver = webdriver.Chrome(executable_path="C://Users//gunee//Desktop//TinderBot//chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://tinder.com/")

class TinderBot(unittest.TestCase):

    def login(self):

        
        # cookies_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/button/svg')
        # cookies_btn.click()
    
        fb_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
        fb_btn.click()
        driver.implicitly_wait(10)
        # switch to login popup
        base_window = driver.window_handles[0]
        driver.switch_to_window(driver.window_handles[1])

        email_in = driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys("guneet.singh.710")

        pw_in = driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys("8492892832")

        login_btn = driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        driver.switch_to_window(base_window)

        popup_1 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


if __name__ == "__main__":
   bot = TinderBot()
   bot.login()