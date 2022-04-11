from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from commen import method
from testdata import data

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = data.data_t.get("url")
username = data.data_t.get("username")
password = data.data_t.get("password")

result = method.search_fun(driver=driver,By=By,url=url,time=time,username=username,password=password)
print(result)