# Browser abstraction to get a webdriver (for whichever browser we are using)
# Setup the profile and maximize it
# Should include basics of downloading ICA file and XLSX files automatically

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Browser:

    def __init__(self):
        self.mLog = logging.getLogger('root')
        self.prof = self._setup_profile()
        self.wd = webdriver.Firefox(firefox_profile = self.prof)
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)

    def __del__(self):
        self.mLog.debug('__del__ - cleanup')
        self.wd.quit()

    def _setup_profile(self):
        self.mLog.debug('Create FireFox Profile')
        prof = webdriver.FirefoxProfile()
        prof.set_preference('browser.helperApps.neverAsk.openFile','application/octet-stream,application/x-ica')
        self.mLog.debug('Return FireFox Profile')
        return prof

    def goto_url(self, url):
        self.mLog.debug('Going to URL:' + url)
        self.wd.get(url)

    def assert_in_title(self, text):
        self.mLog.debug('Assert that title has: ' + text)
        assert text in self.wd.title

    def fill_element_by_name(self, elemName, value):
        self.mLog.debug('Fill element by name ' + elemName + ' with ' + value)
        element = self.wd.find_element_by_name(elemName)
        element.clear()
        element.send_keys(value)

    def fill_element_by_xpath(self, elemXpath, value):
        self.mLog.debug('Fill element by Xpath ' + elemXpath + ' with ' + value)
        element = self.wd.find_element_by_xpath(elemXpath)
        element.clear()
        element.send_keys(value)

    def click_element_by_name(self, elemName):
        self.mLog.debug('Click element by name ' + elemName)
        element = self.wd.find_element_by_name(elemName)
        element.click()

    def click_element_by_xpath(self, elemXpath):
        self.mLog.debug('Click element by Xpath ' + elemXpath)
        element = self.wd.find_element_by_xpath(elemXpath)
        element.click()
