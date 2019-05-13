# CURES Tools - tools for gathering prescription data from Cures website based on
# Patient name, DOB returning a list of prescriptions filled in a certain amount of time

import common.browser
import config
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Curestools:

    def __init__(self, creds):
        self.browser = common.browser.Browser()
        self.creds = creds

    def __del__(self):
        self.browser.quit()

    def login(self):
        self.browser.goto_url(config.CURES_HOME_URL)
        assert 'State of California Department of Justice TST02' in self.browser.wd.title
        self.browser.fill_element_by_name('USER', self.creds.getCuresUsername())
        self.browser.fill_element_by_name('PASSWORD', self.creds.getCuresPassword())
        self.broser.click_element_by_xpath('//*[@id="loginForm"]/div[1]/span/input')
        time.sleep(10)
        return
