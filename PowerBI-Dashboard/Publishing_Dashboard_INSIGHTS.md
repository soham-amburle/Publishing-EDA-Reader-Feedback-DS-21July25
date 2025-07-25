# Insights: Publishing Feedback Dashboard

## Objective

The **Publishing Feedback Dashboard** provides a comprehensive analysis of reader satisfaction, engagement, and purchase behavior across various countries and publication types. It is designed to empower publishing teams with a quick, interactive way to gain insights into:

- **Engagement by Country**: Identify which countries have the highest feedback volumes.
- **Publication Performance**: Compare feedback across different publications.
- **Reader Satisfaction Trends**: Track how reader satisfaction evolves over time.
- **Revenue & Purchase Behavior**: Analyze purchase trends, segmented by quarter and by reader.

## Key Insights

1. **Country Engagement**:
   - The **Top 10 Countries** bar chart highlights the countries where readers are most engaged, helping editorial and marketing teams target high-impact regions.

2. **Publication Performance**:
   - The **Publication Share** pie chart visually represents the distribution of feedback across different publication types, allowing teams to identify which titles resonate most with readers.

3. **Satisfaction & Trends**:
   - The **Satisfaction Trend** line chart provides a clear view of the evolving average satisfaction scores, which can guide content improvements and decision-making.
   - The **Quarterly Purchase Trend** bar chart helps spot seasonal revenue patterns and offers insights into the financial impact of content.

4. **Top Readers**:
   - The **Top Readers** section allows teams to segment readers by satisfaction score and purchase value, identifying high-value customers and areas for improvement.

5. **Interactive Data**:
   - The **Matrix Table** offers a detailed breakdown of feedback and purchase data by country and publication, providing granular insights into performance.
   - **Slicers** allow users to filter data by country, date range, and publication type for customized views.

## Key Metrics

- **Total Feedback Count**: Tracks the number of feedback entries across all countries and publications.
- **Average Satisfaction**: Measures the average satisfaction score (1-10) based on user feedback.
- **Total Revenue**: Calculates the sum of all purchases, displayed in EUR.
- **Country Count**: The number of countries from which feedback has been received.

## Tools & Technologies Used

- **Power BI Desktop**: Main tool used to build the interactive dashboard.
- **DAX**: Used to create calculated fields and trend lines for deeper analysis.
- **GitHub**: Version control for project management and collaboration.
- **Python**: Employed for exploratory data analysis (EDA) in a separate script.

## Data Overview

This dashboard uses a synthetic dataset of 1,000 entries, with the following fields:

- `reader_name`
- `country`
- `publication`
- `satisfaction_score` (1–10)
- `content_quality`
- `service_rating`
- `purchase_value` (in EUR)
- `feedback_length`
- `submission_date`

## Use Cases

- **Editorial Planning**: Guide decisions on which content to focus on based on reader satisfaction and engagement.
- **Market Targeting**: Identify countries or regions that require targeted marketing efforts.
- **Reader Satisfaction Tracking**: Continuously track and improve reader satisfaction over time.
- **Revenue-Based Segmentation**: Analyze revenue trends and segment readers by purchase behavior.
