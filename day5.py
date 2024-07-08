"""
1)https://demo.guru99.com/test/delete_customer.php
ws to launch demo webpage , click on submit button , print  text  alert and click on ok  and agine print text of alert  and
click ok.

"""
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
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//input[@type='submit']").click()
a = driver.switch_to.alert
print(a.text)
sleep(2)
a.accept()
sleep(3)
b= driver.switch_to.alert
print(b.text)
sleep(2)
b.accept()"""


"""2)httpsin bookmyshow.com/
ws  to launch book my show click on cities, select any city , click hamburger menu , click on login /register ,
click on continue with email and  click continue"""

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
driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//span[.='Bengaluru']").click()
sleep(3)
driver.find_element("xpath", "(//span[.='Bengaluru'])[2]").click()
sleep(3)
driver.find_element("xpath", "//div[@class='bwc__sc-1nbn7v6-13 fcOOgI']").click()
sleep(3)
driver.find_element("xpath", "(//div[.='Login / Register'])[2]").click()
sleep(2)
driver.find_element("xpath", "(//div[@class='bwc__sc-dh558f-10 bUPSGq'])[2]").click()
sleep(3)
driver.find_element("xpath", "//input[@id='emailId']").send_keys("demo@gmail.com")
sleep(2)
driver.find_element("xpath", "//button[.='Continue']").click()

"""

"""
3)https //smallpdf .com/pdf-to-word
ws to upload a pdf and click on ddownload in specific location
"""

f"""rom datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("prefs",{"safebrowsing.enable": True,"download.default_directory":r"C:\Users\Admin\Desktop\web"})
driver = Chrome(options=o)
driver.get("https://smallpdf.com/pdf-to-word")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//input[@id='__picker-input']").send_keys(r"C:\Users\Admin\Desktop\SATYAM_KUMAR.pdf")
sleep(20)
driver.find_element("xpath", "(//span[@class='r5zwp6-3 iiSRjo'])[1]").click()
sleep(5)
"""