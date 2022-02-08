import dividends



def main():
    d = dividends.DividendTracker("psec","5Y")

    print(f'D: {d.get_dividend_change()}')


main()