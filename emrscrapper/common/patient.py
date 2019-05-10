# Patient object from org.afmc.patient module

class Patient:

    def __init__(self):
        self.id_num = None
        self.fname = None
        self.lname = None
        self.mrn = None
        self.dob = None

    def __init__(self, id_num, fname, lname, mrn, dob):
        self.id_num = id_num
        self.fname = fname
        self.lname = lname
        self.mrn = mrn
        self.dob = dob

    def __str__(self):
        """Basic Patient Data Container Object"""
        result = '[ ID: ' + str(self.id_num) + ' [' + self.fname + ' ' + self.lname + '] MRN: ' + str(self.mrn) + ' DOB: ' + str(self.dob) + ']'
        return result

    def getIdNum(self):
        return self.id_num

    def setIdNum(self, id_num):
        self.id_num = id_num

    def getFirstname(self):
        return self.fname

    def setFirstname(self, fname):
        self.fname = fname

    def getLastname(self):
        return self.lname

    def setLastname(self, lname):
        self.lname

    def getMrn(self):
        return self.mrn

    def setMrn(self, mrn):
        self.mrn = mrn

    def getDOB(self, dob):
        return self.dob

    def setDOB(self, dob):
        self.dob
