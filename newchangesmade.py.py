# -*- coding: utf-8 -*-
"""projectmain.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m3rcK60FpyqkA1G36LIm-QmME4ugH5Eg
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

# Load dataset
data = pd.read_csv("onlinefoods.csv")

# Map categorical data to numeric for easier processing
data["Gender"] = data["Gender"].map({"Male": 1, "Female": 0})
data["Occupation"] = data["Occupation"].map({"Student": 1, "Employee": 2, "Self Employed": 3, "Housewife": 4})

# Convert Monthly Income to numeric values
income_mapping = {
    "No Income": 0,
    "Below Rs.10000": 10000,
    "10001 to 25000": 25000,
    "25001 to 50000": 50000,
    "More than 50000": 70000
}
data["Monthly Income"] = data["Monthly Income"].map(income_mapping)

# Example food items
food_items = ["Pizza", "Burger", "Pasta", "Sushi", "Salad"]
for item in food_items:
    data[item] = np.random.randint(1, 6, size=len(data))  # Simulate ratings (1-5)

# Prepare the features and target
x = np.array(data[["Age", "Gender", "Occupation", "Monthly Income"] + food_items])
y = np.array(data[food_items])  # Target is now the food items' ratings directly

# Split data and train the model
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.10, random_state=42)

# Using MultiOutputClassifier for multi-output prediction
model = RandomForestClassifier()
multi_output_model = MultiOutputClassifier(model)
multi_output_model.fit(xtrain, ytrain)

# Evaluate model
print("Model accuracy:", multi_output_model.score(xtest, ytest))

# User input for prediction
print("Enter Customer Details to Predict Which Food Item They Will Order Again")
age = int(input("Enter the Age of the Customer: "))
gender = int(input("Enter the Gender of the Customer (1 = Male, 0 = Female): "))
occupation = int(input("Occupation of the Customer (Student = 1, Employee = 2, Self Employed = 3, Housewife = 4): "))
income_input = input("Monthly Income (options: No Income, Below Rs.10000, 10001 to 25000, 25001 to 50000, More than 50000): ")
income = income_mapping.get(income_input, 0)  # Default to 0 if input doesn't match

# Collect ratings for each food item
food_reviews = []
for item in food_items:
    rating = int(input(f"Rate {item} (1-5): "))
    food_reviews.append(rating)

# Combine inputs into features array for prediction
features = np.array([[age, gender, occupation, income] + food_reviews])

# Predict which food item the customer is most likely to order again
predicted_ratings = multi_output_model.predict(features)
predicted_food_item = food_items[np.argmax(predicted_ratings[0])]  # Get the food item with the highest predicted rating
print("The customer is most likely to order again:", predicted_food_item)

