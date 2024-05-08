from asyncio import streams
from email import message
from re import S
#from lib2to3.pygram import Symbols
from pytest import Item
import requests
from json import load
import json
import os
from urllib import response
#from pickle import NONE
import schedule
os.system("ipconfig /flushdns")
import websockets
#from lib2to3.fixes.fix_imports import MAPPING
import pandas as pd
from datetime import datetime as dt, date
from dateutil.relativedelta import relativedelta
import threading as Thread
import openpyxl
import csv
import requests
today = date.today()
# Functions setup

d1 = today.strftime("%d.%m.%Y")

from neo_api_client import NeoAPI
def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

consumerkey = "wbMFt2gIs3vpld8UmyxK9Az"
consumersecret ="XUOfDmiktXGeeSNapthRgL"    
#on_message, on_open, on_close and on_error is a call back function we will provide the response for the subscribe method.
# access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
# environment by default uat you can pass prod to connect to live server
client = NeoAPI(consumer_key=consumerkey, consumer_secret=consumersecret, 
                environment='prod', on_message=on_message, on_error=on_error, on_close=None, on_open=None)

# Initiate login by passing any of the combinations mobilenumber & password (or) pan & password (or) userid & password
# Also this will generate the OTP to complete 2FA
client.login(mobilenumber="+919967341483", password="Adron@1903")

MPIN="201103"
# Complete login and generate session token
client.session_2fa(OTP=MPIN)

# Once 2FA has you can place the order by using below function
user_input = ''

while True:
    user_input = input(
        'Select: Place_Order(PO) | Modify_Order(MO) | Cancel_Order(CO) | Order_Report (OR) | Order_History(OH) | Trade_Report (TR) | Specific_Order_Trade_Report (SOTR) | Positions (P) | Holdings (H) | Limits(L) | Margin(M) | ScripMaster(SM) | Scrip Specific Segment(SSS) | Search_Scrip (SS) | Quote (Q)' )

# Place_Order
    if user_input.upper() == 'PO':
            client.place_order(exchange_segment='', product='', price='', order_type='', quantity=12, validity='', trading_symbol='',
                    transaction_type='', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                    trigger_price="0", tag=None)
            break          
    
# Modify an order
    elif user_input.upper() == 'MO':
        client.modify_order(order_id = "", price = 0, quantity = 1, disclosed_quantity = 0, trigger_price = 0, validity = "GFD")
        break    
    
# Cancel an order
    elif user_input.upper() == 'CO':
        client.cancel_order(order_id = "")
        break
    
# This is delay type. if order id along with isVerify as True will be passed then check the status of the given order id and then proceed to further
# client.cancel_order(order_id = "", isVerify=True)

# Get Order Book
    elif user_input.upper() == 'OR':
        client.order_report()
        break
        
# Get Order History
    elif user_input.upper() == 'OH':
        client.order_history(order_id = "")
        break
    
# Get Trade Book
    elif user_input.upper() == 'TR':
        client.trade_report()
        break

# Get Detailed Trade Report for specific order id. 
    elif user_input.upper() == 'SOTR':
        client.trade_report(order_id = "")
        break
    
# Get Positions
    elif user_input.upper() == 'P':
        client.positions()
        break
    
# Get Portfolio Holdings
    elif user_input.upper() == 'H':
        client.holdings()
        break
          
# Get Limits
    elif user_input.upper() == 'L':
        client.limits(segment="", exchange="", product="")
        break
          
# Get Margin required for Equity orders. 
    elif user_input.upper() == 'M':
        client.margin_required(exchange_segment = "", price = "", order_type= "", product = "",   quantity = "", instrument_token = "",  transaction_type = "")
        break
    
# Get Scrip Master CSV file
    elif user_input.upper() == 'SM':
        client.scrip_master()
        break

# Get Scrip Master CSV file for specific Exchange Segment. 
    elif user_input.upper() == 'SSS':
        client.scrip_master(exchange_segment = "nse_cm")
        break

