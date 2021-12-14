import datetime as dt
from dateutil import relativedelta
import time



class Utils:
    def __init__(self):
        info = "Utils created 23:26 7/15/2021"

    def PriceFormat(self,number):
        e = float(number)
        formatted_number = "{:,.2f}".format(e)
        try:
            formatted_number = float(formatted_number)
            return formatted_number
        except ValueError:
            return formatted_number


    def MinusMonths(self,months_to_minus):
        today = dt.date.today()
        result = today - relativedelta.relativedelta(months=months_to_minus)
        return result


    def CalculateDates(self,origin,time_to_subtract):
        data_split = str(origin)

        try:
            date, time = data_split.split(" ")
        except ValueError:
            date = data_split
        year, month, day = date.split("-")

        year = int(year)
        month = int(month)
        day = int(day)
        final = dt.datetime(year,month,day)
        date_to_find = final - dt.timedelta(days=time_to_subtract)
        return  date_to_find

    def DateToSeconds(self,date):
        date = str(date)
        year, month, day = date.split("-")

        try:
            year, month, day = int(year), int(month), int(day)
        except ValueError:
            day = str(day)
            day,_ = day.split(" ")
            year, month, day = int(year), int(month), int(day)

        date_in_sec = int(time.mktime(dt.datetime(year,month,day,23,59).timetuple()))
        return date_in_sec