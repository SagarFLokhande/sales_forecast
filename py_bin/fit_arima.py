

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

# Manipulate the cleaned data for category "Furniture".
newfurn = dc.cleaned_furn_data("./raw_data/store_data.xls")
newfurn = newfurn.set_index("Order Date")
#newfurn.index
y = newfurn["Sales"].resample("MS").mean()


# This shows that the lowest AIC (Akaike Information Criterion) value (279.58) comes from SARIMAX(0,1,1)x(0,1,1,12). So we will fit this SARIMAX model (Seasonal Autoregressive Moving Average with eXogenous regressors model)


mod = sm.tsa.statespace.SARIMAX(y, order = (0,1,1), seasonal_order = (0,1,1,12),  enforce_invertibility = False)
results = mod.fit(disp = False)
print("Summary of SARIMAX fit: ")
print(results.summary().tables[1])
results.plot_diagnostics(figsize=(32,16))
print("Graphical diagnostics of our fit are plotted in 'fit_diagnostics.png'.")
plt.savefig("./plots/fit_diagnostics.png")

