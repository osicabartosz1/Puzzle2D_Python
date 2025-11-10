from entities.cube import Cube
from entities.block import Block

class SetOfBlocks:
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