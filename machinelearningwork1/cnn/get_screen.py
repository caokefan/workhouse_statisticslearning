import time
from selenium import webdriver

def get_screen(n):
    driver = webdriver.Firefox()
    driver.get("http://jwc.swjtu.edu.cn/index.html")
    time.sleep(2)
    driver.find_element_by_link_text('学生信息查询').click()
    time.sleep(2)
    driver.find_element_by_link_text('登陆系统').click()
    time.sleep(2)
    for i in range(n):
        driver.save_screenshot("C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/screen/0{}.png".format(i))
        driver.find_element_by_link_text('(更换)').click()
        print("已截图%d张" % i)

if __name__ == '__main__':
    get_screen(200)