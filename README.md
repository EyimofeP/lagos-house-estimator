# Lagos House Price Estimator : Project Overview

An application that allows users to estimate the price of a residential property of their choice in Lagos state, Nigeria.

* Used **Beautiful Soup** to web scrap the data from a real estate company's website

* Performed various Data Preprocessing techniques to clean and make the data ready for model building

* Applied **Feature Engineering** to create new features such as the Neighborhood of the  and the type of duplex is the property

* **Exploratory Data Analysis** was used to discover insights in the data

* Modelled the data with various Machine Learning algorithms with LightGBM performing best

* **Tuned hyperparameters** of the model to achieve best performance.

* LightGBM had an Mean Absolute Error (MAE) score of ₦46.28 million

* Model was deployed on a web application built using **Django** available at [Lagos Estimator](lagos-estimator.onrender.com)
___
## Model Performamce

Mean Absolute Error (MAE) was used as the metric as the target data contained many outliers as Lagos state has properties as low as ₦55 million and as high as ₦1.2 billion 

| Model    |  MAE (₦ millions)   | 
|-----------|---------|
| Random Forest  | 47.98   |
| XGBoost | 47.66   |
| **LightGBM**   | **46.28**   |
| SVM   | 68.47   |
| KNN   | 49.07   |

The high MAE is due to many outliers in the target variable which are due to Nigeria's failing economy and poor political powerss leading to inflations of many properties. More features could be added to the dataset to achieve higher performance
___
## Model Deployment
The final model with the best score was deployed on a web application built with **Django** with the frontend built with **HTML & CSS** with **Boostrap 4** as the CSS Framework.

![Web application of the model](Plots/app.png)


___ 
## Data Collection
The data was web scraped from [PropertyPro NG](https://propertypro.ng), a Nigerian real estate website that contains thousands of listings of proporties around Lagos. Selected cities used for this project were Ikeja, Ikoyi, Lekki and Victoria Island.

```BeautifulSoup 4 ``` was used to scrap the data
___
## Data Preprocessing
Feature Engineering was used to extract new features such as:
* The neighborhood the property was located
* The type of duplex is the property e,g Semi-detached, Fully detached
* Location / City of the property e.g Lekki, Ikeja

Data Processing Techniques such as imputation of missing data, scaling of numerical features, encoding of categorical features was applied.
___
## Exploratory Data Analysis
According to analysis, the average (median) price of a residentaial property in Lagos state is around ₦99 million.

![Histogram of Prices](Plots/price-hist.png)

The prices are positively skewed with majority of prices as the lower rates.

Ikoyi has the most expensive homes with an average price of around ₦ 250 million.
![City Prices](Plots/city-prices.png)

___
