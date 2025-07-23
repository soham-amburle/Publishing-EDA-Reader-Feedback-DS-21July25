21 July, 2025
# 📊 Publishing EDA (Reader Feedback Dataset)

This project performs an Exploratory Data Analysis (EDA) on large-scale reader feedback collected by a publishing firm. Readers provide reviews and ratings after interacting with magazines, journals, and e-books. The objective is to extract meaningful insights from this data to help the publishing team understand satisfaction levels, content performance, and purchasing trends.

---

## 📁 Dataset Overview

The dataset is assumed to contain the following columns:

| Column Name         | Description                                                   |
|---------------------|---------------------------------------------------------------|
| `reader_name`       | Name or identifier of the reader                              |
| `country`           | Country from which the feedback was submitted                 |
| `publication`       | Publication name (e.g., Magazine A, Journal B)                |
| `satisfaction_score`| Overall satisfaction score (scale: 1–10)                      |
| `content_quality`   | Rating for the quality of content (scale: 1–10)               |
| `service_rating`    | Rating for support or service experience (scale: 1–10)        |
| `purchase_value`    | Amount spent by the reader (in EUR or local currency)         |
| `feedback_length`   | Length of the feedback submitted (in characters or words)     |
| `submission_date`   | Date the feedback was submitted                               |

---

## 🔍 Analysis Performed

This script mirrors the functionality used in a previous FIFA EDA project and strictly reuses the same types of analysis:

- Previewing the dataset and checking dimensions
- Viewing column names
- Counting feedbacks by country
- Bar chart of top 10 countries by feedback volume
- Sorting readers by satisfaction score and purchase value
- Filtering readers by country (e.g., India)
- Displaying top-rated readers
- Exploring satisfaction, content quality, and service rating
- Visualizing top 5 readers using bar plots
- Country-specific and publication-specific breakdowns
- Using NumPy for conditional aggregations

---

## 📈 Visualizations

The script includes:
- Bar chart of top 10 feedback countries
- Bar chart of top 5 highest-rated readers
- Bar chart of top 5 purchase value contributors

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn (imported but not used in this)

---

## ▶️ How to Use

1. Clone the repository.
2. Add your dataset as `publishing_feedback.csv` in the root folder.
3. Run the script `publishing_feedback_eda.py`:
   ```bash
   python publishing_feedback_eda.py
