from selenium import webdriver

from PageFactory.MainPage import MainPage
from Utility.TestBase import TestBase
mainPage:MainPage = None

class TestMainPage(TestBase):

    def test_fakeCoin(self):
        ''' Initialise the driver'''
        driver = self.intialize_driver()
        ''' Make driver global'''
        global mainPage
        ''' Create an object for MainPage class to access supporting methods'''
        mainPage= MainPage(driver)
        ''' Call the method to compute and return the fake coin number '''
        fakeCoin = self.computeAndgetTheFakeCoin()
        ''' Retrieve alert message '''
        alertMessage = self.getAlertMessage(driver, fakeCoin)
        '''Compare the alert message and verify if the correct fake coin found'''
        if alertMessage == 'Yay! You find it!':
            '''Display the success message as correct fake coin has been found'''
            display = '\n'+ "The Fake Coin is :" + fakeCoin + '\nThe alert message appeared: '+ alertMessage + '\nThe list of Weighings displayed are: \n' + mainPage.getWeighingsListContent()
            print(display)
            ''' Write the success information in to the output.txt file'''
            self.writeToFile('success', display)
        else:
            ''' Display the incorrect alert message as correct fake coin has not been found'''
            print(alertMessage)
            ''' Write the failure message to output file'''
            self.writeToFile('fail', alertMessage)
        ''' Close the browser'''
        self.quit_browser()


    '''
    Enter the coins into grids and finds the fake coin
    '''
    def computeAndgetTheFakeCoin(self)->str:
        start, end  = 0, 8
        ''' Start with 0 and 8
            verify if the weights equal.
            If equal refresh the grids and place 1, 7 coins in left and right grids.
            Else place right grid with 7th coin
            verify if the coins equal in weigh
            if yes the fake coin was 8 else the fake coin is 0th
            
            Continue until fake coin found
        '''
        while start<end:
            mainPage.insertCoinInLeftGrid(start, start)
            mainPage.insertCoinInRightGrid(start, end)
            mainPage.clickOnWeighButton()
            mainPage.waitUntilResultDisplays()
            if mainPage.isResultEquals():
                mainPage.clickOnResetButton()
                start = start+1
                end = end-1
            else:
                mainPage.clickOnResetButton()
                mainPage.insertCoinInLeftGrid(start, start)
                mainPage.insertCoinInRightGrid(start, end-1)
                mainPage.clickOnWeighButton()
                mainPage.waitUntilResultDisplays()
                if mainPage.isResultEquals():
                    return str(end)
                else:
                    return str(start)
                break
            '''
            If the last iteration reached that means the left over coin 4 is fake as rest all are equal.
            '''
            if start==end:
                return "4"

    '''
    Get the alert message appeared on the screen
    '''
    def getAlertMessage(self, driver, fakeCoin:str)->str:
        mainPage.clickOnFakeCoin(fakeCoin)
        retVal = self.acceptAlertAndGetMessage()
        return retVal






