from selenium.webdriver.common.by import By

class ContactsPage:
    def __init__(self, driver):
        self.driver = driver
        self.office_locator = (By.CSS_SELECTOR, "div.companydata[itemscope]")

    def get_offices(self):
        office_elements = self.driver.find_elements(*self.office_locator)
        offices = []
        for office in range(1, len(office_elements) + 1):
            country = self.driver.find_element(By.CSS_SELECTOR, f"div.companydata:nth-child({office}) > span:nth-child(1)").text.strip()
            company_name = self.driver.find_element(By.CSS_SELECTOR, f"div.companydata:nth-child({office}) > span:nth-child(2) > b:nth-child(1)").text.strip()
            address = self.driver.find_element(By.CSS_SELECTOR,
                                          f"div.companydata:nth-child({office}) > span:nth-child(3)").text.strip()

            try:
                address2 = self.driver.find_element(By.CSS_SELECTOR,
                                               f"div.companydata:nth-child({office}) > span:nth-child(4)").text.strip()
                address3 = self.driver.find_element(By.CSS_SELECTOR,
                                               f"div.companydata:nth-child({office}) > span:nth-child(5)").text.strip()
            except:
                address2 = ""
                address3 = ""
            try:
                phone = self.driver.find_element(By.CSS_SELECTOR,
                                            f"div.companydata:nth-child({office}) > span[itemprop='telephone']").text.strip()
            except:
                phone = ""

            full_address = f'{address}{address2}{address3} {phone}'
            offices.append([country, company_name, full_address])
        return offices