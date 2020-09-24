import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class CallLogTest(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '5LX9K18C12906909'
        self.dc['appPackage'] = 'com.afri_inc.senri'
        self.dc['appActivity'] = '.activity.HomeActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testCallLog(self):
        assert self.driver.find_element_by_accessibility_id('Navigate up').is_displayed()
        assert self.driver.find_element_by_id('titleOnToolbar').is_displayed()
        assert self.driver.find_element_by_id('displayTime').is_displayed()
        assert self.driver.find_element_by_id('displayCustomerName').is_displayed()
        assert self.driver.find_element_by_id('displayDetail').is_displayed()
        assert self.driver.find_element_by_id('menuButton').is_displayed()
        # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(By.ID('menuButton')))
        # self.driver.find_element_by_id('menuButton').click()
        # assert self.driver.find_element_by_xpath("xpath=//*[@text='Add New Customer']").click().is_displayed
        # assert self.driver.find_element_by_xpath("xpath=//*[@text='Add Number']").click().is_displayed
        # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(By.ID('menuButton')))
        # self.driver.find_element_by_id('menuButton').click()
        # assert self.driver.find_element_by_xpath("xpath=//*[@text='Record Visit Report']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()