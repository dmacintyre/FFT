"""
dft.py

Description: 

Donald MacIntyre - djm4912
"""

import math

def buildComplexTable(N):
   base = []
   for k in range(N):
       x = math.cos((2*math.pi*k)/N)
       y = math.sin((2*math.pi*k)/N)
       base.append(complex(x,y))
   return base

def calculateDFT(k,x,unit_circle_vectors):
   y = 0
   angle_inc = 0
   N = len(x)
   for i in x:
       base_vec = unit_circle_vectors[angle_inc]
       angle_inc = (angle_inc + k) % N
       y += base_vec * i
   return y

def main() :
   x = [1,2,3,4]
   res = []
   N = len(x)
   unit_circle_vectors = buildComplexTable(N)
   for i in range(N):
       res.append(calculateDFT(i,x,unit_circle_vectors))

   for k in range(len(res)):
       print('X[' + str(k) + '] = ' + str(res[k]))

if __name__ == "__main__":
   main()
