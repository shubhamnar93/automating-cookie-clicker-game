import time
import datetime
from logging import exception

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver=r"C:\developer\chromedriver.exe"
driver=webdriver.Chrome(service=Service(chrome_driver))
driver.get('https://orteil.dashnet.org/cookieclicker/')

def english_clicker():
    try:
        eng=driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
        eng.click()
    except:
        english_clicker()

english_clicker()
time.sleep(5)

click_cookie=driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
cursor_upgrade = driver.find_element(By.XPATH, '//*[@id="product0"]')
grandma_upgrade = driver.find_element(By.XPATH, '//*[@id="product1"]')


now= datetime.datetime.now()
five_minute_from_now=now+datetime.timedelta(minutes=5)
i=0
while datetime.datetime.now()<five_minute_from_now:
    click_cookie.click()
    cookie = int(driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split()[0].replace(',', ''))
    cursor_price = int(driver.find_element(By.XPATH, '//*[@id="productPrice0"]').text.replace(',', ''))
    grandma_price = int(driver.find_element(By.XPATH, '//*[@id="productPrice1"]').text.replace(',', ''))
    try:
        product3_price_upgrade = driver.find_element(By.XPATH, '//*[@id="product2"]')
        product3_price = int(driver.find_element(By.XPATH, '//*[@id="productPrice2"]').text.replace(',', ''))
        if cookie > product3_price:
            product3_price_upgrade.click()
        elif cookie > grandma_price and grandma_price<product3_price/8:
            grandma_upgrade.click()
        elif cookie>cursor_price and cursor_price<grandma_price/8:
            cursor_upgrade.click()
    except:
        pass


driver.quit()
