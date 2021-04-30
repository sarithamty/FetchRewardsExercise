import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utility import TestBase
'''
Page class for the Main page
Define the page objects and actions related to these page objects to support the actual testcase executions
'''
class MainPage:
    def __init__(self, driver):
        self.driver = driver
    #weigh button XPATGH
    weigh_button = (By.XPATH, '//button[@id="weigh"]')
    #Result button XPATH
    result_button = (By.XPATH, '//div[@class="result"]/button[@id="reset"]')
    #Reset button XPATH
    reset_button = (By.XPATH,'//button[@id="reset" and text()="Reset"]')
    #Weighings list XPATH
    weighings_list = (By.XPATH,'//ol/li')

    '''
    dynamic XPATH builder for left row squares.
    Pass the square number
    '''
    def getLeftrowSquareXPATH(self, square_number):
        return '//input[@id="left_' + str(square_number) + '"]'
    '''
    Left row square webelement will be returned based on square number
    '''
    def getLeftrowSquare(self, square_number):
        return self.driver.find_element(By.XPATH, self.getLeftrowSquareXPATH(square_number))

    '''
    Weigh Element will be returned
    '''
    def getWeighButton(self):
        return self.driver.find_element(*MainPage.weigh_button)

    '''
    Reset button Element will be returned
    '''
    def getResetButton(self):
        return self.driver.find_element(*MainPage.reset_button)

    '''
    Result button Element value will be returned
    '''
    def getResultButtonValue(self)->str:
        return (self.driver.find_element(*MainPage.result_button)).text

    '''
    Weighings list items will be returned
    '''
    def getWeighingsList(self):
        return self.driver.find_elements(*MainPage.weighings_list)


    '''
    return true if result button value is '='
    return false if not
    '''
    def isResultEquals(self):
        return self.getResultButtonValue()=='='

    '''
    return true if result button value is '>'
    return false if not
    '''
    def isResultGreater(self):
        return self.getResultButtonValue() == '>'

    '''
     return true if result button value is '<'
     return false if not
     '''
    def isResultLessthan(self):
        return self.getResultButtonValue() == '<'

    '''
     dynamic XPATH builder for right row squares.
     Pass the square number
     '''
    def getRightrowSquareXPATH(self, square_number):
        return '//input[@id="right_' + str(square_number) + '"]'

    '''
     Left right square webelement will be returned based on square number
     '''
    def getRightrowSquare(self, square_number):
        return self.driver.find_element(By.XPATH, self.getRightrowSquareXPATH(square_number))


    '''
     dynamic XPATH builder for coins.
     Pass the coin number
     '''
    def getButtonXPATH(self, coin_number):
        return '//button[@id="coin_' + str(coin_number)+ '"]'

    '''
    Coin webelement will be returned based on coin number
    '''
    def getCoin(self, coin_number):
        return self.driver.find_element(By.XPATH, self.getButtonXPATH(coin_number))

    '''
    Insert the coin number into passed cell number and grid number 
    '''
    def insert_number(self, grid:str, cell_number, coin_number):
        if grid.lower() == 'left':
            (self.getLeftrowSquare(cell_number)).send_keys(coin_number)
        if grid.lower() == 'right':
            (self.getRightrowSquare(cell_number)).send_keys(coin_number)

    '''
    Insert the passed coin number value in left grid passed cell number
    '''
    def insertCoinInLeftGrid(self, cell_number, coin_number):
        self.insert_number('left',cell_number,coin_number)

    '''
     Insert the passed coin number value in right grid passed cell number
     '''
    def insertCoinInRightGrid(self, cell_number, coin_number):
        self.insert_number('right', cell_number, coin_number)

    '''
    Clicks on the weigh button
    '''
    def clickOnWeighButton(self):
        self.getWeighButton().click()

    '''
    Clicks on Reset button
    '''
    def clickOnResetButton(self):
        self.getResetButton().click()

    '''
    Clicks on the given Coin
    '''
    def clickOnFakeCoin(self, fakeCoin:str):
        self.getCoin(fakeCoin).click()

    '''
    Return the Weighings list displayed on the screen
    '''
    def getWeighingsListContent(self)->str:
        retVal:str= ""
        for listItem in self.getWeighingsList():
            retVal = retVal + listItem.text + '\n'
        return  retVal


    def waitUntilResultComputes(self):
        timer = 0
        while timer<40:
            if not self.getResultButtonValue() == "?":
                break
            time.sleep(2)
            timer= timer+2

    def waitUntilResultDisplays(self):
        wait = WebDriverWait(self.driver, 40)
        wait.until_not(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="result"]/button[@id="reset"]'), "?"))