from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://jwc.swjtu.edu.cn/index.html")

time.sleep(4)
driver.find_element_by_link_text('学生信息查询').click()
time.sleep(3)
driver.find_element_by_link_text('登陆系统').click()
time.sleep(3)
driver.find_element_by_id('username').send_keys(2017114954)
driver.find_element_by_id('password').send_keys('lm307726')

time.sleep(10)

driver.find_element_by_id('submit2').click()
time.sleep(3)
driver.find_element_by_link_text('返回刚才访问的页面').click()
time.sleep(3)
driver.find_element_by_link_text('新生信息').click()
time.sleep(2)
driver.find_element_by_name('keyword').send_keys('四川省')
time.sleep(8)
driver.find_element_by_name('btnl').click()

