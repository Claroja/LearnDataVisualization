import matplotlib.pyplot as plt
import numpy as np
"""
X:(array_like,)M*N的灰度图||M*N*3的RGB图||M*N*4的RGBA图.
cmap:(,image.cmap)灰度与颜色的映射,使用默认的cmap,0是紫色255是黄色
"""

img = np.array([
    [0,0,0],
    [0,255,0],
    [0,0,0],
])

plt.figure()
plt.imshow(img,plt.get_cmap("Paired"))
plt.colorbar()
plt.show()