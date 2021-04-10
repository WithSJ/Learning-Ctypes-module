[1] Create .c file.

[2] Make shared lib.
    command:[ gcc -fPIC -shared -o math.so math.c ]

[3] Create .py file and import ctypes.

[4] Use CDLL class and give it shared lib path.

[5] Using math object you can call function.