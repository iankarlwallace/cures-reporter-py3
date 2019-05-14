#
# EMR Scrapper
#
# Script developed to help with scrapping of prescription data from:
# 1) CURES reporting on patients after c/sections
# 2) EMR scrapping for data needed out of the EMR
# Developed for research project and not intended for general usage
#

import argparse
import config
import sys
import time

import common.credentials as cred
import common.curestools as cures
import common.dbtools as db
import common.emrtools as emr
import common.log as log
import common.patient as pt

def run():
    mLog = log.getLogger()
    mLog.debug('Starting EMR Scrapper')
    mLog.debug('Parsing of command line args %s', sys.argv)

    parser = argparse.ArgumentParser()
    parser.add_argument('-cu',
        '--cures-username',
        required=True,
        help="CURES website username")
    parser.add_argument('-cp',
        '--cures-password',
        required=True,
        help="CURES website password")
    parser.add_argument('-eu',
        '--emr-username',
        required=True,
        help="EMR website username")
    parser.add_argument('-ep',
        '--emr-password',
        required=True,
        help="EMR website password")
    args = parser.parse_args()

    mLog.debug('Args %s', args)

    mCred = cred.Credentials(args.cures_username, args.cures_password, args.emr_username, args.emr_password)
    mLog.debug('Credentials object created')

    patients = db.Dbtools().load_patients()
    mLog.debug('Found [' + str(len(patients)) + '] patients.')

    mCures = cures.Curestools(mCred)
    mCures.login()
    time.sleep(10)
    mLog.debug('Finished EMR Scrapper')
