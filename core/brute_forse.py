import time
import os
import sys
from entities.board import Board
from printer.printer import Printer
from models.set_of_blocks import SetOfBlocks
from helpers.file_helper import FileHelper

class BruteForce():
    def __init__(self, inPattern):
        self.myPattern = inPattern
        self.FileHelper = FileHelper()

    def PlaceBlock(self, nr):
        if(nr == 6):
            self.FileHelper.saveHistory(self.myBoard.makeHistory())
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

    def Run(self):
        history = ""
        historyEnd = ""
        startTime = time.time()
        EndTime = time.time()
        counter = 0

        print("Start = " + str(startTime))

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
                history = self.FileHelper.selectHistory()
                
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
            self.mySetOfBlocks = SetOfBlocks(history)
            self.PlaceBlock(0)
            EndTime = time.time()

        print("End = " + str(EndTime))
        print("Time dif = " + str(EndTime - startTime))
