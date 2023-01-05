import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        self.driver.find_element(By.ID, 'checkbox-header').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div/form/input[2]').click()
        self.driver.get_screenshot_as_file('mod5_housework.jpg')

