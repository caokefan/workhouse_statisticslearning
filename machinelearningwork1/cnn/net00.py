import os
import cv2
import uuid

def convert(dir, file):

    imagepath = dir+'/'+file
    # 读取图片
    image = cv2.imread(imagepath, 0)
    # 二值化
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    img = cv2.resize(thresh, (16, 20), interpolation=cv2.INTER_AREA)
    # 显示图片

    cv2.imwrite('%s/%s.jpg' % (dir, uuid.uuid1()), img)
    os.remove(imagepath)

def main():
    chars = 'abcdefghijkLmnopqrstuvwxyz'
    dirs= ['C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/sample/%s'%char for char in chars]
    for dir in dirs:
        for file in os.listdir(dir):
            convert(dir, file)

main()