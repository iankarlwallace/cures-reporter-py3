# EMR Helper tools that can retrieve data from Cerner for an MRN and the like
# Relies on pyautogui libraries to do most of the work

import common.browser
import pyautogui
import config
import time
from pyscreeze import ImageNotFoundException

class Emrtools:

    def __init__(self, creds):
        self.browser = common.browser.Browser()
        self.creds = creds
        pyautogui.PAUSE=2

    def __del__(self):
        None

    def _pag_click(self, img):
        pyautogui.click(config.IMG_DIR + img)
        return

    def _pag_type(self, txt):
        pyautogui.typewrite(txt, interval=0.1)
        return

    def _pag_locate(self, img):
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
        time.sleep(5)
        return

    def search(self, mrn):
        self._pag_click('powerchart-search-mrn-box.png')
        self._pag_type(mrn)
        self._pag_click('powerchart-search-glass.png')
        self._pag_click('powerchart-search-ok-btn.png')
        try:
            self._pag_locate('powerchart-assign-relationship.png')
            self._pag_click('powerchart-relationship-outpatient-provider.png')
            self._pag_click('powerchart-ok-btn.png')
        except (ImageNotFoundException, TypeError):
            None
        

    def logout(self):
        time.sleep(5)
        cur_screen = pyautogui.screenshot(config.IMG_DIR + 'current-screen.png')
        self._pag_click('cerner-task-btn.png')
        self._pag_click('cerner-exit-btn.png')
        self._pag_click('powerchart-exit-btn.png')
        self._pag_click('powerchart-logoff-btn.png')             

    def find_patient(self, mrn):
        None
