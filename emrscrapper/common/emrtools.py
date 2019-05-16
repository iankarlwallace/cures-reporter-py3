# EMR Helper tools that can retrieve data from Cerner for an MRN and the like
# Relies on pyautogui libraries to do most of the work

import common.browser
import pyautogui
import config
import time

class Emrtools:

    def __init__(self, creds):
        self.browser = common.browser.Browser()
        self.creds = creds

    def __del__(self):
        None

    def login(self):
        self.browser.goto_url(config.EMR_HOME_URL)
        self.browser.assert_in_title('Welcome to CernerWorks!')
        self.browser.fill_element_by_name('username',self.creds.getEmrUsername())
        self.browser.fill_element_by_name('password',self.creds.getEmrPassword())
        self.browser.click_element_by_id('loginBtn')
        time.sleep(5)
        self.browser.click_element_by_xpath('//*[@id="myapps-container"]/div[12]/a/img')
        time.sleep(10)
        return

    def logout(self):
        time.sleep(10)
        pyautogui.PAUSE=2
        cur_screen = pyautogui.screenshot(config.IMG_DIR + 'current-screen.png')
        pyautogui.click(config.IMG_DIR + 'cerner-task-btn.png')
        pyautogui.click(config.IMG_DIR + 'cerner-exit-btn.png')
        pyautogui.click(config.IMG_DIR + 'powerchart-exit-btn.png')
        pyautogui.click(config.IMG_DIR + 'powerchart-logoff-btn.png')             

    def find_patient(self, mrn):
        None
