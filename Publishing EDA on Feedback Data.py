# 📦 Importing required libraries
import pandas as pd                      # For data manipulation
import numpy as np                       # For numerical operations
from matplotlib import pyplot as plt     # For plotting bar charts
import seaborn as sns                    # For advanced visualization (not used yet)

# 📁 Reading the dataset
feedback = pd.read_csv('publishing_feedback.csv')

# 👀 Previewing the first 5 rows of the dataset
print(feedback.head())

# 🧾 Printing the entire dataset (optional, can be huge)
print(feedback)

# 🏷️ Printing all column names
for col in feedback.columns:
    print(col)

# 📐 Checking the shape of the dataset
print(feedback.shape)

# 📊 Counting number of feedbacks per country
print(feedback['country'].value_counts())

# 📈 Plotting a bar chart of the top 10 countries by feedback count
plt.figure(figsize=(7, 7))
plt.bar(
    list(feedback['country'].value_counts()[0:10].keys()),
    list(feedback['country'].value_counts()[0:10]),
    color=['skyblue']
)
plt.show()

# 💸 Creating a DataFrame with readers and their satisfaction scores
reader_satisfaction = feedback[['reader_name', 'satisfaction_score']]
print(reader_satisfaction.head())

# 💰 Sorting readers by satisfaction
reader_satisfaction = reader_satisfaction.sort_values(by=['satisfaction_score'], ascending=False)
print(reader_satisfaction.head())

# 🧮 Filtering highly satisfied readers (score > 9)
top_rated = reader_satisfaction[reader_satisfaction['satisfaction_score'] > 9]
print(top_rated.head())

# 📊 Bar chart of top 5 most satisfied readers
plt.figure(figsize=(8, 5))
plt.bar(
    list(reader_satisfaction['reader_name'])[0:5],
    list(reader_satisfaction['satisfaction_score'])[0:5],
    color=["magenta", "green", "red", "blue", "orange"]
)
plt.show()

# 🧾 Displaying top 3 satisfied readers
print(reader_satisfaction[0:3])

# 🔤 Printing all reader names
print(feedback[['reader_name']])

# ✅ Boolean Series: Is the country "India"?
print(feedback['country'] == 'India')

# 🇮🇳 Creating DataFrame of Indian readers
India = feedback[feedback['country'] == 'India']
print(India.head(10))

# 📏 Tallest feedback scores in India
print(India.sort_values(by=['satisfaction_score'], ascending=False).head())

# 🔁 Printing all column names again
for col in feedback.columns:
    print(col)

# 🔤 Iterating over characters in a string
for char in 'India and USA':
    print(char)

# 🧍 Looping through a list of publications
for pub in ['Magazine A', 'Journal B', 'E-book C']:
    print(pub)

# 🔁 Looping through dictionary keys
for dict in {'a': 1, 'b': 2}:
    print(dict)

# ⚖️ Heaviest feedback weight (example metric)
print(India.sort_values(by=['feedback_length'], ascending=False).head())

# 🇮🇳 Top 5 richest feedback (if wage-like column exists e.g., purchase_value)
print(
    India[['reader_name', 'purchase_value']]
    .sort_values(by=['purchase_value'], ascending=False)
    .head()
)

# 🧮 Checking if a specific reader gave feedback from a certain country
print(
    np.sum(
        (feedback['country'] == 'USA') &
        (feedback['reader_name'] == 'John Doe')
    )
)

# 🧮 USA readers who are NOT John Doe
print(
    np.sum(
        (feedback['country'] == 'USA') &
        (feedback['reader_name'] != 'John Doe')
    )
)

# 🧮 John Doe listed outside USA
print(
    np.sum(
        (feedback['country'] != 'USA') &
        (feedback['reader_name'] == 'John Doe')
    )
)

# 🌎 Number of unique countries
print(len(feedback['country'].unique()))

# 🔄 Convert top 5 India feedbacks to NumPy array
print(
    India[['reader_name', 'purchase_value']]
    .sort_values(by=['purchase_value'], ascending=False)
    .head()
    .to_numpy()
)

# 🔄 Same with `.values`
print(
    India[['reader_name', 'purchase_value']]
    .sort_values(by=['purchase_value'], ascending=False)
    .head()
    .values
)

# 📏 Sorting India readers by feedback length
print(
    India.sort_values(by=['feedback_length'], ascending=False).head()
)

# 🎯 Creating DataFrame with content_quality score
reader_quality = feedback[['reader_name', 'content_quality']]
print(reader_quality.sort_values(by=['content_quality'], ascending=False).head())

# 🛡️ Creating DataFrame with service_rating
reader_service = feedback[['reader_name', 'service_rating', 'country', 'publication']]

# 🛡️ Top 5 by service rating
print(reader_service.sort_values(by=['service_rating'], ascending=False).head())

# ⚪ Creating DataFrame for a specific publication
pub_A = feedback[feedback['publication'] == 'Magazine A']

# 💸 Top 5 readers by purchase value in Magazine A
print(pub_A.sort_values(by=['purchase_value'], ascending=False).head())

# 🔫 Top 5 by content quality in Magazine A
print(pub_A.sort_values(by=['content_quality'], ascending=False).head())

# 🛡️ Top 5 by service rating in Magazine A
print(pub_A.sort_values(by=['service_rating'], ascending=False).head())

# 🌍 Most common countries in Magazine A readers
print(pub_A['country'].value_counts()[0:2])
