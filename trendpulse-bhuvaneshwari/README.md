# 📊 TrendPulse — What’s Actually Trending Right Now

TrendPulse is a 4-stage data pipeline project that collects, cleans, analyzes, and visualizes trending stories from Hacker News.

---

##  Project Overview

This project fetches real-time trending stories using the Hacker News API and processes them step-by-step:

```
Task 1 → Fetch JSON data from API  
Task 2 → Clean and structure data  
Task 3 → Analyze using Pandas & NumPy  
Task 4 → Visualize insights using Matplotlib  
```

---

##  Project Structure

```
trendpulse/
├── data/
│   ├── trends_YYYYMMDD.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
├── outputs/
│   ├── chart1_top_stories.png
│   ├── chart2_categories.png
│   ├── chart3_scatter.png
│   └── dashboard.png
│
├── task1_data_collection.py
├── task2_data_cleaning.py
├── task3_analysis.py
├── task4_visualization.py
└── README.md
```

---

##  Features

* Fetches top 500 trending stories from Hacker News API
* Categorizes stories into:

  * Technology
  * World News
  * Sports
  * Science
  * Entertainment
* Cleans messy real-world data (duplicates, nulls, low-quality entries)
* Performs statistical analysis using NumPy
* Creates visual insights using Matplotlib
* Generates a dashboard of trends

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Requests (for API calls)

---

##  How to Run

### 1. Install dependencies

```
pip install pandas numpy matplotlib requests
```

### 2. Run the pipeline

```
python task1_data_collection.py
python task2_data_cleaning.py
python task3_analysis.py
python task4_visualization.py
```

---

##  Output

###  Data Files

* Raw JSON data
* Cleaned CSV dataset
* Analysed dataset with new features

### Visualizations

* Top 10 trending stories
* Stories per category
* Score vs Comments scatter plot
* Combined dashboard

---

##  Learning Outcomes

* Working with APIs and JSON data
* Data cleaning using Pandas
* Numerical analysis with NumPy
* Data visualization with Matplotlib
* Building an end-to-end data pipeline

---

##  Notes

* Data is fetched live from Hacker News API
* Each run generates a new dataset with the current date
* Error handling is implemented for API failures

