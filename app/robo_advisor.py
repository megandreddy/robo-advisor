# app/robo_advisor.py

import csv 
import json
import os

from dotenv import load_dotenv
import requests

load_dotenv()
#
# info inputs
#

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

api_key = os.environ.get("ALPHAVANTAGE_API_KEY") #demo"
#print(api_key)

#symbol = "AAPL" # TODO: accept user input
symbol = input("PLEASE INPUT A VALID STOCK SYMBOL: ") #"AAPL" # TODO: accept user input
print("SELECTED SYMBOL:", symbol)


if len(symbol) > 5:
    print("OOPS THE INPUT MUST BE BETWEEN 1 AND 5 CHARACTERS. PLEASE TRY AGAIN!")
    exit()
elif len(symbol) <1:
    print("OOPS THE INPUT MUST BE BETWEEN 1 AND 5 CHARACTERS. PLEASE TRY AGAIN!")
    exit()



# elif(isalpha(symbol)):
#     exit()
# def is_alpha_space(symbol): 


# else:
#     print(recommendation)
#if exit():
#   print("OOPS THE INPUT MUST BE BETWEEN 1 AND 5 CHARACTERS. TRY AGAIN!")


# else:
#    print(recommendation)
#     print("OOPS THE INPUT MUST BE LESS THAN 5 CHARACTERS. TRY AGAIN!")
#     exit()


# Validations (Prelim): Prevents an HTTP request if stock symbol not likely to be valid (e.g. symbol of "8888")
# Validations: Fails gracefully if encountering a response error (e.g. symbol of "OOPS")


request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(request_url)
# print(type(response)) #> class 'requests.models.Response'>
# print(response.status_code) #> 200
# print(response.text)

parsed_response = json.loads(response.text)
#print(parsed_response)
response_keys = list(parsed_response.keys())
#print(response_keys) # look at keys, is showing meta deta key or error? and go from there
# this is error message
#keys from response in list, timer series list or list in list in error message

if "Error Message" in response_keys:
    print("OOPS INVALID, PLEASE INPUT A VALID STOCK SYMBOL")
    exit()


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()

tsd = parsed_response["Time Series (Daily)"]


dates = list(tsd.keys()) #assumes first day is on top but sort to ensure latest day is first

latest_day = dates[0] #"2021-07-23"

latest_close = tsd[latest_day]["4. close"] 
latest_close = float(latest_close)

# get high price from each day
#maximum of all high prices
# high_prices = [10, 20, 30, 5]
# recent_high = max(high_prices)

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

#
# info outputs
#

# csv_file_path = "data/prices.csv" # a relative filepath
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers) 
    writer.writeheader() # uses fieldnames set above
    for date in dates: 
        daily_prices = tsd[date]
    # looping
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })

# float_string = float("12")
# print(float_string)

# https://careerkarma.com/blog/python-float/
# answer = round(12.2 + 14.6, 1)
# student_input = input("What is 12.2 + 14.6?")
# if float(student_input) == answer:
# 	print("You're right!")
# else:
# 	print("The correct answer to 12.2 + 14.6 is", answer, ".")


# ref actual variable

# (base)  --->> python -i
# Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 2+2
# 4
# >>> latest_close = "100"
# >>> print(latest_close)
# 100
# >>> type(latest_close)
# <class 'str'>
# >>> x = int(latest_close)
# >>> x
# 100
# >>> type(x)
# <class 'int'>
# >>> y = float(latest_close)
# >>> type(y)
# <class 'float'>
# >>> y
# 100.0
# >>> exit()

# loat_string = float()
# ex. If the stock's latest closing price is less than 20% above its recent low, "Buy", else "Don't Buy"
#if latest closing price is 30% below the recent high price then buy if not sell
# if "close"<"low"+"low"*float(".2"): #+ "low"*20%:
#     print("BUY")
# else:
#     print("DON'T BUY")


# if latest closing price is greater than 30% above highest recent price sell or if ir is more than 10% below highest recent price buy it
# THIS: I want to say "if the latest closing price is greater than 20% above the recent high price SELL, if it is more than 10% below the recent low price BUY, else HOLD". I'm not sure how to say this in a single statement

# x = recent_high*1.2
# if latest_close > x: 
#     recommendation = "sell"
# y = recent_low*1.3
# if latest_close < y:
#     recommendation = "buy"
# print(recommendation)

x = recent_high*.9
y = recent_low*1.1
if latest_close > x:
    recommendation = "RECCOMENDATION: SELL"
elif latest_close < y:
    recommendation = "RECOMMENDATION: BUY"
else:
    recommendation = "RECOMMENDATION: HOLD"
print(recommendation)


# x = recent_low*1.3
# if latest_close < x:
#     recommendation = "buy"
# else:
#     recommendation = "sell"
# print(recommendation)


# x = recent_low*.8
# if latest_close < x:
#      recommendation = "buy"
# else:
#     recommendation = "hold"
# print(recommendation)

# x = recent_low*1.2
# if latest_close < x:
#     print ("BUY")
# else:
#     print("DON'T BUY")



# simple but works
# if latest_close < recent_high:
#     recommendation = "BUY"
# else: 
#     recommendation = "DON'T BUY"
# # print(recommendation) 



#print("SELECTED SYMBOL:")
#print(symbol)
print("-------------------------")
print("LATEST STOCK MARKET DATA:")
#print("REQUEST AT 2018-02-20 02:00pm")
#print("REQUEST AT:", last_refreshed)
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
#print("-------------------------")
#print("RECOMMENDATION: BUY!")
#print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("THANKS FOR USING ROBO ADVISOR! HAPPY INVESTING! :)")
print("-------------------------")


