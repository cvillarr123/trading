#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/cvillarr123/trading/blob/master/notebook/AlphaVantage.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:


#pip install alpha_vantage


#
# **Instala soporte para Pandas**

# In[ ]:


#pip install alpha_vantage pandas


# In[ ]:


import matplotlib
import matplotlib.pyplot as plt
import os
# Make plots bigger
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)


# **Ver el precio de intercambio al cierre**

# In[ ]:


from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='1035HSNE5D7XWHLM')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='GBP',to_currency='AUD')
pprint(data)


# In[ ]:





#

# In[ ]:


from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='1035HSNE5D7XWHLM', output_format='pandas')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='GBP',to_currency='AUD')
pprint(data)


# In[ ]:


data.head()


# Ver el intraday para el calculo de banderas

# In[ ]:


data, _ = cc.get_currency_exchange_intraday('GBP','AUD',interval='15min',outputsize='compact')
pprint(data)


# In[ ]:


data.head()


#

# In[ ]:


data, _ = cc.get_currency_exchange_daily ('GBP','AUD',outputsize='compact')
pprint(data)


# In[ ]:


data.head()


# In[ ]:


data.count()


# In[ ]:


data, _ = cc.get_currency_exchange_monthly('GBP','AUD',outputsize='compact')
pprint(data)
data.head()


# In[ ]:


data, _  = cc.get_currency_exchange_monthly('GBP','AUD',outputsize='compact')


# In[ ]:


type(data)


# In[ ]:


pprint(data)


# In[ ]:


data.head()


# In[ ]:


