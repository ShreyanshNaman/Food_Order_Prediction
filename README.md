# Food_Order_Prediction
# 🍔 Online Food Ordering Analysis & Prediction

Predict whether a customer will order food online again based on their demographic and behavioral data using a machine learning model.  
This project performs **data analysis**, **visualization**, and **prediction** using a `RandomForestClassifier`.

---

## 📁 Project Overview

This project analyzes key customer features like:
- Age, Gender, Marital Status
- Occupation & Education Level
- Monthly Income & Family Size
- Feedback on previous order

Based on this, it predicts whether the customer will **order again** or not.

---

## 📊 Dataset Information

**Filename:** `onlinefoods.csv`

**Columns Used:**
- `Age`
- `Gender`
- `Marital Status`
- `Occupation`
- `Educational Qualifications`
- `Monthly Income`
- `Family size`
- `Pin code`
- `Feedback`
- `Output` (target variable)

---

## 🛠️ Technologies & Libraries

| Tool          | Purpose                     |
|---------------|-----------------------------|
| Python 🐍     | Programming Language         |
| Pandas        | Data Manipulation            |
| NumPy         | Numerical Computations       |
| Seaborn       | Statistical Plots            |
| Matplotlib    | Data Visualization           |
| Plotly        | Interactive Charts           |
| Scikit-learn  | Machine Learning             |

---

## 📈 Key Visualizations

- Age vs Online Order Decision (Histogram)
- Family Size vs Order Frequency
- Gender Split of Repeat Orders (Pie Chart)
- Marital Status Distribution
- Income Group Ordering Behavior

These help understand customer preferences and behavior visually.

---

## 🤖 Machine Learning Model

We use a **Random Forest Classifier** from `scikit-learn`:

- Features: 9 input features after label encoding
- Output: Binary classification — "Yes" or "No"
- Accuracy is calculated on a test split (90/10)
- Interactive input mode via terminal

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/online-food-prediction.git
cd online-food-prediction

