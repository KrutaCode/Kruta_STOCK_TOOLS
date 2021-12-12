import yahoo_fin.stock_info as si

'''
################################################
Explanation cited with https://www.investopedia.com/ask/answers/070114/what-formula-calculating-earnings-share-eps.asp

    Key Notes:
    -Earnings per share or EPS is the portion of a company's profit
     allocated to each outstanding share of common stock.

    -EPS is sometimes known as the bottom line for a firm. It can give an indication of the firms worth.

    Equation:
    EPS (for a company with preferred and common stock) = (net income - preferred dividends)
                                                         --------------------------------------
                                                         average outstanding share of common stock

    In simple terms EPS = net income/ average outstanding share

    -EPS is one measure that can serve as a proxy of a company's financial health.
     If all of a company's profits were paid out to its shareholders, EPS is the portion
     of a company's net income that would be allocated to each outstanding share.

'''

class EPS:

    def __init__(self,ticker):

        self.ticker = ticker.upper()
        self.history = si.get_earnings_history(self.ticker)
        self.epsData = []

        for element in self.history:
            #Get the date of the report.
            period = element['startdatetime']
            #Turn variable into string to format.
            period = str(period)
            period = period[:10]

            #Get the eps
            eps = element['epsactual']
            try:
                epsDict = {'Date Reported':period, 'EPS':float(eps)}
                self.epsData.append(epsDict)
            except:
                pass
        self.cleanData()
    #################################
    #Function: cleanData()
    #Description: Removes duplications and fields with the value 'None'
    #Returns: None
    #################################
    def cleanData(self):
        #Keeps track of index in list.
        index = 0

        for item in self.epsData:
            #Create local variables
            eps = item['EPS']
            date = item['Date Reported']

            try:
                #Gets data within next element.
                newElem = self.epsData[index+1]
                if date == newElem['Date Reported']:
                    del self.epsData[index+1]
            except:
                break
            index += 1
    #################################
    # Function: getMostRecent()
    # Description: Returns the most recent earnings report.
    # Returns: Dictionary
    #################################
    def getMostRecent(self):
        return self.epsData[0]
    #################################
    # Function: getLastFive()
    # Description: Gets the 5 most recent earnings reports.
    # Returns: list[dict]
    #################################
    def getFiveMostRectent(self):
        return self.epsData[0:5]
    #################################
    # Function: getTopFive()
    # Description: Gets the top 5 highest EPS periods.
    # Post-condition: The list is sorted in descending order.
    # Returns: list[dict]
    #################################
    def getTopFive(self):
        #Sort the list to easily splice the list and get the top five.
        data = self.sortData()
        return data[0:5]
    #################################
    # Function: sortData(bool)
    # Description: Sorts the list of dictionaries.
    # Post-condition: The list is rearranged. If descending equals true then the highest values will be first.
    # Returns: list[dict]
    #################################
    def sortData(self, descending=True):
        sortedList = sorted(self.epsData, key=lambda i: i['EPS'], reverse=descending)
        return sortedList
    #################################
    # Function: getLowest()
    # Description: Gets the lowest EPS recorded.
    # Returns: dict
    #################################
    def getLowest(self):
        sortedList = self.sortData(descending=False)
        return sortedList[0]
    #################################
    # Function: getLowestFive()
    # Description: Returns the five lowest recorded EPS.
    # Returns: list[dict]
    #################################
    def getLowestFive(self):
        sortedList = self.sortData(descending=False)
        return sortedList[0:5]
