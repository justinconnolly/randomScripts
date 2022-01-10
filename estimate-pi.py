from random import random
from math import sqrt

def estimate_pi(n: int) -> int:
  in_circle = 0
  total = 0
  for i in range(n):
    xCoord = random()
    yCoord = random()
    if sqrt(xCoord**2 + yCoord**2) <= 1:
      in_circle += 1
    total += 1
  return 4 * in_circle / total
