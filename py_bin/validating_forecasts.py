
# Validating our forecasts model SARIMAX (0,1,1)x(0,1,1,12)

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

# Manipulate the cleaned data for category "Furniture".
newfurn = dc.cleaned_furn_data("./raw_data/store_data.xls")
newfurn = newfurn.set_index("Order Date")
newfurn.index
y = newfurn["Sales"].resample("MS").mean()
mod = sm.tsa.statespace.SARIMAX(y, order = (0,1,1), seasonal_order = (0,1,1,12),  enforce_invertibility = False)
results = mod.fit(disp = False)

# Graphically validating our forecasts
pred = results.get_prediction(start=pd.to_datetime("2017-01-01"), dynamic=False)
pred_ci = pred.conf_int()
ax = y["2014":].plot(label="observed")
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7, figsize=(32, 16))
ax.fill_between(pred_ci.index, pred_ci.iloc[:, 0], pred_ci.iloc[:, 1], color='k', alpha=.2)
ax.set_xlabel("Date")
ax.set_ylabel("Furniture Sales")
plt.legend()
print("Validation of our forecasts is plotted in 'valdating_forecasts.png'.")
plt.savefig("plots/validating_forecasts.png")

# Mean-squared and root-mean-squared errors for our fit.
y_forecasted = pred.predicted_mean
y_truth = y["2017-01-01":]
mse = ((y_forecasted - y_truth)**2).mean()
print("The mean-squared error of our forecasts is {}".format(round(mse,2)))
print("The root-mean-squared error of our forecasts is {}".format(round(np.sqrt(mse),2)))
