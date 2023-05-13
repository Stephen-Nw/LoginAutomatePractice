from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from datetime import datetime


service = Service(r"C:\Development\\chromedriver.exe")


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])   # Remove error message from adding below option"
    options.add_experimental_option("detach", True)   # Keep browswer open
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()
    driver.find_element(By.CSS_SELECTOR, "#id_username").send_keys(
        os.environ.get('AUTOMATE_PYTHON_USERNAME'))
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#id_password").send_keys(
        os.environ.get('AUTOMATE_PYTHON_PASSWORD') + Keys.RETURN)
    time.sleep(2)
    # CLICK HOME BUTTON
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(5)

    element = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/h1[2]/div").text

    output = float(element.split(": ")[1])
    return output


while True:
    time.sleep(2)

    def temp_log():
        temp = main()
        current_date = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        txt_file = f"{current_date}.txt"

        with open(txt_file, 'w') as f:
            f.write(str(temp))

    temp_log()

# print(temp_log())
