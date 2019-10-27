import matplotlib.pyplot as plt
import numpy as np
"""
nrows:(int,)行数
ncols:(int,)列数
index:(int,)索引,从1开始
"""

img = np.array([
    [0,0,0],
    [0,255,0],
    [0,0,0],
])

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)  # 注意subplot第一个是从1开始所以是i+1
    plt.xticks([])  # 隐藏xticks
    plt.yticks([])  # 隐藏yticks
    plt.imshow(img, cmap=plt.cm.binary)
    plt.xlabel(i+1)
plt.show()