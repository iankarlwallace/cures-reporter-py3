# Patient object from org.afmc.patient module

class Patient:

    def __init__(self):
        self.fname = None
        self.lname = None
        self.dob = None

    def __init__(self, fname, lname, dob):
        self.fname = fname
        self.lname = lname
        self.dob = dob

    def getFirstname(self):
        return self.fname

    def setFirstname(self, fname):
        self.fname = fname

    def getLastname(self):
        return self.lname

    def setLastname(self, lname):
        self.lname

    def getDOB(self, dob):
        return self.dob

    def setDOB(self, dob):
        self.dob
