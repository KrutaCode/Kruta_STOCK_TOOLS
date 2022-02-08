import os
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class YahooFinancialScraper:
    def __init__(self,ticker):
        self.ticker = ticker
        cwd = os.getcwd()
        chromeDriver = cwd + "\\chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')

        #Create browser object
        self.browser = webdriver.Chrome(chromeDriver,
                                        options=options)

        self.setIncomeStatement()

        time.sleep(50)

    ##################
    # Function: setData()
    # Description: Scrapes all of the data on the Income Statement from Yahoo Finance
    # Returns: None
    ##################
    def setIncomeStatement(self):

        # Create url with the specified ticker
        url = f"https://finance.yahoo.com/quote/{self.ticker.upper()}/financials?p={self.ticker.upper()}"

        # Load page with the desire url
        self.browser.get(url)

        # Click on the quarterly button
        quarterlyButton_path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[2]/button/div"
        self.clickItem(quarterlyButton_path)

        time.sleep(1)
        col1_Label = self.getItem("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[1]/div/div[3]")
        col2_Label = self.getItem("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[1]/div/div[4]/span")
        col3_Label = self.getItem("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[1]/div/div[5]/span")
        col4_Label = self.getItem("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[1]/div/div[6]/span")

        # Declare local variables
        col1 = []
        col2 = []
        col3 = []
        col4 = []

        labels = []

        # Gets the labels
        Running = True
        errorCount = 0
        hardIndex = 1
        while Running:
            if errorCount > 5:
                Running = False
            try:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                label = self.getItem(labelPath)
                labels.append(label)
            except NoSuchElementException:
                errorCount += 1
                pass
            hardIndex += 1

        # Gets the first column
        Running = True
        errorCount = 0
        hardIndex = 1
        while Running:

            try:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                path = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[3]/span"
                try:
                    label = self.getItem(labelPath)
                except NoSuchElementException:
                    break
                data = self.getItem(path)
                data = self.formatNumber(data)
                val = {label:data}
                col1.append(val)
            except NoSuchElementException:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                label = self.getItem(labelPath)
                if label != "Tax Effect of Unusual Items":
                    col1.append({label:"-"})

                else:
                    col1.append({label:"-"})
                    break
            hardIndex += 1

        # Gets the second column
        Running = True
        errorCount = 0
        hardIndex = 1
        while Running:
            try:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                path = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[4]/span"
                try:
                    label = self.getItem(labelPath)
                except NoSuchElementException:
                    break
                data = self.getItem(path)
                data = self.formatNumber(data)
                val = {label: data}
                col2.append(val)
            except NoSuchElementException:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                label = self.getItem(labelPath)
                if label != "Tax Effect of Unusual Items":
                    col2.append({label:"-"})
                else:
                    col2.append({label:"-"})
                    break
            hardIndex += 1

        # Gets the third columns
        Running = True
        errorCount = 0
        hardIndex = 1
        while Running:
            try:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                path = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[5]/span"
                try:
                    label = self.getItem(labelPath)
                except NoSuchElementException:
                    break
                data = self.getItem(path)
                data = self.formatNumber(data)
                val = {label:data}
                col3.append(val)
            except NoSuchElementException:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                label = self.getItem(labelPath)
                if label != "Tax Effect of Unusual Items":
                    col3.append({label:"-"})
                else:
                    col3.append({label:"-"})
                    break
            hardIndex += 1

        # Gets the fourth columns
        Running = True
        errorCount = 0
        hardIndex = 1
        while Running:
            try:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                path = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[6]/span"
                try:
                    label = self.getItem(labelPath)
                except NoSuchElementException:
                    break
                data = self.getItem(path)
                data = self.formatNumber(data)
                val = {label:data}
                col4.append(val)
            except NoSuchElementException:
                labelPath = f"/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[4]/div[1]/div[1]/div[2]/div[{hardIndex}]/div[1]/div[1]/div[1]/span"
                label = self.getItem(labelPath)
                if label != "Tax Effect of Unusual Items":
                    col4.append({label:"-"})
                else:
                    col4.append({label:"-"})
                    break
            hardIndex += 1

        table = {
            col1_Label: [x.values() for x in col1],
            col2_Label: [x.values() for x in col2],
            col3_Label: [x.values() for x in col3],
            col4_Label: [x.values() for x in col4]
        }

        self.incomeStatement = pd.DataFrame(table,index=labels)

        print(self.incomeStatement)



    ##################
    # Function: clickItem(string)
    # Description: Clicks on a item at the designated xpath.
    # Returns: None
    ##################
    def clickItem(self,xpath):
        try:
            self.browser.find_element_by_xpath(xpath).click()
        except Exception:
            time.sleep(1)
            self.clickItem(xpath)

    ##################
    # Function: getItem(string)
    # Description: Retrieves the item at the designated xpath.
    # Returns: string
    ##################
    def getItem(self,xpath):
            text = self.browser.find_element_by_xpath(xpath).text
            return text

    ##################
    # Function:
    # Description:
    # Returns:
    ##################
    def formatNumber(self,num):
        if "," in num:
            num = num.replace(",","")
            num = float(num)
            return num
    ##################
    # Function:
    # Description:
    # Returns:
    ##################
    ##################
    # Function:
    # Description:
    # Returns:
    ##################