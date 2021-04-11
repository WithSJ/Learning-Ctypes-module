import ctypes
from time import time,sleep

math = ctypes.CDLL("./math.so")

print("\n#Use add function")
print("Add number ",math.add(1,2))

print("\n#Use loopFmul and cal time it takes")
S = int(time())

print("loops : ",math.loopFmul(100000000))
# sleep(2)

E = int(time())

print("Time in sec: ",E-S)




