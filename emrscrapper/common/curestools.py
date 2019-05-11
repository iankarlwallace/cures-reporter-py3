# CURES Tools - tools for gathering prescription data from Cures website based on
# Patient name, DOB returning a list of prescriptions filled in a certain amount of time

import config
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Curestools:

    def __init__(self, creds):
        self.fp = self._setup_firefox_profile()
        self.wd = webdriver.Firefox(firefox_profile = self.fp)
        self.wd.implicitly_wait(3)
        self.creds = creds

    def __del__(self):
        self.wd.quit()

    def _setup_firefox_profile(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference('browser.helperApps.alwaysAsk.force', False)
        return fp

    def _fill_element_by_name(self, elemName, value):
       element = self.wd.find_element_by_name(elemName)
       element.clear()
       element.send_keys(value)

    def login(self):
        self.wd.get(config.CURES_HOME_URL)
        assert 'State of California Department of Justice TST02' in self.wd.title
        self._fill_element_by_name('USER', self.creds.getCuresUsername())
        self._fill_element_by_name('PASSWORD', self.creds.getCuresPassword())
        elemLogin = self.wd.find_element_by_xpath('//*[@id="loginForm"]/div[1]/span/input')
        elemLogin.click()
        time.sleep(10)
        return

