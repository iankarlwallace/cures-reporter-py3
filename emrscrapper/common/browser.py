# Browser abstraction to get a webdriver (for whichever browser we are using)
# Setup the profile and maximize it
# Should include basics of downloading ICA file and XLSX files automatically

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Browser:

    def __init__(self):
        self.prof = self._setup_profile()
        self.wd = webdriver.Firefox(firefox_profile = self.prof)
        self.wd.maximize_window()
        self.wd.implicitly_wait(3)

    def __del__(self):
        self.wd.quit()

    def _setup_profile(self):
        prof = webdriver.FirefoxProfile()
        prof.set_preference('browser.helperApps.neverAsk.openFile','application/octet-stream,application/x-ica')
        return prof

    def goto_url(self, url):
        self.wd.get(url)

    def fill_element_by_name(self, elemName, value):
        element = self.wd.find_element_by_name(elemName)
        element.clear()
        element.send_keys(value)

    def click_element_by_xpath(self, elemXpath, value):
        element = self.wd.find_element_by_xpath(elemXpath)
        element.click()

    def quit(self):
        self.__del__
