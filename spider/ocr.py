import tesserocr
import time
from PIL import Image
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://jwc.swjtu.edu.cn/index.html")

time.sleep(4)
driver.find_element_by_link_text('学生信息查询').click()
time.sleep(3)
driver.find_element_by_link_text('登陆系统').click()
time.sleep(3)
driver.find_element_by_id('username').send_keys(2017114954)
driver.find_element_by_id('password').send_keys('lm307726')

driver.save_screenshot("C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/spider/01.png")

# 3、打开截图，获取验证码位置，截取保存验证码
ran = Image.open("C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/spider/01.png")
box = (1030, 301, 1130, 330)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
ran.crop(box).save("C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/spider/02.png")

image = Image.open("C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/spider/02.png")
result = tesserocr.image_to_text(image)
print(result)
time.sleep(1)
driver.find_element_by_name('ranstring').send_keys(result)

driver.find_element_by_id('submit2').click()
