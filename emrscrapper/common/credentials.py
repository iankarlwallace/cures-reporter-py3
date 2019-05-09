# Credentials object for login to CURES site and EMR

class Credentials:

    def __init__(self):
        self.curesr_uname = None
        self.cures_pwd = None
        self.emr_uname = None
        self.emr_pwd = None

    def __init__(self, cures_uname, cures_pwd, emr_uname, emr_pwd):
        self.cures_uname = cures_uname
        self.cures_pwd = cures_pwd
        self.emr_uname = emr_uname
        self.emr_pwd = emr_pwd

    def getCuresUsername(self):
        return self.cures_uname

    def setCuresUsername(self, cures_uname):
        self.cures_uname = cures_uname

    def getCuresPassword(self):
        return self.cures_pwd

    def setCuresPassword(self, cures_pwd):
        self.cures_pwd = cures_pwd

    def getEmrUsername(self):
        return self.emr_uname

    def setEmrUsername(self, emr_uname):
        self.emr_uname = emr_uname

    def getEmrPassword(self):
        return self.emr_pwd

    def setEmrPassword(self, emr_pwd):
        self.emr_pwd = emr_pwd 
