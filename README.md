## Student Performance Prediction Model

##In cmd

clone project
```
git clone https://github.com/ashay-thamankar/Student-Performance-Prediction-Model.git
```

train the model
```
python src/components/data_ingestion.py
```

to run the flask application
```
python app.py
```

# Black Friday Sales Prediction Model 🛍️💰

## Overview 📊

This project aims to predict Black Friday sales using machine learning techniques. By analyzing a dataset containing various customer attributes and purchase details, we strive to gain insights into buying patterns and build a predictive model.

## Table of Contents 📑

1. [Introduction](#introduction)
2. [Dataset Exploration](#dataset-exploration)
    - [Data Overview](#data-overview)
    - [Data Preprocessing](#data-preprocessing)
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
    - [Data Distributions and Skewness](#data-distributions-and-skewness)
    - [Gender Distribution](#gender-distribution)
    - [Gender-wise Purchase Comparison](#gender-wise-purchase-comparison)
    - [Marital Status Distribution by Gender](#marital-status-distribution-by-gender)
    - [Occupation Impact on Purchases](#occupation-impact-on-purchases)
    - [Purchase Distribution by Age](#purchase-distribution-by-age)
    - [Purchase Distribution by Gender](#purchase-distribution-by-gender)
    - [Purchase Distribution by Occupation and Gender](#purchase-distribution-by-occupation-and-gender)
    - [Purchase Distribution by Occupation](#purchase-distribution-by-occupation)
    - [Purchase Distribution by Product Category 1](#purchase-distribution-by-product-category-1)
4. [Model Development](#model-development)
    - [Data Preparation](#data-preparation)
    - [Model Selection](#model-selection)
        - [Linear Regression](#linear-regression)
        - [Decision Tree Regressor](#decision-tree-regressor)
        - [Random Forest Regressor](#random-forest-regressor)
    - [Model Evaluation](#model-evaluation)
5. [Final Model](#final-model)
    - [Prediction using Final Model](#prediction-using-final-model)
6. [Conclusion](#conclusion)

## Introduction 🚀

_Black Friday_ is a significant shopping event, and understanding the factors influencing sales can provide valuable insights for both retailers and consumers. In this project, we employ machine learning to predict Black Friday sales based on customer demographics and purchase behavior.

## Dataset Exploration 📊

### Data Overview

The dataset contains information about customers, including their gender, age, marital status, occupation, and purchase details. Exploring and preprocessing the data is the initial step in building an effective predictive model.

### Data Preprocessing

Handling missing values, encoding categorical variables, and other preprocessing steps are crucial for preparing the data for analysis.

## Exploratory Data Analysis (EDA) 📈

Exploratory Data Analysis involves visualizing and interpreting the dataset to extract meaningful insights. Let's explore some key aspects:

### Data Distributions and Skewness

![Data Distributions](charts/Exploring%20Data%20Distributions%2C%20Detecting%20Skewness%20with%20Density%20Plots.png)

### Gender Distribution

![Gender Distribution](charts/Gender%20Distribution%2C%20Male%20Count%20Outnumbers%20Female%20Count%20countplot.png)

### Gender-wise Purchase Comparison

![Gender-wise Purchase Comparison](charts/Gender-wise%20Purchase%20Comparison%2C%20Higher%20Purchases%20by%20Males%20barplot.png)

### Marital Status Distribution by Gender

![Marital Status Distribution by Gender](charts/Marital%20Status%20Distribution%20by%20Gender%20%2C%20Slight%20Female%20Majority%20barplot.png)

### Occupation Impact on Purchases

![Occupation Impact on Purchases](charts/Occupation%20Impact%20on%20Purchases%2C%20Higher%20Activity%20Noted%20for%20Codes%2012%2C%2015%2C%2017%20countplot.png)

### Purchase Distribution by Age

![Purchase Distribution by Age](charts/Purchase%20Distribution%20by%20Age%2C%20Identifying%20Outliers%20with%20Boxplot.png)

### Purchase Distribution by Gender

![Purchase Distribution by Gender](charts/Purchase%20Distribution%20by%20Gender%2C%20Outlier%20Detection%20with%20Boxplot.png)

### Purchase Distribution by Occupation and Gender

![Purchase Distribution by Occupation and Gender](charts/Purchase%20Distribution%20by%20Occupation%20and%20Gender%20%2C%20Females%20Lead%20in%20Purchases%20barplot.png)

### Purchase Distribution by Occupation

![Purchase Distribution by Occupation](charts/Purchase%20Distribution%20by%20Occupation%2C%20Identifying%20Outliers%20with%20boxplot.png)

### Purchase Distribution by Product Category 1

![Purchase Distribution by Product Category 1](charts/Purchase%20Distribution%20by%20Product%20Category%201%2C%20Identifying%20Outliers%20with%20Boxplot.png)

## General Analysis 📈

The exploratory data analysis reveals interesting insights into customer behavior during Black Friday sales:

- **Gender Impact:** Males exhibit a higher purchasing tendency than females.
- **Occupation Influence:** Occupations with codes 12, 15, and 17 show increased purchasing activity.
- **Age and Marital Status:** Slight female majority is observed in the dataset's marital status distribution.

## Model Development 🤖

### Data Preparation

Before building models, we preprocess the data, splitting it into training and testing sets.

### Model Selection

#### Linear Regression

- R2 Score: 0.20
- RMSE: 0.67

#### Decision Tree Regressor

- R2 Score on Training Data: 0.75
- R2 Score on Test Data: 0.76
- RMSE on Training Data: 0.37
- RMSE on Test Data: 0.37

#### Random Forest Regressor

- R2 Score on Training Data: 0.97
- R2 Score on Test Data: 0.78
- RMSE on Training Data: 0.13
- RMSE on Test Data: 0.35

## Final Model 🏆

The **Random Forest Regressor** is selected as the final model due to its superior performance:

- R2 Score: 0.78
- RMSE on Test Data: 0.35

### Prediction using Final Model

Predictions are made on the test data using the final model.

## Conclusion 🎉

This comprehensive Black Friday Sales Prediction Model project demonstrates the significance of exploratory data analysis and model evaluation in developing accurate machine learning models. The insights gained from the data analysis contribute to informed decision-making, and the selected Random Forest Regressor showcases its prowess in predicting Black Friday sales.

