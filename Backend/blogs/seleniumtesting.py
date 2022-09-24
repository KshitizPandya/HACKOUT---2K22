import time
from selenium import webdriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def singhu(a, b):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://singhania.in/blog/")
    driver.find_element(By.XPATH, a).click()
    time.sleep(15)

    # driver.find_element(By.XPATH, b).click()
    # time.sleep(5)
    driver.find_element(By.XPATH, b).click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, b))).click()
    time.sleep(5)

print("Select the blog u want to read:")
list = ["//div[@class='post format-standard-image']//a[contains(text(),'Physical Verification of Registered office')]", "//div[@class='post format-standard-image']//a[contains(text(),'Shareholder has no right to litigate on behalf of ')]", ]

for i in list:
    print(list.index(i),".", i)
take = input("give input: ")
print(take)
x = int(take)
a = "//a[@href='blog']"
b = list[x]
singhu(a, b)
# print(b)