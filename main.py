from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=driver_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID,"cookie")
buy_timer = time.time() + 5
wait = WebDriverWait(driver, 10)

def buy_from_store():
    global buy_timer
    to_click = True
    while to_click:
        store_items = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "#store div[id^='buy']")))
        money = int(driver.find_element(By.ID, "money").text.replace(",",""))

        costs = ([int(item.find_element(By.TAG_NAME, "b")
                      .text.replace(",","")
                      .split(sep=" ")[-1])
                  for item in store_items
                  if item.find_element(By.TAG_NAME,"b").text != ""])

        min_cost = min(costs)
        if money < int(min_cost):
            to_click = False
        else:
            for item in store_items:
                if item.find_element(By.TAG_NAME,"b").text == "":
                    continue
                item_cost = int(item.find_element(By.TAG_NAME, "b").text.replace(",","").split(sep=" ")[-1])
                if min_cost == item_cost:
                    item.click()
                    time.sleep(0.2)
                    break
    buy_timer = time.time() + 5

try:
    while True:
        cookie.click()
        if time.time() >= buy_timer:
            buy_from_store()
except KeyboardInterrupt:
    print("\nProgram terminated by user.")






