from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv
import os

# Credentials
load_dotenv()
API_KEY = os.getenv("ALPACA_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
print(API_KEY)
print(SECRET_KEY)
BASE_URL = 'https://paper-api.alpaca.markets'

api = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)


price = api.get_latest_quote('AAPL') # Current price of stock
price = float(price.ask_price)
symbol = 'AAPL'
qty = 10
stop_price = round(price * 0.9, 2) # Price to sell stock at

# Buys stock
order = api.submit_order(
    symbol=symbol,
    qty=qty,
    side='buy',
    type='market',
    time_in_force='fok'
)

# Sets stop limit
sell = api.submit_order(
    symbol=symbol,
    qty=qty,
    side='sell',
    type='stop_limit',
    time_in_force='gtc',
    stop_price=stop_price,
    limit_price=round(stop_price * 0.97, 2)
)

print("Order submitted:")
print(order)