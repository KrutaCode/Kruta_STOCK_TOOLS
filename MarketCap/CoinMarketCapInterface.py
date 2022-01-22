import json
from bs4 import BeautifulSoup
from lxml import etree
from api_details import COIN_MARKET_API_KEY
from requests import Request, Session







class CoinMarketCap:
    def __init__(self,currencyConversion = "USD"):
        self.conversion = currencyConversion
        self.headers = {
            'Accepts':"application/json",
            "X-CMC_PRO_API_KEY": COIN_MARKET_API_KEY
        }

        self.session = Session()
        self.session.headers.update(self.headers)


    def setData(self,ticker):

        #Url to get latest quotes from API
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        params = {
            'symbol':ticker,
            'convert':self.conversion
        }

        #Create session and get it in json format
        response = self.session.get(url,params=params)
        data = json.loads(response.text)

        #Get the max supply of the token.
        self.maxSupply = data['data'][ticker]['max_supply']

        #Get the associated tags
        self.tags = data['data'][ticker]['tags']

        #Get the name of the platform that is hosting coin/token
        self.platformHostingName = data['data'][ticker]['platform']['name']

        #Get the latest price of the coin along with the 1h & 24h percent change.
        self.price = data['data'][ticker]['quote']['USD']['price']
        self.percentChange1h = data['data'][ticker]['quote']['USD']['percent_change_1h']
        self.percentChange24h = data['data'][ticker]['quote']['USD']['percent_change_24h']
        self.percentChange7d = data['data'][ticker]['quote']['USD']['percent_change_7d']
        self.percentChange30d = data['data'][ticker]['quote']['USD']['percent_change_30d']
        self.percentChange60d = data['data'][ticker]['quote']['USD']['percent_change_60d']
        self.percentChange90d = data['data'][ticker]['quote']['USD']['percent_change_90d']

        #Get the market cap of the coin/token. Along with the dominance of its sector.
        self.marketCap = data['data'][ticker]['quote']['USD']['market_cap']
        self.dilutedMarketCap = data['data'][ticker]['quote']['USD']['fully_diluted_market_cap']
        self.marketCapDominance = data['data'][ticker]['quote']['USD']['market_cap_dominance']

        #Get the volume and the 24 hour change.
        self.volume24h = data['data'][ticker]['quote']['USD']['volume_24h']
        self.volumeChange24h = data['data'][ticker]['quote']['USD']['volume_change_24h']

    def getCoinPriceData(self):
        return {'Price':self.price,
                '1h %':self.percentChange1h,
                '24h_%_change':self.percentChange24h,
                '7d_%_change':self.percentChange7d,
                '30d_%_change':self.percentChange30d,
                '60d_%_change':self.percentChange60d,
                '90d_%_change':self.percentChange90d}

    def getCoinVolumeData(self):
        return {'24h_volume':self.volume24h,
                '24h_volume_change':self.volumeChange24h}

    def getCoinProfile(self):
        return{'Price':self.price,
               'Market_cap':self.marketCap,
               'Diluted_cap':self.dilutedMarketCap,
               'Dominance':self.marketCapDominance,
               'Maximum_supply':self.maxSupply,
               '24h_volume':self.volume24h,
               'Platform':self.platformHostingName,
               'Tags':self.tags}





