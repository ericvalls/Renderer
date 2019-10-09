import numpy as np
import matplotlib.pyplot as plt
import math


f= open("a.txt","r")
contents = f.readlines()
for i in range(0, len(contents)):
    contents[i] = int(contents[i])

print "---"
print len(contents)

square = int(math.sqrt(len(contents)/4))

contents2 = [[] for i in range (0, square)]


for i in range(0, len(contents)/4):
    contents2[i/square] += [[int(contents[4*i + j]) for j in range (0,3)]]

#print contents2
print square

#print len(contents2[-1])


plt.imshow(contents2);
plt.colorbar()
plt.show()
