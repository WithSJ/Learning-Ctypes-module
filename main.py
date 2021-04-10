import ctypes
from time import time

math = ctypes.CDLL("./math.so")

print("\n#Use add function")
print("Add number ",math.add(1,2))

print("\n#Use loopFmul and cal time it takes")
S = time()

print("loops : ",math.loopFmul(1000000))

E = time()

print("Time in sec: ",E-S)




