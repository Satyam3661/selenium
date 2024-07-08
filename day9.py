from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://canarabank.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("xpath", "//a[@id='eng']").click()
