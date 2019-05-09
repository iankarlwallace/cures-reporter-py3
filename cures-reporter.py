#
# Cures-Reporter Script
#

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

fp = webdriver.FirefoxProfile()
fp.set_preference('browser.helperApps.alwaysAsk.force', False)

driver = webdriver.Firefox(firefox_profile = fp)
driver.implicitly_wait(5)
driver.get('https://vchaca.cernerworks.com')
assert 'Welcome to CernerWorks!' in driver.title
elemUserName = driver.find_element_by_name('username')
elemUserName.clear()
elemUserName.send_keys('')
elemPassword = driver.find_element_by_name('password')
elemPassword.clear()
elemPassword.send_keys('')
elemLogin = driver.find_element_by_id('loginBtn')
elemLogin.click()
time.sleep(20)
elemPowerChartP441 = driver.find_element_by_xpath('//*[@id="myapps-container"]/div[12]/a')
elemPowerChartP441.click()
time.sleep(20)
driver.close()
