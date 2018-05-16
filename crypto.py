#Crypto
import numpy, random

STARTING_SIMPLE_NUMBER=571828182881

q=STARTING_SIMPLE_NUMBER
random.seed()
r=random.randint(q+1, 4*q+2)
print(r)
p=q*r+1
print(p)