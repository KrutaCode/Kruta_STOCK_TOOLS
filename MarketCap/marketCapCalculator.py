import YahooFinanceInterface
import CoinMarketCapInterface
from menus import main_menu, stock_menu, sharePrice_menu, marketCap_menu, crypto_menu, cryptoPrice_menu, cryptoMarketCap_menu






class MarketCapCalculator:
    def __init__(self,isCrypto=False):
        self.isCrypto = isCrypto

    def calculateMarketCap(self,supply,sharePrice):
        #Declare local variables
        marketCap = None
        #Determine if the asset is a crypto currency
        if self.isCrypto:
            pass
        #If not a crypto then it is a stock
        else:
            supply = formatNumber(supply)
            supply, sharePrice = float(supply), float(sharePrice)
            marketCap = sharePrice * supply
        return marketCap

    ##############
    # Function: getSharesOutstanding()
    # Description: Calculates the number of shares outstanding
    # Returns: Float
    ##############
    def calculateSharesOutstanding(self,marketCap,assetPrice):
        mktCap = marketCap
        price = assetPrice

        #Format the data
        mktCap = formatNumber(mktCap)

        # Calculate the shares outstanding
        outstanding = mktCap / price

        print(f"Outstanding: {outstanding}")
        return outstanding
    ##############
    # Function:
    # Description:
    # Returns:
    ##############
    def calculateSharePrice(self,outStandingShares,marketCap):
        if self.isCrypto:
            marketCap = formatNumber(marketCap)
            maxSupply = outStandingShares

            print(f"Market: {marketCap}")
            price = float(marketCap) / float(maxSupply)
        else:
            #Get the data
            outstanding = outStandingShares
            mktCap = marketCap

            #Format the data
            outstanding = formatNumber(outstanding)
            mktCap = formatNumber(mktCap)

            # Calculate the share price
            price = mktCap / outstanding

        return price
    ##############
    # Function:
    # Description:
    # Returns:
    ##############
    def sharePriceByMarketCap(self,outstandingShares):
        user_input = str(input("Enter the market cap: "))

        if "," in user_input:
            user_input = user_input.replace(",","")

        if "T" in user_input:
            user_input = user_input[:-1]
            user_input = float(user_input)
            user_input *= 1000000000000
        elif "B" in user_input:
            user_input = user_input[:-1]
            user_input = float(user_input)
            user_input *= 1000000000
        elif "M" in user_input:
            user_input = user_input[:-1]
            user_input = float(user_input)
            user_input *= 1000000
        elif "TH" in user_input:
            user_input = user_input[:-1]
            user_input = float(user_input)
            user_input *= 1000

        mktCap = float(user_input)

        #Get the shares outstanding
        outstanding = outstandingShares

        #Format data
        outstanding = formatNumber(outstanding)

        #Calculate the share price
        price = mktCap / outstanding

        print(f"Price: {price}")
    ##############
    # Function:
    # Description:
    # Returns:
    ##############
    ##############
    # Function:
    # Description:
    # Returns:
    ##############
    ##############
    # Function:
    # Description:
    # Returns:
    ##############


##############
# Function: formatMarketCap(String)
# Description: Looks at the trailing character and multiplies it accordingly.
# Returns: Float
##############
def formatNumber(num):

    #Remove commas from the number if they are present.
    if "," in num:
        num = num.replace(",","")
    #At the end of the num variable is a letter that indicates the size of the number. Ex: 2M   2,000,000
    multiple_letter = num[-1]

    #If the last element is a letter, or digit.
    if multiple_letter == "T" or multiple_letter == "B" or multiple_letter == "M":
        #Remove the tail letter
        num = num[:-1]

    #Convert to float to do calculations
    num = float(num)

    if multiple_letter == "T":
        multiple = 1000000000000
        num *= multiple
    elif multiple_letter == "B":
        multiple = 1000000000
        num *= multiple
    elif multiple_letter == "M":
        multiple = 1000000
        num *= multiple

    return num

def formatPrice(num):
    format = "{:,.2f}".format(num)
    num = float(format)
    return num

def addCommas(num):
    num = "{:,}".format(num)
    return num




