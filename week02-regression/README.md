# Machine Learning Engineering (Zoomcamp) - Data Talks 

## 2 - Machine Learning for Regression

* 2.1 - Car price prediction project
    * Prepare data and Exploratory data analysis (EDA)
    * Use linear regression for predicting price
    * Understanding the internals of linear regression
    * Evaluating the model with RMSE
    * Feature engineering
    * Regularization
    * Using the model
    
* 2.2 - Data preparation
Downloading the data and importing the librarys

* 2.3 - Exploratory Data Analysis (EDA)
    * Ploting the price distribution and making more normal
    * Counting the number of missing values
    
* 2.4 - Setting Up The Validation Framework

        TRAIN              | VALIDATION     | TEST

        (X_train, y_train) | (X_val, y_val) | (X_test, y_test)
        
* 2.5 - Linear regression
Understanding the linear regression:

$$ g(x) = w_0 + \sum_{i=0}^{n-1} w_i x_i $$,

where $w_j$ are the *weights*

* 2.6 - Linear regression vector form
Understanding how to calculate linear regression for multiple training examples

* 2.7 - Training linear regression: Normal equation
	
		Xw = y => (X.TX)w = X.Ty => (X.TX)^-1(X.TX)w = (X.Tx)^-1X.Ty
	
* 2.8 - Baseline model for car price prediction project

* 2.9 - Root mean squared error

* 2.10 - Using RMSE on validation data

* 2.11 - Feature engineering

* 2.12 - Categorical variables

* 2.13 - Regularization

* 2.14 - Tuning the model

* 2.15 - Using the model
