import time

from selenium import webdriver
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None
class TestBase:

    '''
    Initialise the browser
    Maximise the window
    '''
    def intialize_driver(self)->webdriver:
        global driver
        driver = webdriver.Chrome(os.getcwd() + '/Browsers/chromedriver')
        print(os.getcwd() + '\Browsers\chromedriver.exe')
        driver.get('http://ec2-54-208-152-154.compute-1.amazonaws.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    '''
    Closes all the open browsers
    '''
    def quit_browser(self):
        driver.quit()

    '''
    Utility method to verify if the alert present and accpet the alert
    Returns the alert message to calling method
    '''
    def acceptAlertAndGetMessage(self)-> str:
        if self.is_alert_present():
            alert = driver.switch_to_alert()
            retVal= alert.text
            time.sleep(5)
            alert.accept()
            return retVal
        else:
            return 'No alert present'

    '''
    Open an output file and writes to the file.
    Need to pass the content and status of test case
    '''
    def writeToFile(self, status, display):
        try:
            file = open(os.getcwd()+'\Resources\output.txt', 'a')
            file.write(status + '\n')
            file.write(display)
            file.write('***************************************************')
        finally:
            file.close()


    '''
    Verify if the alert present or not
    return true if present
    return false if not present
    '''
    def is_alert_present(self):
        try:
            wait = WebDriverWait(driver, 40)
            wait.until(EC.alert_is_present())
            return True
        except TimeoutError:
            return False
        except:
            return False


    def waitUntilTextPresent(self, locator, text:str):
        wait = WebDriverWait(driver, 40)
        wait.until_not(EC.text_to_be_present_in_element(locator, text))