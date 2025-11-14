import unittest
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.brute_forse import BruteForce
from entities.pattern import Pattern

class TestBruteForse(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie danych")

    def tearDown(self):
        print("Sprzątanie po teście")

    def test_e2e(self):
        with patch.object(sys, "argv",[sys.argv[0], "000000000000000000000000000000000000000000000000000000"]):
            myPattern = Pattern.Earth_Zones.value
            bf = BruteForce(myPattern)
            bf.Run()
            self.assertEqual(bf.history , "437503464756767722542504550500727763540575523546470402")

if __name__ == '__main__':
    unittest.main()