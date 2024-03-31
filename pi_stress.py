import time
import numpy as np
from temp_logger import read_temp

threshold = read_temp()

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



for i in range(100):
    print(fibonacci(i))
    print(read_temp(), "C")
    