import requests
from bs4 import BeautifulSoup
from lxml import etree


class YahooFinanceScraper:
    def __init__(self,ticker):
        self.ticker = ticker

        #Var Init
        self.yahoo_dict = {}
        ah = None
        headers = {'User-Agent':'Chrome/93.0.4577.82'}
        url = f'https://finance.yahoo.com/quote/{self.ticker.upper()}?p={self.ticker.upper()}&.tsrc=fin-srch'
        post_market = None
        self.pathExtension = "/text()"

        # Get the html of website
        req = requests.get(url,headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        dom = etree.HTML(str(soup))

        # Previous Close
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]"
            prev_close = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Previous Close'] = prev_close[0]
        except IndexError:
            print(f"---Failed to get Previous Close---")

        # Open
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]"
            today_open = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Open'] = today_open[0]
        except IndexError:
            print(f"---Failed to get Today's Open")

        # Live Price
        try:
            live_price_path = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div[1]/fin-streamer[1]"
            pctDifference_path = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div[1]/fin-streamer[3]/span"
            priceDifference_path = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div[1]/fin-streamer[2]/span"
            live_price = (dom.xpath(live_price_path + self.pathExtension))
            pctDifference = (dom.xpath(pctDifference_path + self.pathExtension))
            priceDifference = (dom.xpath(priceDifference_path + self.pathExtension))
            live_price = str(live_price[0]) + " " + str(priceDifference[0]) + " " + str(pctDifference[0])
            _p, _d, _perc = live_price.split()
            _perc = _perc.strip("()")
            live_price = [_p, _d, _perc]
            self.yahoo_dict['Live Price'] = live_price
        except IndexError:
            print(f"---Failed to get Live Price---")

        # 1y Price Target
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[8]/td[2]"
            priceTarget_1y = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['1y Price Target'] = priceTarget_1y[0]
        except IndexError:
            print(f"---Failed to get 1y Price Target---")

        # Year Range
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[6]/td[2]"
            year_range = (dom.xpath(path + self.pathExtension))
            year_range = str(year_range).split("-")
            start, end = year_range[0].strip("['"),year_range[1].strip("']")
            yRange = (float(start),float(end))
            self.yahoo_dict['Year Range'] = yRange
        except IndexError:
            print(f"---Failed to get Year Range---")

        #Daily Volume
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/fin-streamer"
            daily_volume = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Volume'] = daily_volume[0]
        except IndexError:
            print(f"---Failed to get Daily Volume")

        #Avg Volume
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[8]/td[2]"
            avg_volume = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Avg Volume'] = avg_volume[0]
        except IndexError:
            print(f"---Failed to get Average Volume---")

        #Dividend
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[6]/td[2]"
            div_yield = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Dividend'] = div_yield[0]
        except IndexError:
            print(f"---Failed to get Dividend---")

        #ETF Yield
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[4]/td[2]"
            etf_yield = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['ETF Yield'] = etf_yield[0]
        except IndexError:
            print(f"---Failed to get ETF Yield---")

        #Ex-Div-Date
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[7]/td[2]/span"
            ex_div_date = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Div-Date'] = ex_div_date[0]
        except IndexError:
            print(f"---Failed to get Ex-Div-Date---")

        #PE Ratio
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[3]/td[2]"
            pe_ratio = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['P/E ratio'] = pe_ratio[0]
        except IndexError:
            print(f"---Failed to get P/E Ratio---")

        #YTD Total Return
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[1]/span"
            YTD_returns = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['YTD Returns'] = YTD_returns[0]
        except IndexError:
            print(f"---Failed to get YTD Total Return(ETF Only)---")

        #EPS
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[4]/td[2]"
            eps = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['EPS'] = eps[0]
        except IndexError:
            print(f"---Failed to get EPS---")

        #Earnings Date
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[2]/span"
            earnings_date = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Earnings Date'] = earnings_date
        except IndexError:
            print(f"---Failed to get Earnings Date---")

        #Market Cap
        try:
            path = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]"
            market_cap = (dom.xpath(path + self.pathExtension))
            self.yahoo_dict['Market Cap'] = market_cap[0]
        except KeyError:
            print(f"---Failed to get Market Cap---")





        try:
            postPricePath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div[2]/fin-streamer[2]"
            priceDiffPath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div[2]/span[1]/fin-streamer[1]/span"
            pctDiffPath = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div[2]/span[1]/fin-streamer[2]/span"
            post_market = str(postPricePath[0]) + " " + str(priceDiffPath[0]) + " " + str(pctDiffPath[0])
            p,d,perc = post_market.split()
            perc = perc.strip("()")
            post_market = [p,d,perc]
            ah = True
        except:
            print("---Failed to get Post Market Price---")
            ah = False

        if ah:
            self.yahoo_dict['Post-Market'] = post_market

    def getPrevClose(self):
        try:
            return self.yahoo_dict['Previous Close']
        except KeyError:
            pass

    def getOpen(self):
        try:
            return self.yahoo_dict['Open']
        except KeyError:
            pass

    def getLivePrice(self):
        try:
            return self.yahoo_dict['Live Price']
        except KeyError:
            pass

    def get1yPriceTarget(self):
        try:
            return self.yahoo_dict['1y Price Target']
        except KeyError:
            pass
    def getYearRange(self):
        try:
            return self.yahoo_dict['Year Range']
        except KeyError:
            pass

    def getVolume(self):
        try:
            return self.yahoo_dict['Volume']
        except KeyError:
            pass

    def getAvgVolume(self):
        try:
            return self.yahoo_dict['Avg Volume']
        except KeyError:
            pass
    def getDividend(self):
        try:
            return self.yahoo_dict['Dividend']
        except KeyError:
            pass
    def getETFyield(self):
        try:
            return self.yahoo_dict['ETF Yield']
        except KeyError:
            pass

    def getExDivDate(self):
        try:
            return self.yahoo_dict['Div-Date']
        except KeyError:
            pass

    def getPEratio(self):
        try:
            return self.yahoo_dict['P/E ratio']
        except KeyError:
            pass

    def getYTDreturns(self):
        try:
            return self.yahoo_dict['YTD Returns']
        except KeyError:
            pass

    def getEPS(self):
        try:
            return self.yahoo_dict['EPS']
        except KeyError:
            pass
    def getEarningsDate(self):
        try:
            return self.yahoo_dict['Earnings Date']
        except KeyError:
            pass

    def getMarketCap(self):
        try:
            return self.yahoo_dict['Market Cap']
        except KeyError:
            pass

    def getPostMarket(self):
        try:
            return self.yahoo_dict['Post-Market']
        except KeyError:
            pass
"""
Example Use: 
_______________________________

def main():
    y = YahooFinanceScraper("AAPL") #Creates an object will info related to the ticker entered. 

    print(f"{y.getLivePrice()}") #Gets the most recent price of live market hours. If it is after close, or the weekend then it will return the closing prices. 
main()
"""
