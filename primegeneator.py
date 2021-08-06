#def primeGeneator(argv):
import math
import time
prime = []

start = time.time()
for num1 in range(0,10000 + 1):
        primeNum = True

        for num2 in range(2,num1):
            if (num1 % num2 == 0):
             primeNum = False
            stop = time.time()


       #if primeNum:
            #print(num1)

print(stop - start)
