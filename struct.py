from ctypes import *

def wrap_func(lib,funcname,restype,argstypes):
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argstypes = argstypes
    return func


class Vector(Structure):

    __fields__=[('x',c_int),
                ('y',c_int),
                ('z',c_int)]
    
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"



if __name__ == "__main__":
    libvec = CDLL("./libvector.so")
    show = wrap_func(libvec,"show_point",None,[Vector])

    v1 = Vector(1,2,3)
    show(v1)
