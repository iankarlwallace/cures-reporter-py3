# EMR Helper tools that can retrieve data from Cerner for an MRN and the like
# Relies on pyautogui libraries to do most of the work

import time
import config
import logging
import pyautogui
import common.browser
from pyscreeze import ImageNotFoundException

class Emrtools:

    def __init__(self, creds):
        self.mLog = logging.getLogger('root')
        self.browser = common.browser.Browser()
        self.creds = creds
        pyautogui.PAUSE=2.5

    def __del__(self):
        None

    def _pag_click(self, img):
        self.mLog.debug('Click on image [' + img +']')
        pyautogui.click(config.IMG_DIR + img)
        return

    def _pag_type(self, txt):
        self.mLog.debug('Type [' + txt +']')
        pyautogui.typewrite(txt)
        return

    def _pag_locate(self, img):
        self.mLog.debug('Locate [' + img +']')
        pyautogui.locateOnScreen(config.IMG_DIR + img, grayscale=True)
        return

    def login(self):
        self.browser.goto_url(config.EMR_HOME_URL)
        self.browser.assert_in_title('Welcome to CernerWorks!')
        self.browser.fill_element_by_name('username',self.creds.getEmrUsername())
        self.browser.fill_element_by_name('password',self.creds.getEmrPassword())
        self.browser.click_element_by_id('loginBtn')
        time.sleep(5)
        self.browser.click_element_by_xpath('//*[@id="myapps-container"]/div[12]/a/img')
        time.sleep(8)
        return

    def search(self, mrn):
        self.mLog.debug('Search for MRN [' + mrn +'] start.')
        try:
            self._pag_locate('powerchart-search-mrn-box.png')
            self.mLog.debug('Search button found on first try.')
        except (ImageNotFoundException, TypeError):
            self.mLog.debug('Search button not loaded yet, lets wait and try again.')
            time.sleep(5)
        self._pag_click('powerchart-search-mrn-box.png')
        self.mLog.debug('Search button found on second try.')
        self._pag_type(mrn)
        self._pag_click('powerchart-search-glass.png')
        self._pag_click('powerchart-search-ok-btn.png')
        try:
            self._pag_locate('powerchart-assign-relationship.png')
            self._pag_click('powerchart-relationship-outpatient-provider.png')
            self._pag_click('powerchart-ok-btn.png')
        except (ImageNotFoundException, TypeError):
            None
        try:
            self._pag_locate('discern-alert-vaccination-necessary.png')
            self._pag_click('powerchart-ok-btn.png')
        except (ImageNotFoundException, TypeError):
            None
        time.sleep(2)
        self._pag_click('powerchart-close-single-chart.png')
        self.mLog.debug('Search for MRN [' + mrn +'] complete.')
        

    def logout(self):
        time.sleep(2)
        cur_screen = pyautogui.screenshot(config.IMG_DIR + 'current-screen.png')
        self._pag_click('cerner-task-btn.png')
        self._pag_click('cerner-exit-btn.png')
        self._pag_click('powerchart-exit-btn.png')
        self._pag_click('powerchart-logoff-btn.png')             

    def find_patient(self, mrn):
        None
