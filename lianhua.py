# coding:utf-8
rom appium.webdriver.mobilecommand import MobileCommand
import HTMLTestRunner
import os
import time
import unittest
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://lotus.chinab2bi.com/mainLogon.hlt#")
driver.implicitly_wait(15)
driver.set_window_size(1920, 1080)
driver.find_element_by_xpath("//*[@id='j_username']").send_keys("lt30028667")  # 用户名
driver.find_element_by_xpath("//*[@id='j_password']").send_keys("lianhua,,")  # 密码
driver.find_element_by_xpath("//*[@id='loginForm']/table/tbody/tr[2]/th[1]/table/tbody/tr[6]/td[2]/input").click()
driver.find_element_by_xpath("/html/body/div[10]/div[1]/div[2]/a[2]").click()  # 关闭通知
driver.find_element_by_xpath("/html/body/div[8]/div[1]/div[2]/a[2]").click()  # 关闭通知
driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/a[2]").click()  # 关闭通知dr
driver.find_element_by_xpath("//*[@id='xbd']/div[1]/div[3]/ul/li[3]/a/span[1]").click()  # 供应商门户系统
driver.find_element_by_xpath("//*[@id='menuLeve1_0']/ul/li[4]/div/a").click()  # 购销供应商日销售查询

driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='main-center2']/div[2]/div/div/iframe"))
#  当日下载
driver.find_element_by_xpath("//*[@id='sellModel_salesReportStartDateStart']").click()  # 选择日期
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[12]/iframe"))
driver.find_element_by_xpath("//*[@id='dpTodayInput']").click()    # 选择今天
driver.switch_to.parent_frame()
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='main-center2']/div[2]/div/div/iframe"))
driver.find_element_by_xpath("//*[@id='searchbutton']/span/span").click()  # 点击查询
driver.find_element_by_xpath("//*[@id='row']/tbody/tr/td[2]/a[2]").click()  # PDF 下载
#  当月下载
driver.find_element_by_xpath("//*[@id='list_panel']/tbody/tr[2]/td/div[3]/table/tbody/tr/td[1]/a").click()  # PDF 下载
driver.find_element_by_xpath("//*[@id='dateType']").click()  # 选择当月
driver.find_element_by_xpath("//*[@id='searchbutton']/span/span").click()  # 点击查询
driver.find_element_by_xpath("//*[@id='row']/tbody/tr/td[2]/a[2]").click()  # PDF 下载




time.sleep(5)
driver.quit()









