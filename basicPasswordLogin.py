from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.implicitly_wait(1)

def loginAs(driver, expect):
    user = driver.find_element_by_id('span_unread_reminder').text.split()[1]
    if user != expect:
        print('Error: user should be %s but is %s' % (expect, user))

try:
    driver.get("http://kevinzhang.info")
    loginAs(driver,'游客')
    menuBtn = driver.find_element_by_id('a_target')
    menuBtn.click()
    loginBtn = driver.find_element_by_id('btn_trigger_login')
    loginBtn.click()
    uname = driver.find_element_by_id('input_login_username')
    uname.send_keys("pegasus.xiong@uhubor.com")
    pword = driver.find_element_by_id('input_password')
    pword.send_keys('uhb11')
    loginBtn = driver.find_element_by_id('btn_login')
    loginBtn.click()
    loginAs(driver,'pegasus')
    time.sleep(0.5)
    loginAs(driver,'pegasus')

except Exception as e:
    print(e)

finally:
    driver.quit()