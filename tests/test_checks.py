import pytest
import os
import csv
from selenium import webdriver
from src.main_page import MainPage
from src.contacts_page import ContactsPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def contacts_page(driver):
    return ContactsPage(driver)

def test_navigation_to_contacts(main_page):
    main_page.open()
    main_page.hover_over_about()
    main_page.click_contacts()
    current_url = main_page.driver.current_url
    assert "contacts" in current_url

def test_parse_offices(main_page, contacts_page):
    main_page.open()
    main_page.hover_over_about()
    main_page.click_contacts()
    offices = contacts_page.get_offices()
    assert len(offices) > 0
    for office in offices:
        assert len(office) == 3

def test_save_to_csv(main_page, contacts_page):
    main_page.open()
    main_page.hover_over_about()
    main_page.click_contacts()
    offices = contacts_page.get_offices()

    with open("test_offices.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerow(["Country", "CompanyName", "FullAddress"])
        writer.writerows(offices)


    with open("test_offices.csv", "r", encoding='utf-8') as file:
        lines = file.readlines()
        assert len(lines) > 1

        for line in lines[1:]:
            assert line.count(';') == 2

def test_csv_content(main_page, contacts_page):
    main_page.open()
    main_page.hover_over_about()
    main_page.click_contacts()
    offices = contacts_page.get_offices()

    with open("test_offices.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerow(["Country", "CompanyName", "FullAddress"])
        writer.writerows(offices)

    with open("test_offices.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header = next(reader)
        assert header == ["Country", "CompanyName", "FullAddress"]

        for row in reader:
            assert len(row) == 3
            assert all(row)

@pytest.mark.parametrize("filename", ["test_offices.csv"])
def test_csv_file_exists(main_page, contacts_page, filename):
    main_page.open()
    main_page.hover_over_about()
    main_page.click_contacts()
    offices = contacts_page.get_offices()

    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='\\')
        writer.writerow(["Country", "CompanyName", "FullAddress"])
        writer.writerows(offices)

    assert os.path.isfile(filename)
