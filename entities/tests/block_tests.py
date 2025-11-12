import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from entities.block import Block
from entities.cube import Cube

class TestBlock(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie danych")

    def tearDown(self):
        print("Sprzątanie po teście")

    def test_rotation(self):
        k1 = Block(1,2); 
        k1.addCube(Cube(8 ,8 ,"Red", "Black"))
        k1.addCube(Cube(8, 9 ,"Black", "Yellow"))
        k1.clockwiseRotation()
        self.assertEqual(k1.cubes[0].posX , 8)
        self.assertEqual(k1.cubes[0].posY , 8)
        self.assertEqual(k1.cubes[1].posX , 7)
        self.assertEqual(k1.cubes[1].posY , 8)
if __name__ == '__main__':
    unittest.main()
