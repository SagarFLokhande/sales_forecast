# Time Series Analysis and Forecasting with Python

# Contributor : Sagar F. Lokhande

* Data used : 
Large Excel Sheet data of a supermarket sales over a period of 3 years. It has 10000 entries, with many different categories of objects sold. The data can be downloaded from - https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls 

* Cleaning the data: 
First we focus on a particular category, example 'Furniture' sales. We use *numpy* and *pandas* to clean the data. We care about sales over time, so get rid of all other data, most of which is descriptive in the form of strings. We then sort the data according to date. 

* Sales over time: 
We use *matplotlib* to visaulize the sales data as a function of time. We notice multiple minima and maxima, indicating seasonality in the sales. Taking inspiration, we visualize the data differently using *time series decomposition.* For this we use *statsmodels* library.

* Seasonal ARIMA model for time series analysis : 
To understand the seasonal data better, we search for a Seasonal Autoregressive Integrated Moving-Average with eXogenous regressors (SARIMAX) model - https://www.statsmodels.org/dev/statespace.html.
For this we do a *grid search* and use the statespace method. We choose the model with the lowest Akaike Information Criterion (AIC), which turns out to have the parameters SARIMAX (0,1,1)x(0,1,1,12). Once we have a prospective model, we make sure that it is a good fit by performing a graphical *diagnostic* as well as by calculating mean-squared and root-mean-squared errors. 

* Forecasting using the chosen SARIMAX model: 
Having obained a good fit, we forecast future sales using our SARIMAX model. The forecast shows expected seasonality and is assumed to be a good fit for a finite number of years in the future. We also validate our forecasts by comparing the predicted values against the known (cleaned) data. 

This repo mostly uses Python, but there is a small interlude where we used a Unix Shell script to identify the best SARIMAX model. 

All the data, results and plots are included. 