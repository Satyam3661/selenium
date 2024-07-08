
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
def take_screenshort():
    d = datetime.now().strftime("%d-%m-%Y %H-%M %S")
    driver.save_screenshot(f"./deffect/{d}.png")
def verify_url(url):
    assert driver.current_url == url, take_screenshort()
def verify_title(etitle):
    assert driver.title == etitle, take_screenshort()

driver = Chrome(options=o)
driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
driver.maximize_window()
verify_title("Movie Tickets, Plays, Sports, Events & Cinemas near Bengaluru - BookMyShow Bengaluru.")
sleep(5)
driver.find_element("xpath", "//a[.='Movies']").click()
sleep(5)
verify_url("https://i.bookmyshow.com/explore/movies-bengaluru")
sleep(5)
driver.find_element("xpath", "(//div[@class='sc-7o7nez-0 beKeQH'])[3]").click()
sleep(5)
verify_url("https://in.bookmyshow.com/explore/movies-bengaluru?languages=hindi")
sleep(5)
"""driver.find_element("xpath", "(//div[.='Godzilla x Kong: The New Empire'])[1]").click()
sleep(5)
verify_title("Movie Tickets, Plays, Sports, Events & Cinemas near Bengaluru - BookMyShow Bengaluru.")
sleep(5)
driver.find_element("xpath", "(//span[.='Book tickets'])[1]").click()
sleep(5)
verify_title("Movie Tickets, Plays, Sports, Events & Cinemas near Bengaluru - BookMyShow Bengaluru.")"""


