import pandas_datareader.data as web
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 12, 31)

gs = web.DataReader("078930.KS", "yahoo", start, end)
print(gs)