

def open_page(driver,url):

    driver.implicitly_wait(20)
    driver.get(url)


def login_fun(driver,By,username,password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "btnSubmit").click()


#搜索函数
def search_fun(driver,url,time,By,username,password):
    open_page(driver,url)
    login_fun(driver,By,username,password)

    id = driver.find_element(By.XPATH, "//div[@class='title']/..").get_attribute('id')

    print(id)
    id_iframe = id + "-frame"
    print(id_iframe)

    driver.switch_to.frame(id_iframe)  # 通过id进行切换frame
    time.sleep(1)
    userSum = driver.find_element(By.XPATH, "//span[@id='thisUserSum']").text

    return userSum