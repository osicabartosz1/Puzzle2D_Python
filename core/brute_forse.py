import time
import os
import sys
from entities.board import Board
from printer.printer import Printer
from models.set_of_blocks import SetOfBlocks

class BruteForce():
    def __init__(self, inPattern):
        self.myPattern = inPattern
    def PlaceBlock(self, nr):
        if(nr == 6):
            self.saveHistory(self.myBoard.makeHistory())
        if(nr == 18):
            myPrinter = Printer(self.myBoard);
            myPrinter.printBoard(self.myBoard.makeHistory())
            print("last history = " + self.myBoard.makeHistory())
            return True
        while self.myBoard.moveToNextCorrectPosition(self.mySetOfBlocks.Zbior[nr]):
            if self.PlaceBlock(nr + 1):
                return True
        for r in range(nr , 18):
            self.mySetOfBlocks.Zbior[r].resetPosition()
        return False
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
    def selectHistory(self,folder):
        temp = self.pickTheNameOfYoungestFile(folder)
        temp = self.addOne(temp, 1) # 33 - pomijanie podobnych rozwiazan
        return self.checkHistory(temp)
    def Run(self):
        history = ""
        historyEnd = ""
        startTime = time.time()
        EndTime = time.time()
        counter = 0


        self.MainFolder = os.getcwd()
        print("Start = " + str(startTime))
        print(self.MainFolder)

        while True:
            counter = counter + 1
            if historyEnd == "":
                if not (startTime + 1 > EndTime):
                    break
            else:
                if history > historyEnd:
                    print("history      = " + history)
                    print("historyEnd   = " + historyEnd)
                    break
            
            if len(sys.argv) == 1:
                history = self.selectHistory(self.MainFolder)
                
            if counter == 1 and len(sys.argv) == 2:
                history = sys.argv[1]

            if counter == 1 and len(sys.argv) == 3:
                history = sys.argv[1]
                historyEnd = sys.argv[2]
            
            if counter > 1:
                history = self.addOne(history, 1)
            
            print( "old  history = " + history)
            
            try:
                del  mySetOfBlocks
            except:
                Nothing = 1
            try:
                del  myBoard
            except:
                Nothing = 1
            self.myBoard = Board(self.myPattern)
            #self.myHolesFinder = HolesFinder(myBoard)
            self.mySetOfBlocks = SetOfBlocks(history)
            self.PlaceBlock(0)
            EndTime = time.time()

        print("End = " + str(EndTime))
        print("Time dif = " + str(EndTime - startTime))
