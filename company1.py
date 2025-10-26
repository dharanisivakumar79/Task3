# Customer Churn Prediction Project
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Step 1: Load the dataset
# You can download Telco Customer Churn dataset from Kaggle
# Dataset link: https://www.kaggle.com/blastchar/telco-customer-churn
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Step 2: Explore the dataset
print("Dataset Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Step 3: Data preprocessing
# Drop customerID as it's unique and not useful
df.drop("customerID", axis=1, inplace=True)

# Convert 'TotalCharges' to numeric, coerce errors to NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Encode categorical variables
for column in df.select_dtypes(include='object').columns:
    if df[column].nunique() == 2:  # Binary encoding
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
    else:  # One-hot encoding for multi-class
        df = pd.get_dummies(df, columns=[column])

# Step 4: Feature Scaling
scaler = StandardScaler()
numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[numeric_features] = scaler.fit_transform(df[numeric_features])

# Step 5: Split the dataset
X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Step 6: Build ML models

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_lr))
print(confusion_matrix(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))

# Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_dt))
print(confusion_matrix(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))

# Step 7: ROC Curve for the best model
y_pred_prob = rf.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
roc_auc = roc_auc_score(y_test, y_pred_prob)

plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label='Random Forest (AUC = %0.2f)' % roc_auc)
plt.plot([0,1],[0,1],'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

# Step 8: Feature Importance (Random Forest)
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': rf.feature_importances_})
feature_importance = feature_importance.sort_values(by='importance', ascending=False)

plt.figure(figsize=(12,8))
sns.barplot(x='importance', y='feature', data=feature_importance.head(20))
plt.title('Top 20 Feature Importance - Random Forest')
plt.show()

# Step 9: Save the model for future predictions
import joblib
joblib.dump(rf, "telecom_churn_model.pkl")
print("Model saved as telecom_churn_model.pkl")
