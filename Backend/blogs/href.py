import requests
from bs4 import BeautifulSoup
# import time
# from selenium import webdriver
# # from selenium.webdriver.support import expected_conditions
# # from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import Keys
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.common.exceptions import NoSuchElementException
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import webbrowser


def singhu(p):
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver.get("https://www.google.com/")
    # driver.find_element(By.XPATH, "//input[@title='Search']").send_keys(p)
    # driver.find_element(By.XPATH, "//input[@title='Search']").send_keys(Keys.RETURN)
    webbrowser.open(p)

# fetching all href links
url = 'https://singhania.in/blog'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

list = []
urls = []
for link in soup.find_all('a'):
    # print(link.get('href'))
    list.append(link.get('href'))
    # list = list.append(link.get('href'))

print(list)

# cleaning the href link for the required data
# blog/
for i in list:
    if "blog/" in i:
        # print(i)
        urls.append(i)

proper = []
for u in urls:
    tag = "https://singhania.in/"+u
    proper.append(tag)
print(proper)



new = []
# for y in urls:
#
#     new.append(y)
# print(new)


#cleaning the data
print("\n\n")
for i in urls:
    q = i.replace("blog/", "").replace("-", " ")
    new.append(q)
# print(new)


# basic model
for ff in new:
    print(new.index(ff),".", ff)

o = input("Give the input u want to read:")
print(o)
o = int(o)
p = proper[o]
singhu(p)