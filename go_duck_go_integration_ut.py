import unittest
from selenium import webdriver
import time

class BaseOne():
    def test_url(self):
        self.driver.get("http://duckduckgo.com/")
        self.driver.find_element_by_id(
            'search_form_input_homepage').send_keys("realpython")
        self.driver.find_element_by_id("search_button_homepage").click()
        self.assertIn(
            "https://duckduckgo.com/?q=realpython", self.driver.current_url
        )

    def tearDown(self):
        t = time.time() - self.startTime
        print 50 * '!'
        print "%s: %.3f" % (self.id(), t)
        print 50 * '!'
        print '\n'
        self.driver.quit()

class Chrome(BaseOne, unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        self.driver = webdriver.Chrome()

class FF(BaseOne, unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        self.driver = webdriver.Firefox()

class Phantom(BaseOne, unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()
        self.driver = webdriver.PhantomJS()

if __name__ == '__main__':
    unittest.main()