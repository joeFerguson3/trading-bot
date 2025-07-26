from alpaca_trade_api.rest import REST, TimeFrame

# Credentials

BASE_URL = 'https://paper-api.alpaca.markets'

api = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

symbol = 'AAPL'
qty = 10
sell_at = 

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
    stop_price=180.00,     # triggers the order
    limit_price=179.50 
)

print("Order submitted:")
print(order)