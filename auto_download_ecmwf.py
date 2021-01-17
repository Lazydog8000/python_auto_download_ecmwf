import time
import os
import sys
from selenium import webdriver
import win32api
import win32con
from selenium.common.exceptions import NoAlertPresentException
import traceback
from urllib import request
import msvcrt
 
# chrome启动地址
chromedriver = "C:/Program Files/Google/Chrome/Application/chromedriver.exe"
# 设置环境变量
os.environ["webdriver.ie.driver"] = chromedriver
# 选择Chrome浏览器,executable_path=chrome
driver=webdriver.Chrome(executable_path=chromedriver) 
# 最大化谷歌浏览器
driver.maximize_window() 
# 打开网站
driver.get('https://www.ecmwf.int/') 

#登陆账号
username = "请填入你的账号" # 请替换成你的用户名
password = r"请填入你的密码" # 请替换成你的密码

#找到登录按钮
driver.find_element_by_xpath("//*[@id=\"navbar-user\"]/ul/li[2]/a").click()
driver.find_element_by_id('username').click() # 点击用户名输入框
driver.find_element_by_id('username').clear() # 清空输入框
driver.find_element_by_id('username').send_keys(username) # 自动敲入用户名

driver.find_element_by_id('password').click() # 点击密码输入框
driver.find_element_by_id('password').clear() # 清空输入框
driver.find_element_by_id('password').send_keys(password) # 自动敲入密码

driver.find_element_by_class_name('btn').click() # 点击“登录”按钮

#进入datasets
driver.find_element_by_xpath("//*[@id=\"node-17581\"]/div/div/div[2]\
    /div/div/div/div/div/div[1]/div/div/div/div[2]/div/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id=\"node-18067\"]/div/div/div/div\
    /div/div/div/div/div[3]/div/div/div/div[2]/div/ul/li[3]/a").click()
driver.find_element_by_xpath("//*[@id=\"block-system-main\"]/ol/li[10]\
    /div[5]/div[3]/div/div/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/button/\
    span").click()
#进入下载页面
#再次登录
driver.find_element_by_xpath("//*[@id=\"header-user\"]/li[2]/a").click()# 登录按钮
'''
driver.find_element_by_id('username').click() # 点击用户名输入框
driver.find_element_by_id('username').clear() # 清空输入框
driver.find_element_by_id('username').send_keys(username) # 自动敲入用户名

driver.find_element_by_id('password').click() # 点击密码输入框
driver.find_element_by_id('password').clear() # 清空输入框
driver.find_element_by_id('password').send_keys(password) # 自动敲入密码
'''

# 采用xpath定位登陆按钮，
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[2]/button/span").click()
#//*[@id="date_year_month"]/div[2]/table/tbody/tr[1]/td[1]/input
driver.find_element_by_xpath("//*[@id=\"date_year_month\"]/div[2]/table\
    /tbody/tr[2]/td[2]/input").click()    #利用xpath查找radio并点击=================
driver.find_element_by_xpath("//*[@id=\"time\"]/div[3]/a[1]").click()
driver.find_element_by_xpath("//*[@id=\"step\"]/div[2]/table/tbody/tr[1]\
    /td/input").click()
driver.find_element_by_xpath("//*[@id=\"param\"]/div[2]/table/tbody/tr[38]\
    /td/input").click()
driver.find_element_by_xpath("//*[@id=\"param\"]/div[2]/table/tbody/tr[39]\
    /td/input").click()
driver.find_element_by_xpath("//*[@id=\"requestForm\"]/button[3]").click()
#//*[@id="requestForm"]/button[3]
driver.find_element_by_xpath("//*[@id=\"area\"]/sub/a").click()
driver.find_element_by_xpath("//*[@id=\"area-custom\"]").click()
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[1]")\
    .clear()
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[1]")\
    .send_keys("50")
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[2]")\
    .clear()
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[2]")\
    .send_keys("90")
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[3]")\
    .clear()
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[3]")\
    .send_keys("0")
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[4]")\
    .clear()
driver.find_element_by_xpath("//*[@id=\"area-custom-container\"]/input[4]")\
    .send_keys("140")
driver.find_element_by_xpath("//*[@id=\"grid\"]/sub/a").click()
driver.find_element_by_xpath("//*[@id=\"grid-0.125/0.125\"]").click()
driver.find_element_by_xpath("//*[@id=\"selectorForm\"]/button").click()
time.sleep(60)
driver.find_element_by_xpath("//*[@id=\"jobresults\"]/div/a").click()
  
print("Press 'space' to exit...")
while True:
  if ord(msvcrt.getch()) in [32]:
        break
