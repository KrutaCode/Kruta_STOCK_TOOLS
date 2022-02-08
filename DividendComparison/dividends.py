import yfinance as yf
import datetime as dt
import pandas as pd




class DividendTracker:
    def __init__(self, ticker,timeframe="1Y"):
        #Change the timeframe to a day value. (ex. 1Y = 365)
        n = self.timeframe_to_days(timeframe)
        #Get the timestamp of today
        td = dt.datetime.now()

        #Calculate the difference based on the timeframe
        timerange = dt.datetime.now() - dt.timedelta(days=n)

        #Convert the datetime objects to seconds.
        period1 = int(timerange.timestamp())
        period2 = int(td.timestamp())


        # Fetch the data
        query = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker.upper()}?period1={period1}&period2={period2}&interval=1d&events=div&includeAdjustedClose=true"

        self.data = pd.read_csv(query)
        print(f"Data; {self.data}")

    #######################
    # Function: get_dividend_change()
    # Description: Compares the first and last entry in the data
    # Returns: float
    #######################
    def get_dividend_change(self):
        most_recent_dividend = float(self.data['Dividends'].iloc[-1])
        last_dividend = float(self.data['Dividends'].iloc[0])

        # Get the percentage value
        result = (most_recent_dividend / last_dividend) - 1
        result = str(self.format_number(result)) + "%"
        return result
    #######################
    # Function:
    # Description:
    # Returns:
    #######################
    def format_number(self,num,digits=3):
        if digits == 1:
            num = "{:,.1f}".format(num)
        elif digits == 2:
            num = "{:,.2f}".format(num)
        elif digits == 3:
            num = "{:,.3f}".format(num)
        elif digits == 4:
            num = "{:,.4f}".format(num)
        elif digits == 5:
            num = "{:,.5f}".format(num)



        return num
    #######################
    # Function:
    # Description:
    # Returns:
    #######################
    #######################
    # Function:
    # Description:
    # Returns:
    #######################


    #######################
    # Function: timeframe_to_days(str)
    # Description: Will convert the timeframe to the number of days.
    # Returns: int
    #######################

    def timeframe_to_days(self,tf):
        # Variable Init
        r = None
        m = None
        # Get the number
        num = tf[:-1]
        # Get the multiple (i.e. Y, M, D)
        multiple = tf[-1]

        # Logic to assign multiple
        if multiple == "Y" or multiple == "y":
            m = 365
        elif multiple == "M" or multiple == "m":
            m = 30
        elif multiple == "D" or multiple == "d":
            m = 1

        # Calculate the result
        r = int(num) * m

        return r





