import yfinance as yf


import yahoo_fin.stock_info as si
msft_data = si.get_quote_table("ZIM")

print (msft_data)