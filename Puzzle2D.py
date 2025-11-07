import time
import os
import sys
from entities.block import Block
from entities.cube import Cube
from entities.board import Board
from entities.holes_finder import HolesFinder


class setOfBlocks:
	Zbior = []
	def __init__(self, history):
		i = 1
		k1 = Block(1,8)
		k1.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addCube(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Yellow"))
		k1.addCube(Cube(8 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addCube(Cube(8 + int(history[i:i+1]),11 + int(history[i+1:i+2]),"Black", "Blue"))
		k1.addCube(Cube(8 + int(history[i:i+1]),12 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addCube(Cube(8 + int(history[i:i+1]),13 + int(history[i+1:i+2]),"Black", "Yellow"))
		k1.addCube(Cube(8 + int(history[i:i+1]),14 + int(history[i+1:i+2]),"Red", "Black"))
		k1.addCube(Cube(8 + int(history[i:i+1]),15 + int(history[i+1:i+2]),"Black", "Blue"))
		for j in range(int(history[i-1:i])):
			k1.clockwiseRotation()
		self.Zbior.append(k1)
		i = 4
		k2 = Block(2,4)
		k2.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Black", "Blue"))
		k2.addCube(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Red", "Black"))
		k2.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Black", "Yellow"))
		k2.addCube(Cube(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Red", "Black"))
		for j in range(int(history[i-1:i])):
			k2.clockwiseRotation()
		self.Zbior.append(k2)
		i = 7
		k3 = Block(3,4)
		k3.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k3.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Blue"))
		k3.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Black"))
		k3.addCube(Cube(9 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red","Yellow"))
		for j in range(int(history[i-1:i])):
			k3.clockwiseRotation()
		self.Zbior.append(k3)
		i = 10
		k4 = Block(4,4)
		k4.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Blue"))
		k4.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Black"))
		k4.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Yellow"))
		k4.addCube(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Yellow"))
		for j in range(int(history[i-1:i])):
			k4.clockwiseRotation()
		self.Zbior.append(k4)
		i = 13
		k5 = Block(5,4)
		k5.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Yellow"))
		k5.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Black"))
		k5.addCube(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red", "Black"))
		k5.addCube(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Blue"))
		for j in range(int(history[i-1:i])):
			k5.clockwiseRotation()
		self.Zbior.append(k5)
		i = 16
		k6 = Block(6,4)
		k6.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k6.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Blue"))
		k6.addCube(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k6.addCube(Cube(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red", "Yellow"))
		for j in range(int(history[i-1:i])):
			k6.clockwiseRotation()
		self.Zbior.append(k6)
		i = 19
		k7 = Block(7,4)
		k7.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Red", "Black"))
		k7.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]), "Red", "Black"))
		k7.addCube(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Red", "Black"))
		k7.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]), "Black", "Blue"))
		for j in range(int(history[i-1:i])):
			k7.clockwiseRotation()
		self.Zbior.append(k7)
		i = 22
		k8 = Block(8,4)
		k8.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black" ,"Black"))
		k8.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k8.addCube(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k8.addCube(Cube(11 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Blue"))
		for j in range(int(history[i-1:i])):
			k8.clockwiseRotation()
		self.Zbior.append(k8)
		i = 25
		k9 = Block(9,4)
		k9.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Yellow"))
		k9.addCube(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red","Black"))
		k9.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Blue"))
		k9.addCube(Cube(9 + int(history[i:i+1]),10 + int(history[i+1:i+2]),"Red","Black"))
		for j in range(int(history[i-1:i])):
			k9.clockwiseRotation()
		self.Zbior.append(k9)
		i = 28
		k10 = Block(10,4)
		k10.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k10.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Yellow"))
		k10.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Black"))
		k10.addCube(Cube(10 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red","Blue"))
		for j in range(int(history[i-1:i])):
			k10.clockwiseRotation()
		self.Zbior.append(k10)
		i = 31
		k11 = Block(11,4)
		k11.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Yellow"))
		k11.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Black"))
		k11.addCube(Cube(8 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red","Black"))
		k11.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Blue"))
		for j in range(int(history[i-1:i])):
			k11.clockwiseRotation()
		self.Zbior.append(k11)
		i = 34
		k12 = Block(12,3)
		k12.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k12.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		k12.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Red", "Blue"))
		for j in range(int(history[i-1:i])):
			k12.clockwiseRotation()
		self.Zbior.append(k12)
		i = 37
		k13 = Block(13,3)
		k13.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black", "Black"))
		k13.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k13.addCube(Cube(9 + int(history[i:i+1]),9 + int(history[i+1:i+2]),"Black", "Black"))
		for j in range(int(history[i-1:i])):
			k13.clockwiseRotation()
		self.Zbior.append(k13)
		i = 40
		k14 = Block(14,3)
		k14.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		k14.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k14.addCube(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		for j in range(int(history[i-1:i])):
			k14.clockwiseRotation()
		self.Zbior.append(k14)
		i = 43
		k15 = Block(15,3)
		k15.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Yellow"))
		k15.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Black"))
		k15.addCube(Cube(10 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red", "Blue"))
		for j in range(int(history[i-1:i])):
			k15.clockwiseRotation()
		self.Zbior.append(k15)
		i = 46
		k16 = Block(16,2)
		k16.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Black"))
		k16.addCube(Cube(9 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Blue"))
		for j in range(int(history[i-1:i])):
			k16.clockwiseRotation()
		self.Zbior.append(k16)
		i = 49
		k17 = Block(17,1)
		k17.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Black","Blue"))
		for j in range(int(history[i-1:i])):
			k17.clockwiseRotation()
		self.Zbior.append(k17)
		i = 52
		k18 = Block(18,1)
		k18.addCube(Cube(8 + int(history[i:i+1]),8 + int(history[i+1:i+2]),"Red","Black"))
		for j in range(int(history[i-1:i])):
			k18.clockwiseRotation()
		self.Zbior.append(k18)
	def __del__(self):
		self.Zbior.clear()
def PlaceBlock(nr):
	if(nr == 6):
		saveHistory(myBoard.makeHistory())
	if(nr == 18):
		myBoard.printBoard(myBoard.makeHistory())
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
	mySetOfBlocks = setOfBlocks(history)
	PlaceBlock(0)
	EndTime = time.time()

print("End = " + str(EndTime))
print("Time dif = " + str(EndTime - startTime))
