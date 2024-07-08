

"""
ws to launch https:www.byjus.com
enter the name mobile gmail address state , otp click on continue schurdule
for 5 set of input

"""
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions


from xlrd import *
d = {}
wb = open_workbook("../excel/byjus.xlsx")  # control+ space
sh = wb.sheet_by_name("Sheet1")
row_c = sh.nrows
for i in range(1, row_c):
    data = sh.row_values(i)
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://byjus.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys(data[0])
    driver.find_element("xpath","(//input[@type='text'])[2]").send_keys(data[1])
    driver.find_element("xpath", "//button[.='Send OTP']").click()
    driver.find_element("xpath","//input[@name='otp']").send_keys(data[2])
    sleep(3)
    #driver.find_element("xpath","//input[@type='email']").send_keys(data[3])



