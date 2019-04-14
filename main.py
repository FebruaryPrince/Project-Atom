get_ipython().system('pip install quandl')
get_ipython().system('pip install fbprophet')
get_ipython().system('pip install pytrends')

from stocker import Stocker
import quandl
quandl.ApiConfig.api_key = 'AsJgrNdvc_MbnWxwNB4V'
import matplotlib.pyplot as plt

ms = Stocker('MSFT')

ms.plot_stock()
ms.changepoint_date_analysis()
ms.buy_and_hold(start_date='2017-09-01', end_date='2018-03-01', nshares=100)
model, future = ms.create_prophet_model(days=180)
