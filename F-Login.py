from neo_api_client import NeoAPI
def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)
    
#on_message, on_open, on_close and on_error is a call back function we will provide the response for the subscribe method.
# access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
# environment by default uat you can pass prod to connect to live server
client = NeoAPI(consumer_key="", consumer_secret="", 
                environment='prod', on_message=on_message, on_error=on_error, on_close=None, on_open=None)

# Initiate login by passing any of the combinations mobilenumber & password (or) pan & password (or) userid & password
# Also this will generate the OTP to complete 2FA
client.login(mobilenumber="+919967341483", password="Adron@09")
MPIN = "201103"
# Complete login and generate session token
client.session_2fa(OTP=MPIN)

#Select User input
user_input = ''
while True:
     user_input = input ('select: Place_Order (PO)|Modify_Order(MO)|Cancel_Order(CO)|Order_Book(OB)|Quote(O)')

# Once 2FA has you can place the order by using below function
     if user_input.upper == 'PO':
client.place_order(exchange_segment='', product='', price='', order_type='', quantity=12, validity='', trading_symbol='',
                    transaction_type='', amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                    trigger_price="0", tag=None)
						
# Modify an order
elif user_input.upper == 'MO':
client.modify_order(order_id = "", price = 0, quantity = 1, disclosed_quantity = 0, trigger_price = 0, validity = "GFD")

# Cancel an order
elif user_input.upper == 'CO':
client.cancel_order(order_id = "")

# This is delay type. if order id along with isVerify as True will be passed then check the status of the given order id and then proceed to further
client.cancel_order(order_id = "", isVerify=True)

# Get Order Book
elif user_input.upper == 'OB':
client.order_report()

# Get Order History
elif user_input.upper == 'OH':
client.order_history(order_id = "")

# Get Trade Book
elif user_input.upper == 'TB':
client.trade_report()

# Get Detailed Trade Report for specific order id. 
elif user_input.upper == 'TRS':
client.trade_report(order_id = "")

# Get Positions
elif user_input.upper == 'P':
client.positions()

# Get Portfolio Holdings
elif user_input.upper == 'H':
client.holdings()

# Get Limits
elif user_input.upper == 'L':
client.limits(segment="", elif user_input.upper == 'MO':M':
client.margin_required(exchange_segment = "", price = "", order_type= "", product = "",   quantity = "", instrument_token = "",  transaction_type = "")

# Get Scrip Master CSV file
elif user_input.upper == 'SM':
client.scrip_master()

# Get Scrip Master CSV file for specific Exchange Segment. 
elif user_input.upper == 'SMS':
client.scrip_master(exchange_segment = "")

# Search for the Scrip details from Scrip master file
# exchange_segment is mandatory option to pass and remaining parameters are optional

client.search_scrip(exchange_segment="cde_fo", symbol="", expiry="", option_type="",
                    strike_price="")

# Get Quote details. 
elif user_input.upper == 'Q':
instrument_tokens = [{"instrument_token": "6531", "exchange_segment": "nse_cm"},
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""}]

# quote_type can be market_depth, ohlc, ltp, 52w, circuit_limits, scrip_details
# By Default quote_type is set as None that means you will get the complete data.
# Quotes api can be accessed without completing login by passing session_token, sid and server_id 
client.quotes(instrument_tokens = instrument_tokens, quote_type="", isIndex=False, 
              callback=on_message, session_token="", sid="",server_id="")

# Subscribe method will get you the live feed details of the given tokens.
# By Default isIndex is set as False and you want to get the live feed to index scrips set the isIndex flag as True 
# By Default isDepth is set as False and you want to get the depth information set the isDepth flag as True
client.subscribe(instrument_tokens = instrument_tokens, isIndex=False, isDepth=False)

# Un_Subscribes the given tokens. First the tokens will be checked weather that is subscribed. If not Subscribed we will send you the error message else we will unsubscribe the give tokens
client.un_subscribe(instrument_tokens=instrument_tokens)

#Order Feed 
client.subscribe_to_orderfeed()
#Terminate user's Session
client.logout()