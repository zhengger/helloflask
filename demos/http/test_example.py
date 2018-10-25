# _*_ coding: utf-8 _*_
import unittest
from selenium import webdriver


class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_PageTitle(self):
        self.browser.get('https://www.bing.com')
        print(self.browser.title)
        self.assertIn('bing', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
