# Changlog 
# Added Indices TSI < 0 crossover indicator 
# Re organized the output on telegram 


#source : https://www.youtube.com/watch?v=DLqB6ly5k0I
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

Charting_url ='https://chartink.com/screener/process'

Condition = {'scan_clause' : '( {57960} ( latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < 0 and latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} < 0 and latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 day ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} <= 1 day ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

Exit_Condition = {'scan_clause': '( {57960} ( latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > 0 and latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} > 0 and latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 day ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} >= 1 day ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

Weekly_Entry_Condition = {'scan_clause': '( {57960} ( weekly {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < 0 and weekly {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} < 0 and weekly {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > weekly {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 week ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} <= 1 week ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

Indice_Daily_Entry_condition = {'scan_clause':'( {45603} ( latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} < -5 and latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} < -5 and latest {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} > latest {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} and 1 day ago  {custom_indicator_23679_start}"(  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} ) * 100"{custom_indicator_23679_end} <= 1 day ago  {custom_indicator_23680_start}"ema(  {custom_indicator_22715_start} "100 * (  {custom_indicator_22711_start}"ema(  ema(  {custom_indicator_22709_start} "close - 1 candle ago close"{custom_indicator_22709_end} , 25 ) , 13 )"{custom_indicator_22711_end} /  {custom_indicator_22714_start}"ema(  ema(  {custom_indicator_22712_start}"abs(  close - 1 candle ago close )"{custom_indicator_22712_end} , 25 ) , 13 )"{custom_indicator_22714_end} )"{custom_indicator_22715_end} , 13 )"{custom_indicator_23680_end} ) ) '}

with requests.session() as s:
r_data = s.get(Charting_url)
soup = bs(r_data.content, "lxml")
meta = soup.find("meta",{"name" : "csrf-token"})["content"]

```
header = {"X-Csrf-Token" : meta}

# Fetching Entry Stock
data = s.post(Charting_url, headers=header, data=Condition).json()
stock_list = pd.DataFrame(data["data"])
print (stock_list)
telegram_output = stock_list

# Fetching Exit Stocks
data = s.post(Charting_url, headers=header, data=Exit_Condition).json()
exit_stock_list = pd.DataFrame(data["data"])
print (exit_stock_list)
exit_telegram_output = exit_stock_list

# Fetching WEEKLY Entry Stock
data = s.post(Charting_url, headers=header, data=Weekly_Entry_Condition).json()
weekly_tsi_entry_stock_list = pd.DataFrame(data["data"])
print (weekly_tsi_entry_stock_list)
weekly_tsi_entry_stock_list_telegram_output = weekly_tsi_entry_stock_list

# Fetching Indices Entry Stock
data = s.post(Charting_url, headers=header, data=Indice_Daily_Entry_condition).json()
indices_entry_stock_list = pd.DataFrame(data["data"])


# Select the desired columns for Entry stocks
filtered_stock_list = stock_list[['sr', 'nsecode', 'close']]
print(filtered_stock_list)

# Select the desired columns for Exit stocks
exit_filtered_stock_list = exit_stock_list[['sr', 'nsecode', 'close']]
print(exit_filtered_stock_list)

# Select the desired columns for Exit stocks
weekly_tsi_entry_stock_list_filtered = weekly_tsi_entry_stock_list[['sr', 'nsecode', 'close']]
print(weekly_tsi_entry_stock_list_filtered)

# Select the desired columns for Indices Entry stocks
indices_entry_stock_list_filtered = indices_entry_stock_list[['sr', 'nsecode', 'close']]
print(indices_entry_stock_list_filtered)


```

# Sending Stock list to python

TOKEN='7449783431:AAHqe61k6R14Z_YismA2VEJYeXsACZbpgYg'
url = f"[https://api.telegram.org/bot{TOKEN}/getUpdates](https://api.telegram.org/bot%7BTOKEN%7D/getUpdates)"

#test chat id
#chat_id="-4287405834"

# Original chat id

chat_id="-1002199303920"

strategy_name = "Daily chart ENTRY: TSI Screener"
message = filtered_stock_list.to_string(index=False).replace('&', '%26')
#message = filtered_stock_list.to_string(index=False)
url = f"[https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={strategy_name}\\n\\n{message}](https://api.telegram.org/bot%7BTOKEN%7D/sendMessage?chat_id=%7Bchat_id%7D&text=%7Bstrategy_name%7D%5C%5Cn%5C%5Cn%7Bmessage%7D)"
print(requests.get(url).json())

strategy_name = "Weekly chart ENTRY: TSI Screener"
message = weekly_tsi_entry_stock_list_filtered.to_string(index=False).replace('&', '%26')
#message = weekly_tsi_entry_stock_list_filtered.to_string(index=False)
url = f"[https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={strategy_name}\\n\\n{message}](https://api.telegram.org/bot%7BTOKEN%7D/sendMessage?chat_id=%7Bchat_id%7D&text=%7Bstrategy_name%7D%5C%5Cn%5C%5Cn%7Bmessage%7D)"
print(requests.get(url).json())

strategy_name = "Daily chart ENTRY: Indices Only - TSI Screener"
message = indices_entry_stock_list_filtered.to_string(index=False).replace('&', '%26')
#message = indices_entry_stock_list_filtered.to_string(index=False)
url = f"[https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={strategy_name}\\n\\n{message}](https://api.telegram.org/bot%7BTOKEN%7D/sendMessage?chat_id=%7Bchat_id%7D&text=%7Bstrategy_name%7D%5C%5Cn%5C%5Cn%7Bmessage%7D)"
print(requests.get(url).json())

strategy_name = "Daily chart EXIT: TSI Screener"
message = exit_filtered_stock_list.to_string(index=False).replace('&', '%26')
#message = exit_filtered_stock_list.to_string(index=False)
url = f"[https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={strategy_name}\\n\\n{message}](https://api.telegram.org/bot%7BTOKEN%7D/sendMessage?chat_id=%7Bchat_id%7D&text=%7Bstrategy_name%7D%5C%5Cn%5C%5Cn%7Bmessage%7D)"
print(requests.get(url).json())
