from selenium import webdriver
import unittest, time
import page
import locators
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions


class TestScript(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://kevinzhang.info')

    def test_1(self):
        '''Test case 1.'''
        home = page.HomePage(self.driver)
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
