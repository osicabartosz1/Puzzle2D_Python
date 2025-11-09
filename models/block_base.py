from models.rectangle import Rectangle

class BlockBase:
	def __init__(self, inOrder, numberOfCubes):
		self.order = inOrder
		self.count = numberOfCubes
		self.cubes = []
		self.rotation = 0
		self.rect = Rectangle(8,8,8,8)
	def __del__(self):
		Nothing = 1