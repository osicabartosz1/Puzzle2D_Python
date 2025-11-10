import time
import os
import sys
from entities.block import Block
from entities.cube import Cube
from entities.board import Board
from entities.holes_finder import HolesFinder
from printer.printer import Printer
from models.set_of_blocks import SetOfBlocks

def PlaceBlock(nr):
	if(nr == 6):
		saveHistory(myBoard.makeHistory())
	if(nr == 18):
		myPrinter = Printer(myBoard);
		myPrinter.printBoard(myBoard.makeHistory())
		print("last history = " + myBoard.makeHistory())
		return True
	while myBoard.moveToNextCorrectPosition(mySetOfBlocks.Zbior[nr]):
		if PlaceBlock(nr + 1):
			return True
	for r in range(nr , 18):
		mySetOfBlocks.Zbior[r].resetPosition()
	return False
def addOne(inputStr, where):
	if len(inputStr) == 0:
		return ""
	last = int(inputStr[len(inputStr) - 1 - where:len(inputStr) - where])
	last = last + 1
	res = inputStr[0:len(inputStr) - 1 - where] + str(last) + len(inputStr[len(inputStr) - where : len(inputStr)]) * "0"
	return res
def pickTheNameOfYoungestFile(folder):
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
def saveHistory(toWrite):
	fhand = open(MainFolder + '\\history.txt','a')
	fhand.writelines(toWrite + '\n')
	fhand.close()
def checkHistory(hist):
	if len(hist) < 54 or (not hist.isdecimal()):
		return "000000000000000000000000000000000000000000000000000000"
	return hist
def selectHistory(folder):
	temp = pickTheNameOfYoungestFile(folder)
	temp = addOne(temp, 1) # 33 - pomijanie podobnych rozwiazan
	return checkHistory(temp)


history = ""
historyEnd = ""
startTime = time.time()
EndTime = time.time()
counter = 0
#Earth Zones
Pattern = ["Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Yellow", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Black", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Blue", "Black", "Yellow", "Black", "Blue", "Black", "Yellow", "Black"]

#Checkerboard
#Pattern = ["Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red", "Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red","Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red","Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black", "Red"]

#Elephant
#Pattern = ["Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Black","Black" ,"Red", "Black", "Red", "Red", "Red", "Black", "Red", "Red", "Black" ,"Red", "Red", "Black", "Black", "Black", "Red", "Black" ,"Red", "Black", "Black", "Black", "Black", "Red", "Black", "Red", "Red" ,"Black", "Black", "Black", "Red", "Black", "Red", "Black" ,"Red", "Black", "Red", "Black", "Red", "Red", "Black", "Red", "Red" ,"Black", "Red", "Black", "Red", "Black", "Red", "Red" ,"Black", "Red", "Black", "Red", "Black", "Red", "Black"]

#Elephant 2
#Pattern = ["Red","Black","Red","Black","Red","Black","Red","Red","Black","Red","Black","Red","Red","Red","Red","Black","Red","Black","Red","Black","Black","Black","Black","Red","Black","Red","Red","Black","Black","Red","Red","Black","Red","Red","Black","Black","Black","Black","Black","Red","Black","Red","Black","Black","Red","Red","Red","Black","Red","Black","Black","Red","Black","Red","Black","Red","Black","Red","Red","Black","Red","Black","Red","Black"]

MainFolder = os.getcwd()
print("Start = " + str(startTime))
print(MainFolder)

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
		history = selectHistory(MainFolder)
		
	if counter == 1 and len(sys.argv) == 2:
		history = sys.argv[1]

	if counter == 1 and len(sys.argv) == 3:
		history = sys.argv[1]
		historyEnd = sys.argv[2]
	
	if counter > 1:
		history = addOne(history, 1)
	
	print( "old  history = " + history)
	
	try:
		del  mySetOfBlocks
	except:
		Nothing = 1
	try:
		del  myBoard
	except:
		Nothing = 1
	myBoard = Board(Pattern)
	myHolesFinder = HolesFinder(myBoard)
	mySetOfBlocks = SetOfBlocks(history)
	PlaceBlock(0)
	EndTime = time.time()

print("End = " + str(EndTime))
print("Time dif = " + str(EndTime - startTime))
