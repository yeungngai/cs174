import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('LibraryData.csv')

print(data)

plt.hist(data["books"], color = "pink", ec = "black", bins = 20)
plt.xlabel("Books On Shelf", fontsize = 14)
plt.ylabel("Frequency", fontsize = 14)
plt.savefig("LibraryDataHistogram.png", dpi = 300)
plt.show()


# Length
n = len(data["books"])
print('Length:', n)

# Mean
M = np.sum(data["books"]) / n
print('Mean:', M)

# Deviations
devs = data["books"] - M

# Squared Deviations
devs_sqrd = devs ** 2

# Sum of the Squared Deviations
SS = np.sum(devs_sqrd)
print('SS:', SS)

variance = SS/(n-1)
s = np.sqrt(variance)
print('Standard Deviations:', s)
