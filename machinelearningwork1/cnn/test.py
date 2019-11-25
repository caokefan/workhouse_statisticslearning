# -*- coding: utf-8 -*-

"""
利用训练好的CNN模型对验证码进行识别
（共训练960条数据，训练1000次，loss:0.00059, 测试集上的准确率为%93.45.）
"""
import os
import cv2
import pandas as pd
from VerifyCodeCNN import CNN

def split_picture(imagepath):

    # 以灰度模式读取图片
    gray = cv2.imread(imagepath, 0)

    # 将图片的边缘变为白色
    height, width = gray.shape
    for i in range(width):
        gray[0, i] = 255
        gray[height-1, i] = 255
    for j in range(height):
        gray[j, 0] = 255
        gray[j, width-1] = 255

    # 中值滤波
    blur = cv2.medianBlur(gray, 3) #模板大小3*3

    # 二值化
    ret,thresh1 = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

    # 提取单个字符
    chars_list = []
    image, contours, hierarchy = cv2.findContours(thresh1, 2, 2)
    for cnt in contours:
        # 最小的外接矩形
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w*h >= 100:
            chars_list.append((x,y,w,h))

    sorted_chars_list = sorted(chars_list, key=lambda x:x[0])
    for i,item in enumerate(sorted_chars_list):
        x, y, w, h = item
        cv2.imwrite('C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/test_verifycode/chars/%d.jpg'%(i+1), thresh1[y:y+h, x:x+w])

def remove_edge_picture(imagepath):

    image = cv2.imread(imagepath, 0)
    height, width = image.shape
    corner_list = [image[0,0] < 127,
                   image[height-1, 0] < 127,
                   image[0, width-1]<127,
                   image[ height-1, width-1] < 127
                   ]
    if sum(corner_list) >= 3:
        os.remove(imagepath)

def resplit_with_parts(imagepath, parts):
    image = cv2.imread(imagepath, 0)
    os.remove(imagepath)
    height, width = image.shape

    file_name = imagepath.split('/')[-1].split(r'.')[0]
    # 将图片重新分裂成parts部分
    step = width//parts     # 步长
    start = 0             # 起始位置
    for i in range(parts):
        cv2.imwrite('C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/test_verifycode/chars/%s.jpg'%(file_name+'-'+str(i)), \
                    image[:, start:start+step])
        start += step

def resplit(imagepath):

    image = cv2.imread(imagepath, 0)
    height, width = image.shape

    if width >= 64:
        resplit_with_parts(imagepath, 4)
    elif width >= 48:
        resplit_with_parts(imagepath, 3)
    elif width >= 26:
        resplit_with_parts(imagepath, 2)

# rename and convert to 16*20 size
def convert(dir, file):

    imagepath = dir+'/'+file
    # 读取图片
    image = cv2.imread(imagepath, 0)
    # 二值化
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    img = cv2.resize(thresh, (16, 20), interpolation=cv2.INTER_AREA)
    # 保存图片
    cv2.imwrite('%s/%s' % (dir, file), img)

# 读取图片的数据，并转化为0-1值
def Read_Data(dir, file):

    imagepath = dir+'/'+file
    # 读取图片
    image = cv2.imread(imagepath, 0)
    # 二值化
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # 显示图片
    bin_values = [1 if pixel==255 else 0 for pixel in thresh.ravel()]

    return bin_values

def main():

    VerifyCodePath = 'C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/test_verifycode/03.png'
    dir = 'C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/test_verifycode/chars'
    files = os.listdir(dir)
    """
    # 清空原有的文件
    if files:
        for file in files:
            os.remove(dir + '/' + file)
    """
    #split_picture(VerifyCodePath)

    files = os.listdir(dir)
    if not files:
        print('查看的文件夹为空！')
    else:
        """
        # 去除噪声图片
        for file in files:
            remove_edge_picture(dir + '/' + file)

        # 对黏连图片进行重分割
        for file in os.listdir(dir):
            resplit(dir + '/' + file)
        """
        # 将图片统一调整至16*20大小
        for file in os.listdir(dir):
            convert(dir, file)
        
        # 图片中的字符代表的向量

        table = [Read_Data(dir, file) for file in os.listdir(dir)]
        test_data = pd.DataFrame(table, columns=['v%d'%i for i in range(1,321)])

        # 模型保存地址
        MODEL_SAVE_PATH = 'C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/cnn_verifycode.ckpt'
        # CNN初始化
        cnn = CNN(1000, 0.0005, MODEL_SAVE_PATH)
        y_pred = cnn.predict(test_data)

        # 预测分类
        prediction = []
        labels = 'abcdefghijkLmnopqrstuvwxyz'
        for pred in y_pred:
            label = labels[list(pred).index(max(pred))]
            prediction.append(label)

        print(prediction)


main()