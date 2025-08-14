
#######################################################################################################################################################
# 
# Name:Snehasish Kaibartta
# SID:740100109
# Exam Date:14th August 2025
# Module:BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/bemm458-ref-def-2425-practice-test-EXsk1002.git
#
########################################################################################################################################################
# Instruction 1. Carefully read each question before attempting the solution. Complete all tasks in the script provided.

# Instruction 2. Only ethical and minimal use of AI tools is allowed. This includes help in syntax, documentation look-up, or debugging only.
#                You must not use AI to generate the core logic or full solutions.
#                Clearly indicate where and how AI support was used.

# Instruction 3. Paste the output of each code section directly beneath it as a comment (e.g., # OUTPUT: (34, 90))

# Instruction 4. Add sufficient code comments to demonstrate your understanding of each solution.

# Instruction 5. Save your file, commit it to GitHub, and upload to ELE. GitHub commit must be done before the end of the exam session.

########################################################################################################################################################
# Question 1 - List Comprehension and String Manipulation
# You are analysing customer reviews collected from a post-service survey.
# Your SID will determine the two allocated keywords from the dictionary below. Use the **second** and **second-to-last** digits of your SID.
# For each selected keyword, identify all positions (start and end) where the word occurs in the customer_review string.
# Store each occurrence as a tuple in a list called `location_list`.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

# Dictionary of keywords
feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}
# Write your code here to populate location_list
location_list = []

# SID digits
sid = "740100109" #my sid
second_digit = int(sid[1])
print(second_digit) # OUTPUT: 4
second_last_digit = int(sid[-2])
print(second_last_digit) # OUTPUT: 0

# Select keywords based on second and second-to-last digits of SID for the varibale selected_keywords
selected_keywords = [feedback_keywords[second_digit], feedback_keywords[second_last_digit]]

# Find all (start, end) positions for each keyword in the review
location_list = [
    (i, i + len(keyword)) #  (start, end) tuple
    for keyword in selected_keywords # iterate through each keyword
    for i in range(len(customer_review)) # iterate through each character in the customer_review
    if customer_review.startswith(keyword, i) # check if the keyword starts at index i
]

# OUTPUT: print(location_list)
print(location_list)

########################################################################################################################################################
# Question 2 - Metrics Function for Business Intelligence
# You work in a startup focused on digital health. Your manager wants reusable functions to calculate key performance metrics:
# Gross Profit Margin, Churn Rate, Customer Lifetime Value (CLV), and Cost Per Acquisition (CPA).
# Use the **first** and **last** digits of your student ID as sample numerical values to test your function outputs.

# Insert first digit of SID here:7
# Insert last digit of SID here:9

# function for Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100
def gross_profit_margin(revenue, cost_of_goods_sold):
    return (revenue - cost_of_goods_sold) / revenue * 100

# function for Churn Rate (%) = (Customers Lost / Customers at Start) * 100
def customer_retention_rate(customers_at_start, customers_at_end):
    return (customers_at_end / customers_at_start) * 100

# function for Customer Lifetime Value = Average Purchase Value × Purchase Frequency × Customer Lifespan
def customer_lifetime_value(avg_purchase_value, purchase_frequency, customer_lifespan):
    return avg_purchase_value * purchase_frequency * customer_lifespan

# function for CPA = Marketing Cost / Number of Acquisitions
def cost_per_acquisition(marketing_cost, number_of_acquisitions):
    return marketing_cost / number_of_acquisitions

# Testing functions here
first_digit = 7  
last_digit = 9   

print("Gross Profit Margin:", gross_profit_margin(100*first_digit, 60*last_digit))  
print("Customer Retention Rate:", customer_retention_rate(100*first_digit, 80*last_digit))
print("Customer Lifetime Value:", customer_lifetime_value(50*first_digit, 2*last_digit, 5))
print("Cost Per Acquisition:", cost_per_acquisition(1000*first_digit, 10*last_digit))
# OUTPUT: (22.857142857142858)
# OUTPUT: (102.85714285714285)
# OUTPUT: (31500)
# OUTPUT: (77.77777777777777)

########################################################################################################################################################
# Question 3 - Linear Regression for Pricing Strategy
# A bakery is studying how price affects cupcake demand. Below is a table of past pricing decisions and customer responses.
# Using linear regression:
# 1. Estimate the best price that maximises demand.
# 2. Predict demand if the bakery sets price at £25.

"""
Price (£)    Demand (Units)
---------------------------
8            200
10           180
12           160
14           140
16           125
18           110
20           90
22           75
24           65
26           50
"""

# Write your linear regression solution here
import numpy as np
from sklearn.linear_model import LinearRegression
# Data preparation
prices = np.array([8, 10, 12, 14, 16, 18, 20, 22, 24, 26]).reshape(-1, 1)
demands = np.array([200, 180, 160, 140, 125, 110, 90, 75, 65, 50])
# Create and fit the model
model = LinearRegression()
model.fit(prices, demands)
# Predict the best price that maximises demand
best_price = prices[np.argmax(demands)]
print("Best Price to Maximise Demand: £", best_price[0])
# Predict demand at a price of £25
predicted_demand = model.predict(np.array([[25]]))
print("Predicted Demand at £25: ", predicted_demand[0])
# OUTPUT: Best Price to Maximise Demand: £ 8.0
# OUTPUT: Predicted Demand at £25:  52.9


########################################################################################################################################################
# Question 4 - Debugging and Chart Creation
# The following code is intended to generate 100 random integers between 1 and your SID, and plot them as a scatter plot.
# However, the code contains bugs and lacks contextual annotations. Correct the code and add appropriate comments and output.

import random
import matplotlib.pyplot as plt

# Accept student ID as input
sid_input = input("Enter your SID: ")
# Convert the input string to an integer
sid_value = int(sid_input)

# Generate 100 random values
random_values = [random.randint(1, sid_value) for _ in range(100)]

# Plotting as scatter plot
#create a scatter plot of the random values
plt.figure(figsize=(10,5))
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values')
# Add title and labels
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
#Add legend and grid for better readability
plt.legend()
plt.grid(True)
# Show the plot or Display the plot
plt.show()

########################################################################################################################################################
