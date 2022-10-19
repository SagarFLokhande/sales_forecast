# Python program to study historical time series data.

# First import all modules we expect to use
import warnings, itertools, typing, matplotlib
from matplotlib import pyplot as plt
from pylab import rcParams
import statsmodels.api as sm  # We need the .api to call the statsmodels module.
import data_cleaning as dc

# Second, customize plot style.
warnings.filterwarnings("default")
plt.style.use("fivethirtyeight")
matplotlib.rcParams["axes.labelsize"] = 14
matplotlib.rcParams["xtick.labelsize"] = 12
matplotlib.rcParams["ytick.labelsize"] = 12
matplotlib.rcParams["text.color"] = "k"

# Manipulate the cleaned data for category "Furniture".
newfurn = dc.cleaned_furn_data("./raw_data/store_data.xls")
newfurn = newfurn.set_index("Order Date")
newfurn.index

# The datetime index is useful but we will use avg daily sales value for a given month instead.
y = newfurn["Sales"].resample("MS").mean()

# Visualizing time series data
y.plot(figsize=(22,11))
print("Sales over time data is plotted in 'sales_over_time.png'. This is the historical data.")
plt.savefig("sales_over_time.png")

# Visualizing the same data using time-series-decomposition. This method decomposes the time series data into: trend, seasonality and noise. 
rcParams['figure.figsize'] = 28, 12
decomposition = sm.tsa.seasonal_decompose(y, model='additive')
fig = decomposition.plot()
print("Time seris decomposition of historical data is plotted in 'ts_decomp_data.png'.")
plt.savefig("./plots/ts_decomp_data.png")