from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from time import sleep
driver=Chrome(r"C:\Users\SACHIN\Desktop\training\chromedriver.exe")
#url="https://www.flipkart.com/offers-store"
url="file:///C:/Users/SACHIN/Desktop/demo.html"
driver.get(url)
box=driver.find_element_by_id("standard_cars")
list=Select(box)


driver = webdriver
driver.123
a ="sachin"
b= "sachinks"
c = "sachinsachu"
