from selenium import webdriver
import unittest


class FuncTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get('http://127.0.0.1:8000')
        assert 'Keeper' in self.browser.title

# todo add selenium in requirements

if __name__ == '__main__':  #
    unittest.main(warnings='ignore')
