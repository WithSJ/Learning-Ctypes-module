import ctypes

math = ctypes.CDLL("./math.so")

a = math.add(1,2)

print(a)
