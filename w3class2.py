# 取平均或取總和會如何影響分布
import numpy as np
import matplotlib.pyplot as plt
import random

xbar1 = []
xbar2 = []
xbar3 = []
xbar4 = []
xbar5 = []
n = 1000
sample_size = 16

for i in range(0,n):
  x = [random.uniform(1.0, 0.0) for _ in range(sample_size)]
  xbar1.append(sum(x) / 16)
for i in range(0,n):
  x = [random.uniform(1.0, 0.0) for _ in range(sample_size)]
  xbar2.append(sum(x) / 8)
for i in range(0,n):
  x = [random.uniform(1.0, 0.0) for _ in range(sample_size)]
  xbar3.append(sum(x) / 4)
for i in range(0,n):
  x = [random.uniform(1.0, 0.0) for _ in range(sample_size)]
  xbar4.append(sum(x) / 2)
for i in range(0,n):
  x = [random.uniform(1.0, 0.0) for _ in range(sample_size)]
  xbar5.append(sum(x) / 1)

# xbar2 = [x + 10 for x in xbar2]
# xbar3 = [x + 20 for x in xbar3]
# xbar4 = [x + 30 for x in xbar4]
# xbar5 = [x + 40 for x in xbar5]
plt.hist(xbar1)
plt.show()
plt.hist(xbar2)
plt.show()
plt.hist(xbar3)
plt.show()
plt.hist(xbar4)
plt.show()
plt.hist(xbar5)
plt.show()

# plt.hist(np.log(xbar1))
# plt.show()
# plt.hist(np.log(xbar2))
# plt.show()
# plt.hist(np.log(xbar3))
# plt.show()
# plt.hist(np.log(xbar4))
# plt.show()
# plt.hist(np.log(xbar5))
# plt.show()