def getUserInput(textToDisplay,dataType,floor=0,ceiling=10,allowNegative = True):
    #Declare local variables
    userInput = None
    integer = int
    floatingPoint = float
    string_ = str

    #If input is a integer
    if type(dataType) == type(integer):
        # Get initial input
        userInput = int(input(textToDisplay))

        if allowNegative:
            while type(userInput) != type(integer):
                try:
                    userInput = int(input("-There was a problem handling your previous entry.\n Please make another entry: "))
                except ValueError:
                    userInput = int(input("-There was a problem handling your previous entry.\n Please make another entry: "))

        else:
            while type(userInput) != type(integer) and (userInput <= floor or userInput > ceiling):
                try:
                    userInput = int(input("-There was a problem handling your previous entry.\n Please make another entry: "))
                except ValueError as e:
                    userInput = int(input("-There was a problem handling your previous entry.\n Please make another entry: "))

    #If input is a float
    elif type(dataType) == type(floatingPoint):
        # Get initial input
        userInput = float(input(textToDisplay))

        if allowNegative:
            while type(userInput) != type(floatingPoint):
                try:
                    userInput = float(input("-There was a problem handling your previous entry.\n Please make another entry: "))
                except ValueError:
                    userInput = float(input("-There was a problem handling your previous entry.\n Please make another entry: "))

        else:
            while type(userInput) != type(floatingPoint) and (userInput <= floor or userInput > ceiling):
                try:
                    userInput = float(input("-There was a problem handling your previous entry.\n Please make another entry: "))
                except ValueError:
                    userInput = float(input("-There was a problem handling your previous entry.\n Please make another entry: "))

    #If input is a string
    elif type(dataType) == type(string_):
        # Get the initial input
        userInput = str(input(textToDisplay))

        while type(userInput) != type(string_):
            try:
                userInput = str(input("-There was a problem handling your previous entry.\n Please make another entry: "))
            except ValueError:
                userInput = str(input("-There was a problem handling your previous entry.\n Please make another entry: "))







    return userInput







