# XLSX Spreadsheet is the data repository that we use currently
# The library needs to be in the Excel files directory to work correctly (that's what the docs report)
#

import sys, os
import openpyxl
import config
import logging
import common.patient as pt

class Dbtools:

    def __init__(self):
        None

    def _is_file_rw(self, file):
        if os.access(file, os.R_OK|os.W_OK ):
            return True
        else:
            return False

    def load_patients(self):
        ptList = []
        mLog = logging.getLogger('root')
        if self._is_file_rw(config.XLSX_FILE):
            wb = openpyxl.load_workbook(config.XLSX_FILE, data_only=True)
        else:
            raise OSError('File ' + config.XLSX_FILE + ' not accessible.')
        sheet = wb.get_sheet_by_name('Sheet1')
        for row in sheet.iter_rows(min_row=2):
            # Foreach row we should create a patient object and add to our object map
            id_num = row[0].value
            name = row[1].value
            fname, lname = name.split(';')
            fname = fname.strip()
            lname = lname.strip()
            mrn = row[6].value
            dob = row[7].value
            newPt = pt.Patient(id_num, fname, lname, mrn, dob)
            ptList.append(newPt)
            print('.', end='')
        print('.') 
        sys.stdout.flush()
        return ptList
