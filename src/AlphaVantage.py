
#!/usr/bin/env python
# coding: utf-8

#pip install alpha_vantage

# **Instala soporte para Pandas**

#pip install alpha_vantage pandas

import pypm
from pypm import metrics

import matplotlib
import matplotlib.pyplot as plt
import os
# Make plots bigger
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)

pd.set_option('max_colwidth', 400)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# **Ver el precio de intercambio al cierre**

from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='1035HSNE5D7XWHLM',output_format='pandas')
# There is no metadata in this call
data_exchange_rate, meta_exchange_rate = cc.get_currency_exchange_rate(from_currency='GBP',to_currency='AUD')
pprint(data_exchange_rate)
data_exchange_rate.head()
# para analisis diario

data_daily, meta_daily = cc.get_currency_exchange_daily ('GBP','AUD',outputsize='compact')
pprint(data_daily)

data_daily.head()

# para analisis mensual

data_monthly, meta = cc.get_currency_exchange_monthly('GBP','AUD',outputsize='compact')
pprint(data_monthly)
data_monthly.head()


# Ver el intraday para el calculo de banderas

data_intraday, meta_intraday = cc.get_currency_exchange_intraday('GBP','AUD',interval='15min',outputsize='compact')
pprint(data_intraday)
data_intraday.head()

