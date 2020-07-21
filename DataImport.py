import pandas as pd
from alpha_vantage.timeseries
import TimeSeries
import time

api_key = "2PNMXB7PYSF8WJYZ"

ts = TimeSeries(key = api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='AAPL', interval='1min',outputsize='full')
print(data)
