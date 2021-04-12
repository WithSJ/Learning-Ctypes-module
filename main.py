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


print("\n#Use Structure in python with C")

class Point(ctypes.Structure):
    _fields_ = [('x',ctypes.c_int),('y',ctypes.c_int)]

    def __repr__(self):
        return f"({self.x},{self.y})"

point = ctypes.CDLL("./point.so")

show_p = point.__getattr__("show_point")
show_p.argtypes = [Point]
show_p.restype = None


p1 = Point(x=2,y=2)

print(p1)

show_p(p1)
