from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@dataclass
class WebSitePage:
    language: str
    def browser_open(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://tribe.com.cy")

    def click_change_language_button (self):
        WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'min-h-screen') and contains(@class,'items-center')]")
            )
        )
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span/parent::button"))).click()

    def click_chose_language_button (self):
        if self.language == "English":
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[text()='ENG']"))).click()
        elif self.language == "Russian":
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[text()='РУС']"))).click()
        elif self.language == "Greek":
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[text()='ΕΛ']"))).click()

    def check_language(self):
        return self.driver.find_element(By.XPATH, "//button/child::span").text
















