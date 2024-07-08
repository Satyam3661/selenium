"""
launch amazon.in
click on mobiles
click on any mobile (like poco...)
clickon any phone
slect quantity as 3 and click on add to cart
click on proceed to check out
enter mail and log in
"""

from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
driver.find_element("xpath","(//a[@class='nav-a  '])[5]").click()
sleep(3)
driver.find_element("xpath", "(//span[.='Redmi'])[2]").click()
sleep(4)
driver.find_element("xpath", "//span[.='Redmi 13C 5G (Startrail Silver, 4GB RAM, 128GB Storage) | MediaTek Dimensity 6100+ 5G | 90Hz Display']").click()
sleep(5)
#####yaha se wrong
driver.find_element("xpath","(//input[@title='Add to Shopping Cart'])[2]").click()
sleep(5)
ids =driver.window_handles
ds = driver.switch_to.window(ids[1])
sleep(3)
d = driver.find_element("xpath", "//select[@name='quantity']")
sleep(2)
s =Select(d)
s.select_by_visible_text("3")
driver.find_element("xpath","(//input[@id='add-to-cart-button'])[2]").click()
sleep(10)
driver.find_element("xpath" , "//span[@id='attach-sidesheet-checkout-button']").click()
sleep(4)
driver.find_element("xpath", "//input[@type='email']").send_keys("demo@gmail.com")
sleep(2)
driver.find_element("xpath", "//input[@id='continue']").click()




