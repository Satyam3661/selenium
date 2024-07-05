"""
from selenium.webdriver import Chrome
from time import sleep
c = Chrome()
sleep(5)
"""
"""
from selenium.webdriver import Chrome
#ws print currnt web page title
from time import sleep
sleep(5)
driver =Chrome(options=0)
driver.get("http://www.flipkart.com/")
driver.maximize_window()
print(driver.title)
#output----->Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!

"""
#ws to print current webpage title after click on mobiles

"""
from selenium.webdriver import Chrome
from time import sleep

driver =Chrome(options=0)
driver.get("http://www.flipkart.com/")
driver.maximize_window()
# driver.find_element("xpath", "(//span[.='mobile'])[1]").click()
sleep(4)
print(driver.title)
#output----->Mobile Phones Online at Best Prices in India"""

#WS TO VERIFY MOBILES PAGE IS DISPLAYED OR NOT
"""
from selenium.webdriver import Chrome
from time import sleep
driver =Chrome(options=0)
driver.get("http://www.flipkart.com/")
driver.maximize_window()
#driver.find_element("xpath", "(//span[.='mobile'])[1]").click()
sleep(5)
if driver.title== "mobile phone online at best price in india ":
    print("testcase pass")
else:
    print("testcase fail")
#output --->testcase fail  
"""

#ws to print current web page url
"""
from selenium.webdriver import Chrome

driver =Chrome(options=0)
driver.get("https://www.amazone.in/")
driver.maximize_window()
print(driver.current_url)
#https://www.amazone.net/en-in
"""
#WS TO PRINT CURRENT WEBPAGE URL AFTER ON THE BEST SELLERS

"""
from selenium.webdriver import Chrome
driver =Chrome(options=0)
driver.get("https://www.amazone.in/")
driver.maximize_window()
#driver.find_element("xpath", "(//a[@ class='nav-a 1])[4]").click()
print(driver.current_url)
# output https://www.amazone.net/en-in
"""

# ws to print current web page source code
"""from selenium.webdriver import Chrome
from time import sleep
driver =Chrome(options=0)
driver.get("https://www.mesho.com/")
driver.maximize_window()
sleep(5)
print(driver.page_source)

#output sourcecode
"""
"""from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
driver.find_element("id", "gender-male").click()
driver.find_element("name", "FirstName").send_keys("satyam")
driver.find_element("name", "LastName").send_keys("kumar")
driver.find_element("id", "Email").send_keys("satyam9050@gmail.com")
driver.find_element("name", "Password").send_keys("satyam@9050")
driver.find_element("name", "ConfirmPassword").send_keys("satyam@9050")
driver.find_element("id", "register-button").click()"""





from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.google.com/maps/@12.9728512,77.725696,12z?entry=ttu")
driver.maximize_window()
driver.find_element("xpath","//button[@jstcache='27']").click()
sleep(4)
#//div[@id='sb_ifc50'](//input[@class="tactile-searchbox-input"])[1]
driver.find_element("xpath","(//input[@class='tactile-searchbox-input'])[1]").send_keys(" Basavanagudi, Bengaluru, Karnataka")
sleep(2)
driver.find_element("xpath","(//input[@class='tactile-searchbox-input'])[2]").send_keys("btm")
driver.find_element("xpath","(//button[@role='radio'])[3]").click()