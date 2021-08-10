from selenium import webdriver
import time
import csv
import pandas as pd
from webdriver_manager.firefox import GeckoDriverManager

username = "mschrier@uw.edu"
password = "Mountrainier1!"

job_counter = 0
page_counter = 1

def pages(page):
    num_page = page.text
    num_page = num_page.split("/")

    return int(num_page[1])


details = []

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://uw.joinhandshake.com/login?ref=open-in-new-tab")

driver.find_element_by_id("sso-name").click()
time.sleep(10)
driver.find_element_by_id("weblogin_netid").send_keys(username)
driver.find_element_by_id("weblogin_password").send_keys(password)
driver.find_element_by_id("submit_button").click()
time.sleep(20)
driver.find_element_by_xpath("//span[contains(text(),'Jobs')]").click()
time.sleep(10)

num_of_pages = pages(driver.find_element_by_class_name("style__page___1UaFT"))
print(num_of_pages)

for page in range(2):
    time.sleep(5)
    left_column = driver.find_element_by_class_name("style__cards___2bvJ9")
    x = left_column.find_elements_by_tag_name('a')

    for i in x:
        time.sleep(2)
        title = driver.find_element_by_xpath("//div[@class='style__job-title___28HlN']")

        try:
            location = driver.find_element_by_class_name("style__list-with-tooltip___2c5rW")
            location = location.text
        except:
            location = 'worldwide'

        type_of_job = driver.find_element_by_class_name("style__job-type-info___2oQHN")

        deadline = driver.find_element_by_class_name('style__content___3I6Ej')

        details.append({"title": title.text, "location": location, "type_of_job": type_of_job.text, "deadline": deadline.text})

        time.sleep(1)
        i.click()
        print(details)
    
    driver.find_element_by_css_selector("svg.svg-inline--fa.fa-chevron-right.fa-w-10.style__left-icon___1hSd_.icon").click()

df = pd.DataFrame.from_dict(details)
df.to_csv("jobs.csv")
