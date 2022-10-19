# Predicting sales in the future. Our fit is SARIMAX (0,1,1)x(0,1,1,12)

import warnings, itertools, typing, matplotlib
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

# Import and order cleaned data.
newfurn = dc.cleaned_furn_data("./raw_data/store_data.xls")
newfurn = newfurn.set_index("Order Date")
newfurn.index
y = newfurn["Sales"].resample("MS").mean()

# Write the fitted SARIMAX model.
mod = sm.tsa.statespace.SARIMAX(y, order = (0,1,1), seasonal_order = (0,1,1,12),  enforce_invertibility = False)
results = mod.fit(disp = False)

# Using the model to visualize future sales.

pred_uc = results.get_forecast(steps=100)
pred_ci = pred_uc.conf_int()
ax = y.plot(label='observed', figsize=(14, 7))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index, pred_ci.iloc[:, 0], pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Furniture Sales')
plt.legend()
print("Future sales forecast is plotted in 'future_sales.png' as per our SARIMAX model.")
plt.savefig("./plots/future_sales.png")