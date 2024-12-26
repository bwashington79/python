from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from locust import HttpUser, TaskSet, task, between
import requests
from urllib3.exceptions import InsecureRequestWarning
import json

# #Selenium vars
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30000)

file_path = 'testdata/testdata_sanitized.json'

#BEGIN----Locust
class User(HttpUser):

    # Suppress the warnings from urllib3
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    host = "<enter host url for system under test>"
    request_cookie = None

    def on_start(self):
        self.client.verify = False

#BEGIN----Selenium code block for getting AspNet cookie

    with open(file_path, 'r') as file:
        data = json.load(file)

    usrname_json = data["user_1"]["username"]
    pwd_json = data["user_1"]["password"]

    driver.get(host)

    try:
        username = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "<enter css selector for username field>"))
        )
        print("The username field is visible!")
        username.clear()
        username.send_keys(usrname_json)
        nextbtn = driver.find_element(By.CSS_SELECTOR, "<enter css selector for button>")
        nextbtn.click()

    except TimeoutException:
        print("Timed out waiting for the username text field to be visible!")

    try:
        password = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "<enter css selector for password field>"))
        )
        print("The password field is visible!")
        password.clear()
        password.send_keys(pwd_json)
        verifybtn = driver.find_element(By.CSS_SELECTOR, "<enter css selector for button>")
        verifybtn.click()

    except TimeoutException:
        print("Timed out waiting for the username text field to be visible!")

    try:
        text = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "<enter css for some text that is displayed when page fully loads>"))
        )
        print("anchor text is visible!")

    except TimeoutException:
        print("Timed out waiting for anchor text to be visible!")

    # csv_file_path = 'cookies.csv'

    # headers = ['name', 'value', 'domain', 'path', 'expiry', 'secure', 'httpOnly']

    # with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.DictWriter(file, fieldnames=headers)

    #     writer.writeheader()

    cookies = driver.get_cookies()

    for cookie in cookies:
    # Ensure that all required fields are present, handle missing fields if any
        if cookie["domain"] == "<enter key value for cookie you are looking for>":
            # cookie_data = {
            #     'name': cookie.get('name'),
            #     'value': cookie.get('value'),
            #     'domain': cookie.get('domain'),
            #     'path': cookie.get('path'),
            #     'expiry': cookie.get('expiry', ''),
            #     'secure': cookie.get('secure', ''),
            #     'httpOnly': cookie.get('httpOnly', ''),
            # }
            # writer.writerow(cookie_data)
            cookies[0] = str(cookie.get('value'))
            print("\nThe cookie value is \n")
            request_cookie = ".AspNet.Cookies=" + str(cookies[0])
            print(request_cookie + "\n")

#END----Selenium code block for getting AspNet cookie

    @task()
    def hello_world(self):
        with self.client.get("<enter endpoint>", 
                             headers={"Cookie": self.request_cookie}, allow_redirects=False, catch_response=True) as response:
            print(response.content)

#END----Locust
