import os
import uuid
import cv2

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
    image, contours, hierarchy = cv2.findContours(thresh1, 2, 2)
    for cnt in contours:
        # 最小的外接矩形
        x, y, w, h = cv2.boundingRect(cnt)
        if x != 0 and y != 0 and w*h >= 100:
            print((x,y,w,h))
            # 显示图片
            cv2.imwrite('C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/sample1/%s.jpg'%(uuid.uuid1()), thresh1[y:y+h, x:x+w])

def main():
    dir = "C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/pre_sample"
    for file in os.listdir(dir):
        imagepath = dir+'/'+file
        split_picture(imagepath)

main()