def main():
    # Menu for selecting which asset to calculate.
    print(main_menu)
    asset_type_input = int(input("Enter an asset type: "))

    #If the user chose Stocks
    if asset_type_input == 1:
        print("\n------------------------\nStocks\n")
        ticker_input = str(input("Enter a ticker: "))

        #Create class objects related to stock assets
        yf_object = YahooFinanceInterface.YahooFinanceInterface(ticker_input)
        mc = MarketCapCalculator()

        #Get basic data
        marketCap = yf_object.getMarketCap()
        shareOutstanding = yf_object.getSharesOutstanding()
        sharePrice = yf_object.getLivePrice()[0]

        # Menu to decide which aspect to calculate.
        running = True
        while running:
            print(f"\n{stock_menu}")

            stockSelection_input = getUserInput("-Enter a calculation type to proceed with: ",int,allowNegative=False)


            #If the user is calculating share price
            if stockSelection_input == 1:
                print(sharePrice_menu)
                sharePrice_input = getUserInput("-Enter the calculation type to proceed with: ",int,allowNegative=False)


                #If the user chose to calculate the share price using a custom market cap.
                if sharePrice_input == 1:
                    customMarketCap = getUserInput("-Enter a custom Market Cap: ",str)
                    sharePrice = mc.calculateSharePrice(shareOutstanding,customMarketCap)
                    print(f"\n-The price per share would be: ${formatPrice(sharePrice)}\n At a market cap of {customMarketCap}\n With {shareOutstanding} outstanding shares")

                #If the user chose to calculate the share price using a custom number of shares outstanding.
                elif sharePrice_input == 2:
                    customOutstanding = getUserInput("-Enter the number of Outstanding Shares: ",str)
                    sharePrice = mc.calculateSharePrice(customOutstanding,marketCap)
                    print(f"\n-The price per share would be: ${formatPrice(sharePrice)}\n At a market cap of {marketCap}\n With {customOutstanding} outstanding shares")

                #If the user chooses to calculate the share price using custom numbers for both fields.
                elif sharePrice_input == 3:
                    customMarketCap = getUserInput("-Enter a custom Market Cap: ",str)
                    customOutstanding = getUserInput("-Enter the number of Outstanding Shares: ",str)
                    sharePrice = mc.calculateSharePrice(customOutstanding,customMarketCap)
                    print(f"\n-The price per share would be: ${formatPrice(sharePrice)}\n At a market cap of {customMarketCap}\n With {customOutstanding} outstanding shares")

            #If the user is calculating shares outstanding
            elif stockSelection_input == 2:
                print(f"\n-The number of shares outstanding the company has is: {mc.calculateSharesOutstanding(marketCap,sharePrice)}")

            #If the user is calculating market cap
            elif stockSelection_input == 3:
                print(marketCap_menu)
                marketCap_input = getUserInput("-Enter a calculation type to proceed with: ",int,allowNegative=False)

                #If the user is calculating market cap using a custom share price
                if marketCap_input == 1:
                    customSharePrice = getUserInput("-Enter a custom share price: ",str)
                    marketCap = mc.calculateMarketCap(shareOutstanding,customSharePrice)
                    print(f"\n-The market cap would be: {addCommas(marketCap)}\n When the price per share is: ${customSharePrice}\n With {shareOutstanding} outstanding shares")

                #If the user is calculating the market cap by a custom number of shares outstanding.
                elif marketCap_input == 2:
                    customOutstanding = getUserInput("-Enter a custom number of Outstanding Shares: ",str)
                    marketCap = mc.calculateMarketCap(customOutstanding,sharePrice)
                    print(f"\n-The market cap would be: {addCommas(marketCap)}\n When the price per share is: ${sharePrice}\n With {customOutstanding} outstanding shares")

                #If the user is calculating the market cap using custom numbers for both fields.
                elif marketCap_input == 3:
                    customSharePrice = getUserInput("-Enter a calculation type to proceed with: ",str)
                    customOutstanding = getUserInput("-Enter a custom number of Outstanding Shares: ",str)
                    marketCap = mc.calculateMarketCap(customOutstanding,customSharePrice)
                    print(f"\n-The market cap would be: {addCommas(marketCap)}\n When the price per share is: ${sharePrice}\n With {customOutstanding} outstanding shares")


    #If the user chose Crypto
    elif asset_type_input == 2:
        print("\n------------------------\nCrypto\n")
        ticker_input = input(str("Enter a ticker: "))

        cmc = CoinMarketCapInterface.CoinMarketCap()
        cmc.setData(ticker_input)

        #Get basic data
        data = cmc.getCoinProfile()
        marketCap = data['Market_cap']
        coinPrice = data['Price']
        dilutedCap = data['Diluted_cap']
        maxSupply = data['Maximum_supply']

        #Create MarketCapCalculator object
        mc = MarketCapCalculator(isCrypto=True)

        running = True
        while running:
            print(f"\n{crypto_menu}")
            cryptoSelection_input = getUserInput("-Enter the calculation type to proceed with: ",int,allowNegative=False)

            #If the user is calculating coin price
            if cryptoSelection_input == 1:
                print(cryptoPrice_menu)
                cryptoPrice_input = getUserInput("-Enter the calculation type to proceed with: ",int,allowNegative=False)

                #If the user chose to calculate price with a custom market cap.
                if cryptoPrice_input == 1:
                    customMarketCap = getUserInput("-Enter a custom Market Cap: ",str)
                    coinPrice = mc.calculateSharePrice(maxSupply,customMarketCap)
                    print(f"\n-The price per coin would be: ${formatPrice(coinPrice)}\n At a market cap of {customMarketCap}\n With a max supply of: {maxSupply} ")

                #If the user chose to calculate price with a custom max supply
                elif cryptoPrice_input == 2:
                    customMaxSupply = getUserInput("-Enter a maximum supply: ",str)
                    coinPrice = mc.calculateSharePrice(customMaxSupply,dilutedCap)
                    print(f"\n-The price per coin would be: ${formatPrice(coinPrice)}\n At a market cap of {dilutedCap}\n With a max supply of: {maxSupply} ")

                #If the user chose to calculate the price using custom data for both fields
                elif cryptoPrice_input == 3:
                    customMarketCap = getUserInput("-Enter a custom Market Cap: ",str)
                    customMaxSupply = getUserInput("-Enter a maximum supply: ",str)
                    coinPrice = mc.calculateSharePrice(customMaxSupply, customMarketCap)
                    print(f"\n-The price per coin would be: ${formatPrice(coinPrice)}\n At a market cap of {customMarketCap}\n With a max supply of: {customMaxSupply} ")

            #If the user is calculating market cap
            elif cryptoSelection_input == 2:
                print(cryptoMarketCap_menu)
                cryptoMarketCap_input = getUserInput("-Enter the calculation type to proceed with: ",int,allowNegative=False)

                #If the user chose to calculate market cap with a custom price per coin
                if cryptoMarketCap_input == 1:
                    customCoinPrice = getUserInput("-Enter a custom coin price: ",float,allowNegative=False)
                    marketCap = mc.calculateMarketCap(maxSupply, customCoinPrice)
                    print(f"\n-The market cap would be: {addCommas(marketCap)}\n When the price per coin is: ${customCoinPrice}\n With a max supply of: {maxSupply} outstanding shares")


                #If the user chose to calculate market cap with a custom max supply
                elif cryptoMarketCap_input == 2:
                    customMaxSupply = getUserInput("-Enter the calculation type to proceed with: ",str)
                    marketCap = mc.calculateMarketCap(customMaxSupply,coinPrice)
                    print(f"\n-The market cap would be: {addCommas(marketCap)}\n When the price per coin is: ${coinPrice}\n With a max supply of: {customMaxSupply} outstanding shares")

                #If the user chose to calculate market cap with custom data for both fields.
                elif cryptoMarketCap_input == 3:
                    customCoinPrice = getUserInput("-Enter a custom coin price: ",float,allowNegative=False)
                    customMaxSupply = getUserInput("-Enter the calculation type to proceed with: ",str)
                    marketCap = mc.calculateMarketCap(customMaxSupply,customCoinPrice)
                    print(f"\n-The market cap would be: {addCommas(marketCap)}\n When the price per coin is: ${customCoinPrice}\n With a max supply of: {customMaxSupply} outstanding shares")




main()
