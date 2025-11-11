from core.brute_forse import BruteForce
from entities.pattern import Pattern

myPattern = Pattern.Earth_Zones.value

bf = BruteForce(myPattern)
bf.Run()
