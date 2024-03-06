# 取log會如何影響分布情況
import numpy as np
import matplotlib.pyplot as plt
import random

xbar = []
n = 1000
sample_size = 10

for i in range(0,n):
  x = [random.uniform(1.0, 0.0) for _ in range(sample_size)]
  xbar.append(sum(x) / sample_size)
plt.hist(xbar, color='blue')
plt.hist(np.log(xbar), color='black')
plt.show()
