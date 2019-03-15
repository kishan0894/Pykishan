import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Remote(command_executor='http://192.168.0.58:4444/wd/hub',
        #                               desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
        self.driver = webdriver.Remote(command_executor='http://192.168.0.58:4444/wd/hub',
                                       desired_capabilities=webdriver.DesiredCapabilities.CHROME)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://github.com")
        assert "GitHub" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("dzitkowskik")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
