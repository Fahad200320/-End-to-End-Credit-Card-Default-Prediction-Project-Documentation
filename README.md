🧾 End-to-End Credit Card Default Prediction Project Documentation



📌 Project Title:

**Credit Card Default Prediction using Machine Learning**



 📖 Problem Statement:

Credit card companies face challenges in identifying customers likely to default on their payments. Early detection can reduce financial risk. The goal of this project is to build a machine learning model that predicts whether a customer will default on their credit card payment next month.



📊 Dataset Description:

* **Source:** [UCI Machine Learning Repository](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)
* **Records:** 30,000 customers
* **Duration:** April 2005 to September 2005
* **Target Variable:** `default.payment.next.month` (1 = default, 0 = no default)

🎯 Features:

* **Demographics:** `SEX`, `EDUCATION`, `MARRIAGE`, `AGE`
* **Credit & Billing:** `LIMIT_BAL`, `BILL_AMT1` to `BILL_AMT6`
* **Payment History:** `PAY_0` to `PAY_6`
* **Payment Amounts:** `PAY_AMT1` to `PAY_AMT6`



🧹 Data Preprocessing:

* Renamed the target column to `default`
* Checked for null and duplicate values
* Scaled features using **StandardScaler**
* Performed **train-test split** (80/20)



📈 Exploratory Data Analysis (EDA):

* **Visualizations:**

  * Count plots for categorical features
  * Histograms and boxplots for numerical features
  * Correlation heatmap
* **Insights:**

  * Males default slightly more often than females
  * Higher `PAY_X` values (delays in payments) correlate with default
  * Younger age groups tend to default more


 ⚙️ Model Building:

✅ Models Trained:

| Model                     | Accuracy | F1-Score |
| ------------------------- | -------- | -------- |
| Logistic Regression       | 0.77     | 0.77     |
| Decision Tree             | 0.81     | 0.81     |
| **Random Forest**         | **0.84** | **0.84** |
| AdaBoost                  | 0.80     | 0.80     |
| Gradient Boosting         | 0.83     | 0.83     |
| XGBoost                   | 0.84     | 0.84     |
| Support Vector Classifier | 0.82     | 0.82     |



 🏆 Best Performing Model: **Random Forest Classifier**

📋 Classification Report:


              precision    recall  f1-score   support

           0       0.82      0.86      0.84      7010
           1       0.85      0.81      0.83      7009

    accuracy                           0.84     14019
   macro avg       0.84      0.84      0.84     14019
weighted avg       0.84      0.84      0.84     14019




 🌐 Deployment:

* Built a **Streamlit** app for user-friendly prediction
* UI allows manual input of customer features (LIMIT\_BAL, PAY\_X, BILL\_AMT\_X, etc.)
* Model predicts whether the customer is likely to **default** or **not default**



📦 File Structure:


ML Project/
│
├── Data/
│   ├── rawdata.csv
│   ├── cleandata.csv
│   └── x.csv, y.csv
│
├── Models/
│   └── model.pkl
│
├── app.py                  # Streamlit app
├── datacleaning.py/ipynb
├── modelbuilding.py/ipynb
├── eda.ipynb
├── preprocess.py
└── venv/


 ✅ Tools & Libraries:

* **Python**, **Pandas**, **NumPy**
* **Matplotlib**, **Seaborn** for EDA
* **Scikit-learn** for ML models
* **XGBoost**
* **Streamlit** for deployment
* **VS Code** for development


 📈 Future Improvements:

* Add hyperparameter tuning (e.g., GridSearchCV)
* Use SMOTE to handle class imbalance (if needed)
* Add SHAP/LIME for explainability
* Deploy on **Heroku** or **Streamlit Cloud**



 🧠 Conclusion:

The Random Forest model achieved a strong **accuracy of 84%**, proving effective for identifying customers likely to default. The Streamlit app makes it usable by non-technical stakeholders.



