# 向已有的csv文件添加新的股票数据

import datetime as dt

import pandas as pd
import tushare as ts
from pandas import DataFrame

# 读入已有的数据
df = pd.read_csv('/Users/sajib/Desktop/wanyan_test/csv/stock_price.csv', index_col='TRADE_DATE',
                 parse_dates=['TRADE_DATE'])[['OPEN', 'CLOSE', 'HIGH', 'LOW', 'VOLUME', 'CODE']]

# 新数据从哪天开始读(最后一天加1天)
new_dt = df.index[-1] + dt.timedelta(days=1)

# 读新的数据，直接使用原有的股票代码
df1 = ts.get_k_data(df.code[0], new_dt.strftime("%Y-%m-%d"))

# 判断是否读到了新数据
if df1.size > 0:
    df1['TRADE_DATE'] = pd.to_datetime(df1['TRADE_DATE'])  # 把字符格式的日期转为日期对象
    df1.set_index('TRADE_DATE', inplace=True)  # 设为索引，以保持与原有数据格式的统一

    # 将新数据合并到已有的数据中
    df = df.append(df1)
    # TODO: Insert hot_rate.csv data, then combined with result.csv and generate new data
    # TODO: Process 3
    # 保存原有的和新读到的完整数据
    df.to_csv('/Users/sajib/Desktop/wanyan_test/csv/result.csv')
else:
    print("没有新数据")



