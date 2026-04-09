Task 1:

Label: repeat_purchase_flag

Justification: This is the target variable because it directly indicates whether the customer made a repeat purchase within 30 days, which is exactly what we are trying to predict.

Data leakage column: discount_used_on_repeat_order

Justification: This column would introduce leakage because it contains information about the repeat purchase event itself (which happens after the prediction point), so using it would give the model access to future information.

Task 2:
Exploratory Data Analysis (EDA):

Before modeling, it’s important to understand the data distribution, missing values, feature relationships, and class imbalance, which helps in making informed decisions about preprocessing and feature selection.

Train-test split (or validation strategy):

Splitting the data into training and testing sets ensures that model performance is evaluated on unseen data, preventing overfitting and giving a realistic estimate of how the model will perform in production.