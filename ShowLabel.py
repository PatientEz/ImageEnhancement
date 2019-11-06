import  numpy as np
from PIL import Image
import  random
import numpy.ma as ma
import  scipy.misc

#加载图片
img = np.array(Image.open('./output-color.png'))
label = np.array(Image.open('./output-label.png'))

for i in range(label.shape[0]):
    for j in range(label.shape[1]):
        if (label[i][j] == 0):
            label[i][j] = 255

label = Image.fromarray(label)
label.show()
label.save('outl.png')