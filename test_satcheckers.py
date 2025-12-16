import os
import json 
import time
<<<<<<< HEAD
import argparse
import sys
=======
>>>>>>> 8f2968964b95a427b8b9ed7004b707a5268bc923

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
<<<<<<< HEAD

parser = argparse.ArgumentParser()
parser.add_argument("--is_headless", type=bool, default=False)
args = parser.parse_args()

is_headless = args.is_headless

# Set up Chrome options for Brave
chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Windows
chrome_options.add_argument("--disable-brave-shields")
if is_headless:
    chrome_options.add_argument("--headless")  # Run in headless mode
=======
>>>>>>> 8f2968964b95a427b8b9ed7004b707a5268bc923

# Set up Chrome options for Brave
chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # Windows

# chrome_options.add_argument("--headless")  # Run in headless mode
import smtplib

email = "netalevy2059@gmail.com"
location = "00000" #your zip code
distance = "10 miles" #whatever your want (has to be on the website as an option)
MAX_EMAILS = 10  # Maximum number of emails to send before killing process

class TestSatchecker():
    def __init__(self):
        self.email_count = 0
    def setup_method(self):
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(10)
        self.vars = {}
        self.actions = ActionChains(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def click_on_element(self, element_ref, search_by):
        elements = self.driver.find_elements(search_by, element_ref)
        if len(elements) > 0:
            element = elements[0]
            element.click()

    def test_satchecker(self):
        #self.driver = webdriver.Chrome(r"chromedriver")

        self.driver.get("https://satsuite.collegeboard.org/sat/test-center-search")

        #self.driver.set_window_size(1720, 1349)
        from selenium.webdriver.support.ui import Select

        time.sleep(3)
        self.click_on_element("onetrust-accept-btn-handler", By.ID)
        time.sleep(1)
        self.click_on_element("apricot_radio_4", By.ID)
        time.sleep(1)
        # locate the dropdown element by id
        dropdown = Select(self.driver.find_element(By.ID, "apricot_select_5"))
        time.sleep(1)
        dropdown.select_by_visible_text("March 14, 2026 — Saturday") #change to match your wanted date

        countries_dropdown = Select(self.driver.find_element(By.NAME, "countries"))
        countries_dropdown.select_by_visible_text("Israel")
        self.click_on_element("//button[contains(text(),'Find a Test Center')]", By.XPATH)
        time.sleep(3)
        # Find the element containing the desired text
        self.click_on_element("/html/body/div[1]/div[6]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/fieldset/div[2]/div[3]/label/input", By.XPATH)
        # Extract the text from the element

        # First, locate the div[2] as the search context
        test_centers_div = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]")

        # Next, find all matching h2 elements within div[2]
        test_center_names = test_centers_div.find_elements(By.XPATH, ".//div/div/div/div[1]/h2")
        available_centers = []

        for h2 in test_center_names:
            text = h2.text
            available_centers.append(text)

        if os.path.exists("available_centers.json") and os.path.getsize("available_centers.json") > 0:
            with open("available_centers.json", "r") as file:
                json_data = json.load(file)
                is_subset = set(available_centers).issubset(
                    # set(center for centers in json_data["available_centers"] for center in centers)
                    set(center for center in json_data["available_centers"])
                )
        else:
            is_subset = False

        if not is_subset:
            # Check if too many emails have been sent
            if self.email_count >= MAX_EMAILS:
                print(f"Maximum email limit ({MAX_EMAILS}) reached. Killing process...")
                self.teardown_method()
                os._exit(1)
            
            with open("available_centers.json", "w") as file:
                file.write(json.dumps({"available_centers": available_centers}))
            
            import smtplib

            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login('drbananas481@gmail.com', "ycid widg zbpe awmr")

            # message to be sent
<<<<<<< HEAD
            subject = "SAT Test Center Availability Update"
            body = str(available_centers) + " Testing Centers Open"
            message = "Subject: {}\n\n{}".format(subject, body)
=======
            message = str(available_centers) + " Testing Centers Open"
>>>>>>> 8f2968964b95a427b8b9ed7004b707a5268bc923
            s.sendmail(email, email, message)

            # terminating the session
            s.quit()
<<<<<<< HEAD
            
            # Increment email counter
            self.email_count += 1
            print(f"Email sent ({self.email_count}/{MAX_EMAILS})")
=======
>>>>>>> 8f2968964b95a427b8b9ed7004b707a5268bc923
        time.sleep(3)



# send("completed the test for SAT")

checker = TestSatchecker()

checker.setup_method()
x = 0
while x < 2:
    checker.test_satchecker()
checker.teardown_method()