# Get Quote details. 
    elif user_input.upper() == 'Q':
        instrument_tokens = [{"instrument_token": "30108", "exchange_segment": "nse_cm"},
                             {"instrument_token": "12531", "exchange_segment": "nse_cm"},
                             {"instrument_token": "12024", "exchange_segment": "nse_cm"},
                             {"instrument_token": "12194", "exchange_segment": "nse_cm"}]
        #instrument_tokens = [{"instrument_token": "11536", "exchange_segment": "nse_cm" }]                
        # json_data = client.quotes(instrument_tokens = instrument_tokens, quote_type="ltp", isIndex=False)
        quotes = client.quotes(instrument_tokens=instrument_tokens, quote_type="ltp", isIndex=False)
        
        filename = "HistoryIntra" + d1 + ".csv"

        #def handle_quote(quote):
            # Check if the file exists and is empty
        file_exists = os.path.isfile(filename)
        is_empty = not os.path.getsize(filename) > 0 if file_exists else False
        
        with open("HistoryIntra"+d1+".csv", mode='a', newline='') as f:
            writer = csv.writer(f)
            # Write the header if the file is new/empty
            if not file_exists or is_empty:
                writer.writerow(['Instrument Token', 'LTP'])
                    
            # Write each quote's data    
            for quote in quotes['message']:
                instrument_token = quote['instrument_token']
                ltp = float(quote['ltp'])
                writer.writerow([instrument_token, ltp,])
        # Start streaming quotes
        #Thread(instrument_tokens, handle_quote(quote))
        #stream_quotes(instrument_tokens, handle_quote)            
             #def job():
             #   writer.writerow([instrument_token, ltp, ts])
             #    schedule.every(0.01).minutes.do(job)    
        #print(df)
        #print(ltp)
        #if 'ltp' in response:
        #    quote = float(response['ltp'])
        #else:
        #    print("Key 'ltp' not found in the response.")
        #print(ltp)
        #quotes_series = pd.Series(data)#quotes_data.quote_type)
        #df = pd.DataFrame(quotes_series)
      
        #def job():
        #    with open("HistoryIntra"+d1+".csv", mode='a') as file:
        #        file.write(df)
        #schedule.every(0.01).minutes.do(job)    
        #response = float(
        client.subscribe(instrument_tokens = instrument_tokens, isIndex=False, isDepth=False)
        #['message'][0]['ltp'])
        #df_string = str(response)
        #string_list = df_string.split(',')
        #with open("HistoryIntra"+d1+".csv", mode='a') as file:
        #    for string in string_list:
        #     (string + '\n')
        #print(response)
  
# quote_type can be market_depth, ohlc, ltp, 52w, circuit_limits, scrip_details
# By Default quote_type is set as None that means you will get the complete data.
# Quotes api can be accessed without completing login by passing session_token, sid and server_id 

        #client.quotes(instrument_tokens = instrument_tokens, quote_type="ltp", isIndex=False)#, callback=on_message,)# session_token="", sid="",server_id="")
        #client.quotes(instrument_tokens = instrument_tokens, quote_type="ltp", isIndex=False)
#**********************************************************************************************************************
   #     quotes_data = client.quotes(instrument_tokens = instrument_tokens, quote_type="ltp", isIndex=False)
   #     with open("HistoryIntra"+d1+".csv", mode='a') as file:
   #         file.write(str(quotes_data))

#**************************************************************************************     
  
        #quotes_series = pd.Series(client.quotes)#quotes_data.quote_type)
        #df = pd.DataFrame(quotes_data)
        
        #df.to_csv("HistoryIntra"+d1+".csv", mode='a', index = False, header= True)

              
        
        #response = client.quotes(instrument_tokens = instrument_tokens, quote_type="ltp")  # Replace with actual API call
        #for item in response:
        #    ts = item.get('ts')
        #    ltp = item.get('ltp')
        #    print(f"Ticker Symbol (ts): {ts}, Last Traded Price (ltp): {ltp}")

        
        #quotes_res = client.quotes(instrument_tokens = instrument_tokens, quote_type="ltp")

        #for quote in quotes_res:
        #    symbol_name = client.quotes.get("ts")
        #    ltp = quote.get("ltp")
        #    print(f"Symbol: {symbol_name}, LTP: {ltp}")

        # b = json.dumps(client.quotes)
        
        #df = pd.DataFrame({'TS' : pd.Series(client.quotes), 'LTP' : pd.Series(client.quotes)})
        #df.to_csv("HistoryIntra"+d1+".csv", index = False, header= True)
        #with open("HistoryIntra"+d1+".csv", 'w'):
        
        
        #print(client.ltp)
# Subscribe method will get you the live feed details of the given tokens.
# By Default isIndex is set as False and you want to get the live feed to index scrips set the isIndex flag as True 
# By Default isDepth is set as False and you want to get the depth information set the isDepth flag as True

        
        # close the file
     #   f.close()
     #   break
    
    else:
        print('Invalid Selection')
        continue						

# Un_Subscribes the given tokens. First the tokens will be checked weather that is subscribed. If not Subscribed we will send you the error message else we will unsubscribe the give tokens
#client.un_subscribe(instrument_tokens=instrument_tokens)

#Order Feed 
#client.subscribe_to_orderfeed()
#Terminate user's Session
client.logout()