import  numpy as np
from PIL import Image
import  random
import numpy.ma as ma
import  scipy.misc

#加载图片
img = np.array(Image.open('./000001-color.png'))
#坐标转换 这样才可以与掩码相乘
img = np.transpose(img,(2,0,1))

label = Image.open('./000001-label.png')



#加载前景图片 使用其中的两个类
front = np.array(Image.open('./000003-color.png'))
#坐标转换 这样才可以与掩码相乘
front = np.transpose(front, (2, 0, 1))

f_label =  np.array(Image.open('./000003-label.png'))
#获取前景图片的label 删去0即背景
front_label = np.unique(f_label).tolist()[1:]

if len(front_label) < 2:
    print('前景图片少于两类')
else:
    front_label = random.sample(front_label, 2)
    for f_i in front_label:
        mk = ma.getmaskarray(ma.masked_not_equal(f_label, f_i))
        # 第一次
        if f_i == front_label[0]:
            mask_front = mk
        else:
            # 得到的结果为  值不为front_label 的为True  值为front_label 的为 False
            mask_front = mask_front * mk

    label_masked = label * mask_front  + f_label * ~mask_front

    img_masked = img * mask_front + front * ~mask_front

    # 加入高斯噪声
    #img_masked = img_masked + np.random.normal(loc=0.0, scale=7.0, size=img_masked.shape)

    #存储
    img_masked = np.transpose(img_masked, (1, 2, 0))
    scipy.misc.imsave('./output-color.png', img_masked)
    scipy.misc.imsave('./output-label.png',label_masked)
    # img_masked = Image.fromarray(img_masked)
    # img_masked.save('./output-color.png')
