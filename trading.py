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
qty = 3
stop_price = round(price * 0.9, 2) # Price to sell stock at

order = api.submit_order(
    symbol=symbol,
    qty=qty,
    side='buy',
    type='market',
    time_in_force='gtc',
    order_class='bracket',
    take_profit={'limit_price': round(price * 1.05, 2)}, # Sell at 5% increase
    stop_loss={'stop_price': stop_price, 'limit_price': round(stop_price * 0.97, 2)}  # Stop loss
)

print("Order submitted:")