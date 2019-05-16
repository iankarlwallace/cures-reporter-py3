# Configuration object with defaults for URLs and the like
# Should be able to parse from environment if overrides
# but has not been built out yet

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
CURES_HOME_URL = 'https://cures.doj.ca.gov'
EMR_HOME_URL = 'https://vchaca.cernerworks.com'
XLSX_DIR = os.path.join(ROOT_DIR,'..','xlsx')
XLSX_FILE = os.path.join(XLSX_DIR,'c_s5to11_18_c.xlsx')
IMG_DIR = os.path.join(ROOT_DIR,'..','images','')
