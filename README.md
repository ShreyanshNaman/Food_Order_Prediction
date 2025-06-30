# Food_Order_Prediction
# 🍔 Online Food Ordering Analysis and Prediction

This project uses customer demographic and behavioral data to analyze online food ordering trends and predict whether a customer will place an order again.

## 📊 Dataset
The dataset contains customer information such as:
- Age, Gender, Marital Status
- Occupation, Educational Qualifications, Monthly Income
- Family size, Pin code, Feedback on last order
- Output (whether they ordered again)

Source: `onlinefoods.csv`

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Seaborn, Matplotlib, Plotly
- Scikit-learn (RandomForestClassifier)

## 📈 Visualizations
Key visualizations include:
- Age vs. Order Decision
- Family Size vs. Order Decision
- Gender and Marital Status Pie Charts
- Income Group Preferences

## 🔍 ML Model
A `RandomForestClassifier` is trained on the transformed dataset. Accuracy is displayed based on test data. The script allows you to input new customer data and predict their likelihood of reordering.

## 🚀 Running the Project

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/online-food-prediction.git
   cd online-food-prediction
