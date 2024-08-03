# Bank customer Churn Prediction

## Domain : Banking

## Introduction:

Customer churn prediction is crucial for banks to retain customers by identifying those at risk of leaving. This project uses multiple classification algorithms to predict customer churn, with the Random Forest Classifier being the most accurate.

## DataSet
The dataset used in this project includes the following columns:

CustomerId: Unique identifier for each customer
Surname: Customer's last name
CreditScore: Customer's credit score
Geography: Customer's geographical location
Gender: Customer's gender
Age: Customer's age
Tenure: Number of years the customer has been with the bank
Balance: Customer's account balance
NumOfProducts: Number of products the customer has with the bank
HasCrCard: Whether the customer has a credit card (1 for yes, 0 for no)
IsActiveMember: Whether the customer is an active member (1 for yes, 0 for no)
EstimatedSalary: Customer's estimated annual salary
Exited: Whether the customer has exited the bank (1 for yes, 0 for no)

## Data Preprocessing
Data preprocessing involves cleaning and transforming the raw data into a suitable format for model training. The steps include:

Handling Missing Values: Check and handle any missing values in the dataset.
Encoding Categorical Variables: Convert categorical variables such as 'Geography' and 'Gender' into numerical values using techniques like one-hot encoding.
Feature Scaling: Normalize or standardize numerical features to ensure they are on the same scale.
Splitting Data: Split the dataset into training and testing sets

## Model Training
Multiple classification algorithms are trained on the preprocessed data to predict customer churn. The algorithms include:

Logistic Regression
Ada Boost Classifier
Random Forest Classifier
Gradient Boosting Classifier
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
ExtraTrees Classifier
Bagging Classifier

## Model Evaluation

The models are evaluated using various metrics, with a focus on accuracy. The ROC-AUC curve is also plotted to visualize the performance.

Results
The Random Forest Classifier achieved the highest accuracy of 89%. Here is a summary of the results:


Algorithm	Accuracy
Random Forest Classifier	89%
Extra Trees Classifier	88%
Bagging Classifier	88%
Gradient Boosting	87%
KNN	84%
SVM	82%
Ada Boost	82%
Logistic Regression	79%
This order reflects the best-performing models at the top.
