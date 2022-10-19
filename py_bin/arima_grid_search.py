# Python program to find the best ARIMA model from historical time series data 

# First import all modules we expect to use

import warnings, itertools, matplotlib
import numpy as np, pandas as pd
import statsmodels.api as sm  # We need the .api to call statsmodels. 
from matplotlib import pyplot as plt
from pylab import rcParams
from statsmodels.api import tsa
import data_cleaning as dc

# Second, customize plot style.
warnings.filterwarnings("ignore")
plt.style.use("fivethirtyeight")
matplotlib.rcParams["axes.labelsize"] = 14
matplotlib.rcParams["xtick.labelsize"] = 12
matplotlib.rcParams["ytick.labelsize"] = 12
matplotlib.rcParams["text.color"] = "k"

# Obtain cleaned data with datetime index.
newfurn = dc.cleaned_furn_data("./raw_data/store_data.xls")
newfurn = newfurn.set_index("Order Date")
newfurn.index
y = newfurn["Sales"].resample("MS").mean()


# Grid search for ARIMA(s,t,n) model. s: seasonality, t: trend, n: noise.
s = t = n = range(0,2)
stn = list(itertools.product(s,t,n))
seasonal_stn = [ (x[0], x[1], x[2], 12) for x in stn ]

""" print("Examples of parameter combinations of seasonal ARIMA.")
print("SARIMAX: {} x {}".format(stn[1], seasonal_stn[2]))
print("SARIMAX: {} x {}".format(stn[3], seasonal_stn[4])) """



for param in stn:
    for param_seasonal in seasonal_stn:
        try:
            model = sm.tsa.statespace.SARIMAX(y, order=param, seasonal_order = param_seasonal, enforce_stationarity = False, enforce_invertibility = False)
            results = model.fit(disp = False)
            print("ARIMA{}x{} 12 - AIC-{}".format(param, param_seasonal, results.aic))
        except: 
            continue




# This shows that the lowest AIC (Akaike Information Criterion) value (279.58) comes from SARIMAX(0,1,1)x(0,1,1,12). So we will fit this SARIMAX model (Seasonal Autoregressive Moving Average with eXogenous regressors model)
# ARIMA(0, 1, 1)x(0, 1, 1, 12) 12 - AIC-279.5806233401351