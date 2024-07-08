#ActionChains


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://byjus.com/")
driver.maximize_window()
sleep(3)
ele1=driver.find_element("xpath","//a[.='Study Materials']")
a = ActionChains(driver)
a.move_to_element(ele1).perform()
sleep(3)
ele2 = driver.find_element("xpath","(//a[.='CBSE'])[1]")
a1 = ActionChains(driver)
a1.move_to_element(ele2).perform()
sleep(3)
ele3=driver.find_element("xpath","//a[.='PHYSICS']")
a2 = ActionChains(driver)
a2.move_to_element(ele3).perform()
sleep(3)
ele4 = driver.find_elements("xpath","(//ul[@class='more-less-open'])[1]/li")
sleep(3)
for i in ele4:
    print(i.text)

"""Mechanics
Optics
Thermodynamics
Electromagnetism
Famous Physicists
Unit Conversion
Kirchhoff's Laws
Faraday's Law
Laws of Motion
Refraction of Light
Maxwell's Equation
Electrostatics
Bernoulli's Principle
Projectile Motion"""



"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()
sleep(3)
scr = driver.find_element("xpath","(//li[@class='block13 ui-draggable'])[2]")
dest =driver.find_element("xpath","(//div[@class='ui-widget-content'])[3]")
a= ActionChains(driver)
a.drag_and_drop(scr,dest).perform()
s=driver.find_element("xpath","//li[@data-id='5']" 
)
d=driver.find_element("xpath","(//div[@class='ui-widget-content'])[2]")
a1= ActionChains(driver)
a1.drag_and_drop(s,d).perform()
"""




"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
sleep(3)
ele= driver.find_element("xpath","//span[.='right click me']")
sleep(3)
a1= ActionChains(driver)
a1.context_click(ele).perform()

"""