from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.about_menu_locator = (By.XPATH, r"/html/body/div[2]/form/div[3]/footer/div/div/div[1]/div[3]/div[1]/div["
                                             r"8]/a")
        self.contacts_link_locator = (By.XPATH, "/html/body/div[2]/form/div[3]/footer/div/div/div[1]/div[3]/div["
                                                "1]/div[8]/a")

    def open(self):
        self.driver.get("https://www.onlyoffice.com")

    def hover_over_about(self):
        about_menu = self.driver.find_element(*self.about_menu_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", about_menu)
        ActionChains(self.driver).move_to_element(about_menu).perform()

    def click_contacts(self):
        contacts_link = self.driver.find_element(*self.contacts_link_locator)
        contacts_link.click()

