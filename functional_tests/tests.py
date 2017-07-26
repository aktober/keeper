from django.test import LiveServerTestCase
from selenium import webdriver
import unittest


class FuncTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        self.browser.get(self.live_server_url)
        assert 'Keeper' in self.browser.title

# todo add selenium in requirements
