# Gradient descent practice

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import imageio
import os

# 方程式區
def f(x):
    return x**2

def gradient(x):
    return 2*x

def gradient_descent(x0, learning_rate, num_iterations):
    x_history = [x0]
    for i in range(num_iterations):
        x_new = x_history[-1] - learning_rate * gradient(x_history[-1])
        # x_history[-1] 表示列表中最後一個元素，即上一次迭代後的 x 值
        x_history.append(x_new)
    return x_history

# 創建資料夾
output_folder = 'gradient_descent_test'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 參數區
x0 = 3.0
learning_rate = 0.01
num_iterations = 300

# 執行
x_history = gradient_descent(x0, learning_rate, num_iterations)

# 繪製動畫
fig, ax = plt.subplots()

x_values = np.linspace(-5, 5, 100)
y_values = f(x_values)
ax.plot(x_values, y_values, 'k-')

line, = ax.plot([], [], 'r-', lw=2)
point, = ax.plot([], [], 'ro')

def animate(i):
    x = x_history[i]
    y = f(x)
    line.set_data([x, x], [0, y])
    point.set_data(x, y)
    return line, point

ax.set_xlim(-3.5, 3.5)
ax.set_ylim(0, 12.25)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# 逐幀生成並保存圖像
frames = []
colors = ScalarMappable(norm=Normalize(0, len(x_history)), cmap='gist_rainbow').to_rgba(range(len(x_history)))
# https://matplotlib.org/stable/users/explain/colors/colormaps.html
for i in range(len(x_history)):
    ax.plot(x_history[i], f(x_history[i]), 'o', color=colors[i])  # 繪製當前點
    fig.canvas.draw()
    image = np.array(fig.canvas.renderer.buffer_rgba())
    frames.append(image)

# 使用圖像列表生成 gif
gif_file_path = os.path.join(output_folder, 'gradient_descent_test(3,0.01,300).gif')
imageio.mimsave(gif_file_path, frames, fps=3)

print("GIF已完成")
