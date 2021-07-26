# app/robo_advisor.py

import requests
import json


#
# info inputs
#

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)
# print(type(response)) #> class 'requests.models.Response'>
# print(response.status_code) #> 200
# print(response.text)
parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) #assumes first day is on top but sort to ensure latest day is first

latest_day = dates[0] #"2021-07-23"

latest_close = tsd[latest_day]["4. close"] 

# get high price from each day
#maximum of all high prices
# high_prices = [10, 20, 30, 5]
# recent_high = max(high_prices)

high_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))

recent_high = max(high_prices)

#
# info outputs
#

print("-------------------------")
print("SELECTED SYMBOL: MSFT")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

