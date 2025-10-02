![Power BI](https://img.shields.io/badge/Tool-Power%20BI-yellow) ![Python](https://img.shields.io/badge/Language-Python-blue)

**Date:** 21 July, 2025  
# Publishing EDA (Exploratory Data Analysis) – Analyzing Reader Feedback

This project explores and analyzes reader feedback data collected by a publishing firm. The goal is to uncover actionable insights that help the editorial and business teams understand how readers perceive various publications, including magazines, journals, and e-books, based on satisfaction scores, content quality, and purchasing behavior.

---

## Dataset Summary

The analysis is based on a structured dataset that contains individual reader responses. Each row represents a feedback entry, including metrics such as satisfaction levels, spending amounts, and qualitative content engagement.

**Key columns include:**

| Column | Description |
|--------|-------------|
| `reader_name` | Reader's name or unique identifier |
| `country` | Country of feedback submission |
| `publication` | Name of the magazine, journal, or e-book |
| `satisfaction_score` | Overall satisfaction (scale of 1–10) |
| `content_quality` | Rating for content quality (scale of 1–10) |
| `service_rating` | Rating of service experience (scale of 1–10) |
| `purchase_value` | Amount spent by the reader |
| `feedback_length` | Length of the written feedback |
| `submission_date` | Date of feedback submission |

---

## What Was Done

The analysis covered a wide range of exploratory techniques using Python, suxh as:

- Loading and previewing the dataset to understand its structure and shape
- Listing and reviewing column headers
- Aggregating feedback volume by country
- Identifying the top 10 countries with the most feedback using bar charts
- Sorting readers by high satisfaction scores and purchase values
- Filtering data for specific regions like India
- Highlighting top-rated and high-spending readers
- Breaking down satisfaction, content quality, and service rating scores
- Visualizing top 5 readers in terms of satisfaction and purchase value
- Performing conditional aggregations using NumPy
- Exploring patterns by country and publication type

---

## Key Visuals

The following charts were generated:

- Bar chart showing the top 10 countries based on feedback volume
- Bar chart of top 5 readers by satisfaction score
- Bar chart of top 5 readers by purchase value

These visualizations helped surface regional trends and highlight which readers and regions are the most engaged and valuable.

---

## Tools and Libraries Used

- Python 3.x
- Pandas for data handling
- NumPy for numerical operations
- Matplotlib for plotting
- Seaborn was imported but not utilized in this version of the script
---
