import csv
import time
import sys
import os
from selenium import webdriver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main_page import MainPage
from src.contacts_page import ContactsPage



def test_offices(path):
    driver = webdriver.Firefox()

    try:
        main_page = MainPage(driver)
        contacts_page = ContactsPage(driver)

        main_page.open()
        time.sleep(5)

        main_page.hover_over_about()
        time.sleep(2)

        main_page.click_contacts()
        time.sleep(5)

        offices = contacts_page.get_offices()

        with open(path, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writerow(["Country", "CompanyName", "FullAddress"])
            writer.writerows(offices)

    finally:
        driver.quit()

def interface():
    path = str(input())
    test_offices(path)

if __name__ == '__main__':
    interface()