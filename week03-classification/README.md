# Machine Learning Engineering (Zoomcamp) - Data Talks 

## 3 - Machine Learning for Classification

* 3.1 - Churn Prediction Project
We want to indentify clients which can churn our telco service and for those clients we want to give some discount to avoid that.

Class of the problem: **binary classification**
In binary classification we want to find a model $ g $ that can predict values between $ 0 $ and $ 1 $, 
    $$ g(x_i) = y_i $$
where $ x_i $ is our training example and $ y_i $ our target variable ($ y_i \in \{0, 1\} $).

* 3.2 - Data Preparation
Download and preparation of the data.

* 3.3 - Setting Up The Validation Framework
Spliting the data with sklearn.

* 3.4 - EDA

* 3.5 - Feature Importance: Churn Rate And Risk Ratio

* 3.6 - [Feature Importance: Mutual Information](https://en.wikipedia.org/wiki/Mutual_information)
Finding a way to measure the importance between categorical variables.

* 3.7 - Feature Importance: Correlation
A way to measure numerical features.

* 3.8 - One-Hot Encoding

* 3.9 - Logistic Regression

* 3.10 - Training Logistic Regression with Scikit-Learn

* 3.11 - Model Interpretation

* 3.12 - Using the Model

* 3.13 - Summary

    - Feature importance - risk, mutual information, correlation
    
    - One-hot encoding can be implemented with DictVectorizer
    - Logistic regression - linear model like linear regression
    - Output of log reg - probability
    - Interpretation of weights is similar to linear regression
