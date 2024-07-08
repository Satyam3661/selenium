
"""
ws to launch https://www.redbus.in/
click on account
c;lick on signup
enter the no
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
driver.get("https://www.redbus.in/")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "//span[.='Account']").click()
sleep(3)
driver.find_element("xpath", " //span[.='Login/ Sign Up']").click()
sleep(4)
dd = driver.find_element("xpath", "//iframe[@class='modalIframe']")
driver.switch_to.frame(dd)
sleep(3)
driver.find_element("xpath", "(//input[@class='IP'])[1]").send_keys("9876543219")



"""from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.twitter.com/")
driver.maximize_window()
sleep(3)
bb= driver.find_element("xpath","//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(bb)
driver.find_element("xpath",  "(//span[.='Sign up with Google'])[1]").click()
sleep(8)
driver.switch_to.parent_frame()
driver.find_element("xpath","(//span[.='Sign up with Apple'])[1]").click()
sleep(5)"""
"""ids = driver.window_handles
for i in ids:
    driver.switch_to.window(i)
    sleep(3)
    if "Sign in with Apple" in driver.title:
        driver.maximize_window()
        sleep(3)
        driver.find_element("xpath", "//input[@id='account_name_text_field']").send_keys("9876545439")
        sleep(4)
        driver.find_element("xpath", "//input[@id='password_text_field']").click()

"""




