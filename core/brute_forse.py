import time
import sys
from entities.board import Board
from printer.printer import Printer
from models.set_of_blocks import SetOfBlocks
from helpers.file_helper import FileHelper

class BruteForce():
    def __init__(self, inPattern):
        self.myPattern = inPattern
        self.myFileHelper = FileHelper()
        self.history = ""
        self.historyEnd = ""
        self.startTime = time.time()
        self.endTime = time.time()
        self.counter = 0
        print("Start = " + str(self.startTime))
    
    def __del__(self):
        print("End = " + str(self.endTime))
        print("Time dif = " + str(self.endTime - self.startTime))

    def PlaceBlock(self, nr):
        if(nr == 6):
            self.myFileHelper.saveHistory(self.myBoard.makeHistory())
        if(nr == 18):
            myPrinter = Printer(self.myBoard);
            self.history = self.myBoard.makeHistory();
            myPrinter.printBoard(self.history)
            print("last history = " + self.history)
            return True
        while self.myBoard.moveToNextCorrectPosition(self.mySetOfBlocks.Zbior[nr]):
            if self.PlaceBlock(nr + 1):
                return True
        for r in range(nr , 18):
            self.mySetOfBlocks.Zbior[r].resetPosition()
        return False

    def Run(self):
        while True:
            self.counter = self.counter + 1
            if self.historyEnd == "":
                if not (self.startTime + 1 > self.endTime):
                    break
            else:
                if self.history > self.historyEnd:
                    print("history      = " + self.history)
                    print("historyEnd   = " + self.historyEnd)
                    break
            
            if len(sys.argv) == 1:
                self.history = self.myFileHelper.selectHistory()
                
            if self.counter == 1 and len(sys.argv) == 2:
                self.history = sys.argv[1]

            if self.counter == 1 and len(sys.argv) == 3:
                self.history = sys.argv[1]
                self.historyEnd = sys.argv[2]
            
            if self.counter > 1:
                self.history = self.myFileHelper.addOne(self.history, 1)
            
            print( "old  history = " + self.history)
            
            try:
                del self.mySetOfBlocks
            except:
                Nothing = 1
            try:
                del self.myBoard
            except:
                Nothing = 1
            self.myBoard = Board(self.myPattern)
            self.mySetOfBlocks = SetOfBlocks(self.history)
            self.PlaceBlock(0)
            self.endTime = time.time()