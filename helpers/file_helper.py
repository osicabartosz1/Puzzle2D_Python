import os;

class FileHelper:
    def __init__(self):
        self.MainFolder = os.getcwd()

    def addOne(self, inputStr, where):
        if len(inputStr) == 0:
            return ""
        last = int(inputStr[len(inputStr) - 1 - where:len(inputStr) - where])
        last = last + 1
        res = inputStr[0:len(inputStr) - 1 - where] + str(last) + len(inputStr[len(inputStr) - where : len(inputStr)]) * "0"
        return res
    
    def pickTheNameOfYoungestFile(self, folder):
        temp = os.listdir(folder)
        res = ""
        for t in temp:
            if not t.upper().endswith(".HTML"):
                continue
            t2 = t.upper().replace(".HTML", "")
            if not t2.isdigit():
                continue
            if res < t2:
                res = t2		
        return res
    
    def saveHistory(self, toWrite):
        fhand = open(self.MainFolder + '\\history.txt','a')
        fhand.writelines(toWrite + '\n')
        fhand.close()

    def checkHistory(self,hist):
        if len(hist) < 54 or (not hist.isdecimal()):
            return "000000000000000000000000000000000000000000000000000000"
        return hist
    
    def selectHistory(self,folder = os.getcwd()):
        temp = self.pickTheNameOfYoungestFile(folder)
        temp = self.addOne(temp, 1) # 33 - pomijanie podobnych rozwiazan
        return self.checkHistory(temp)