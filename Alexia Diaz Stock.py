#Alexia Diaz 
#Excerise 7.2

stock_dictionary = {'NASDAQ:AAPL': 23, 'NYSE:A': 45, 'NASDAQ:MSFT': 89, 'NASDAQ:GOOG': 89, 'NASDAQ:AMZN': 56, 'NYSE:BRK.B': 65,
                    'NYSE:HOG': 78, 'NASDAQ:NFLX': 9, 'NYSE:LUV': 40, 'NYSE:WMT': 6}

while True:
    symbol = str(raw_input("Please enter ticker symbol: "))
    value = stock_dictionary.get(symbol)

    if symbol == 'Exit':
        break

    if symbol not in stock_dictionary:
        print ("Ticker symbol not found")
    else:
        print("Ticker Symbol: " + symbol + " Value: " + str(value))
