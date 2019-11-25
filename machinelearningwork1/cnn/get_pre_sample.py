from PIL import Image
import cv2

def get_code(n):
    for i in range(n):
        ran = Image.open("C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/screen/0{}.png".format(i))
        box = (1030, 300, 1130, 340)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
        ran.crop(box).save("C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/pre_sample/0{}.png".format(i))

if __name__ == '__main__':
    get_code(200)