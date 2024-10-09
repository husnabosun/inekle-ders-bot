import json
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playsound import playsound
from webdriver_manager.chrome import ChromeDriverManager


INEKLE_EMAIL = 'email_address'
INEKLE_PASSWORD = 'password'


def login_inekle(driver):
    try:
        print('Waiting for the login...')
        driver.get('https://inekle.com/uye-girisi')
        email_field = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.NAME, "UserName")))
        password_field = driver.find_element(By.NAME, 'Password')
        email_field.send_keys(INEKLE_EMAIL)
        password_field.send_keys(INEKLE_PASSWORD)

        login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-green.btn-38h")
        login_button.click()

        print('waiting for the login after items')
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-green.btn-30h"))
        )
        print('Login has successfully completed.')
    except Exception as e:
        print(f"An error occured during login: {e}")
        driver.quit()
        exit()


def check_lesson_pool(driver):
    try:
        print('searching for lessons')
        driver.get("https://inekle.com/ogretmen/#/")
        empty_lesson_pool = WebDriverWait(driver, 40).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "qflex-body.pool-empty-content.visible.ng-scope"))
        )
        if empty_lesson_pool:
            return True
        else:
            print('Ders havuzuna ders düştü')
            playsound('Crystal.mp3')
            return False
    except Exception as e:
        print(f"Ders havuzunu kontrol ederken bir hata oluştu:{e}")
        return None


# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Extract configuration values
urls_to_check = config["urls"]
sleep_min_seconds = config["sleep_min_seconds"]
sleep_max_seconds = config["sleep_max_seconds"]
chrome_driver_path = config["chrome_driver_path"]

while True:
    # Create a service object with the path to ChromeDriver from the config

    # Set Chrome options
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())

    # Initialize the Chrome driver with the service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        for url in urls_to_check:
            try:
                login_inekle(driver)
                while True:
                    found = check_lesson_pool(driver)
                    if found is None:
                        print('an error occured during checking')
                        break
                    time.sleep(10)
            except Exception as e:
                print(f"An error occurred :{e}")
    finally:
        print("Closing the browser...")
        driver.quit()

        # Sleep for a random time between the specified min and max seconds before the next check
        sleep_time = random.randint(sleep_min_seconds, sleep_max_seconds)
        print(f"Sleeping for {sleep_time // 60} minutes and {sleep_time % 60} seconds...")
        time.sleep(sleep_time)
