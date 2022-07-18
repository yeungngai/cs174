import random

import numpy as np

randomlist = []

for i in range(0,50):
    n = random.randint(0, 100)
    randomlist.append(n)

M = np.mean(randomlist)
Std = np.std(randomlist)

print(randomlist)
print(M)
print(Std)

