import os
import cv2
import uuid

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
    height, width = image.shape

    # 将图片重新分裂成parts部分
    step = width//parts     # 步长
    start = 0             # 起始位置
    for _ in range(parts):
        cv2.imwrite('C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/sample/%s.jpg'%uuid.uuid1(), image[:, start:start+step])
        start += step

    os.remove(imagepath)

def resplit(imagepath):

    image = cv2.imread(imagepath, 0)
    height, width = image.shape

    if width >= 64:
        resplit_with_parts(imagepath, 4)
    elif width >= 48:
        resplit_with_parts(imagepath, 3)
    elif width >= 26:
        resplit_with_parts(imagepath, 2)

def main():
    dir = 'C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/pre_sample'
    for file in os.listdir(dir):
        remove_edge_picture(imagepath=dir+'/'+file)
    for file in os.listdir(dir):
        resplit(imagepath=dir+'/'+file)

main()
