#
# EMR Scrapper
#
# Script developed to help with scrapping of prescription data from:
# 1) CURES reporting on patients after c/sections
# 2) EMR scrapping for data needed out of the EMR
# Developed for research project and not intended for general usage
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import config 
import common.log as log
import common.patient as pt
import common.credentials as cred
import common.dbtools as db

import argparse, time, sys

def run():
    mLog = log.getLogger()
    mLog.debug('Starting EMR Scrapper')
    mLog.debug('Parsing of command line args %s', sys.argv)

    parser = argparse.ArgumentParser()
    parser.add_argument('-cu','--cures-username',help="CURES website username")
    parser.add_argument('-cp','--cures-password',help="CURES website password")
    parser.add_argument('-eu','--emr-username',help="EMR website username")
    parser.add_argument('-ep','--emr-password',help="EMR website password")
    args = parser.parse_args()

    mLog.debug('Args %s', args)

    mCred = cred.Credentials(args.cures_username, args.cures_password, args.emr_username, args.emr_password)
    mLog.debug('Credentials object created')

    patients = db.Dbtools().load_patients()
    for patient in patients:
        mLog.debug(patient)

    return

    fp = webdriver.FirefoxProfile()
    fp.set_preference('browser.helperApps.alwaysAsk.force', False)

    driver = webdriver.Firefox(firefox_profile = fp)
    driver.implicitly_wait(5)
    driver.get(config.EMR_HOME_URL)
    assert 'Welcome to CernerWorks!' in driver.title
    elemUserName = driver.find_element_by_name('username')
    elemUserName.clear()
    elemUserName.send_keys(mCred.getEmrUsername())
    elemPassword = driver.find_element_by_name('password')
    elemPassword.clear()
    elemPassword.send_keys(mCred.getEmrPassword())
    elemLogin = driver.find_element_by_id('loginBtn')
    elemLogin.click()
    time.sleep(4)
    elemPowerChartP441 = driver.find_element_by_xpath('//*[@id="myapps-container"]/div[12]/a')
    elemPowerChartP441.click()
    time.sleep(4)
    driver.close()

    mLog.debug('Finished EMR Scrapper')
