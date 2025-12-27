📌 Project Overview

Online food delivery platforms generate large volumes of transactional and operational data.
This project focuses on analyzing online food delivery data to uncover customer behavior, delivery efficiency, restaurant performance, and revenue trends using Python, SQL, and Streamlit.

The goal is to transform raw, noisy data into actionable business insights that can support operational and strategic decision-making.

🎯 Business Objectives

Understand customer ordering patterns

Identify delivery inefficiencies and delays

Evaluate restaurant and cuisine performance

Analyze revenue, profit margins, and cancellations

Provide interactive dashboards for decision-makers

🧾 Dataset Description

Size: 100,000 records, 25+ attributes

Data Types Included:

Customer details (age, gender, city)

Order information (order value, discounts, payment mode)

Restaurant details (restaurant, cuisine, ratings)

Delivery metrics (distance, delivery time, ratings)

Financial metrics (final amount, profit margin)

Nature: Real-world noisy data with missing values and inconsistencies

🛠️ Tech Stack

Programming Language: Python

Libraries: Pandas, NumPy, Matplotlib, Streamlit

Database: SQLite

Visualization: Streamlit Dashboard

IDE: VS Code

Version Control: GitHub

🔄 Project Workflow
1️⃣ Data Loading & Understanding

Loaded raw CSV data

Inspected schema, data types, and missing values

Identified key KPIs and analytical dimensions

2️⃣ Data Cleaning & Preprocessing

Handled missing values using business logic

Corrected invalid values (ratings, negative amounts)

Enforced logical consistency (cancelled orders vs ratings)

Standardized categorical values

3️⃣ Exploratory Data Analysis (EDA)

City-wise and cuisine-wise order distribution

Revenue and order trends

Delivery time and distance relationship

Cancellation patterns and payment preferences

All plots saved to outputs/plots/

4️⃣ Feature Engineering (Analytics-Focused)

Created derived features to enhance business analysis:

Customer age groups

Delivery performance categories

Order value segments

Profit categories

Weekend and peak-hour indicators

Note: Feature engineering was done for analytical segmentation, not for machine learning.

5️⃣ SQL Database Integration

Created a structured SQLite database

Inserted cleaned and engineered data

Executed analytical SQL queries to validate insights

6️⃣ Streamlit Dashboard

Interactive KPIs (orders, revenue, delivery time, cancellations)

Filters by city, cuisine, and order status

Visual insights into customer behavior and operations

Error-handled for empty filter selections

📊 Key Insights

Certain cities and cuisines generate significantly higher revenue

Weekend orders show increased demand

Longer distances generally lead to delivery delays

Late delivery is the primary cancellation reason

Digital payment modes dominate transactions

⚠️ Challenges Faced & Solutions
Challenge	Solution
Missing data	Context-aware imputation
Logical inconsistencies	Rule-based corrections
Dashboard crashes	Empty-data handling
Large dataset	Efficient Pandas operations
📂 Project Structure
Online_Food_Delivery_Data_Analysis/
│
├── data/
│   └── raw/
│       ├── online_food_delivery_raw.csv
│       ├── online_food_delivery_cleaned.csv
│       └── online_food_delivery_final.csv
│
├── scripts/
│   ├── 01_data_loading_understanding.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   └── 04_feature_engineering.py
│
├── sql/
│   ├── food_delivery.db
│   ├── food_delivery_sqlite.py
│   └── run_queries.py
│
├── outputs/
│   └── plots/
│
├── app/
│   └── streamlitapp.py
│
└── README.md

🏁 Conclusion

This project demonstrates an end-to-end data analytics pipeline from raw data ingestion to interactive business dashboards.
It highlights strong skills in data cleaning, EDA, SQL, and dashboarding, aligned with real-world data analyst responsibilities.

🚀 Future Enhancements

Power BI dashboard version

Predictive ML models (delivery delay or cancellation prediction)

Real-time data ingestion

📌 Author

Jai Nivetha
Data Analytics Project

