# Praca domowa moduł 6
# 1. odwiedź stronę http://simpletestsite.fabrykatestow.pl/
# 2. kliknij w zakładkę iframe
# 3. kliknij Przycisk 1
# 4. zrób screena strony tak, aby widać było całą zakładkę iframe i zapisz go w projekcie

import unittest
from helpers.iframe import *

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://simpletestsite.fabrykatestow.pl/'
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1(self):
        click_iframe_tab(self.driver)
        click_inside_iframe(self.driver)
        self.driver.get_screenshot_as_file('mod6_housework.jpg')