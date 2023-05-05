from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def pricing():
    driver.get("https://mailchimp.com/")

def signUp():
    driver.get("https://login.mailchimp.com/signup/")

    emailElement = driver.find_element(By.XPATH, "//input[@id='email']")
    emailElement.clear()
    emailElement.send_keys("nhi50@gmail.com")

    # usernameElement = driver.find_element(By.XPATH, "//input[@id='new_username']")
    # usernameElement.clear()
    # usernameElement.send_keys("")

    passwordElement = driver.find_element(By.XPATH, "//input[@id='new_password']")
    passwordElement.clear()
    passwordElement.send_keys(".yym4cAJ389bbGe")

    checkbox = driver.find_element(By.XPATH, "//input[@id='marketing_newsletter']")
    checkbox.click()


    signinButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='create-account-enabled']"))
    )
    driver.execute_script("arguments[0].click();", signinButton)
    try:
        captchaElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='rc-imageselect-payload']")))
        while captchaElement:
            time.sleep(1)
    except:
        pass

    WebDriverWait(driver, 10).until(EC.title_contains("Success"))

    if driver.title  == "Success | Mailchimp":
        print("redirecting to email,")
        openMail = driver.find_element(By.XPATH, "//a[@href='https://mail.google.com/mail/u/0/']")
        openMail.click()
        time.sleep(60)

pricing()
signUp()
