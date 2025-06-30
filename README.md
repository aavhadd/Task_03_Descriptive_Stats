# Task_03_Descriptive_Stats
 
This repository contains my work for Syracuse University OPT Research Task 3. The objective was to analyze datasets related to advertising spend and social media activity on Facebook and Twitter during the 2024 U.S. Presidential Election, using:
 
- Pure Python (no third-party libraries)  
- Pandas  
- Polars  
 
A bonus section includes exploratory visualizations designed to support presentation to senior stakeholders.
 
---
 
## 📂 Project Structure
 
```
Task_03_Descriptive_Stats/
│
├── pure_python_stats.py
├── pandas_stats.py
├── polars_stats.py
├── visualization.ipynb
├── .gitignore
└── README.md
```
 
---
 
## How to Run the Scripts
 
All three main scripts are **parameterized**. You can run them on any of the three datasets by specifying:
 
1. The CSV filename  
2. The grouping columns for that dataset
 
Below you'll find **step-by-step** instructions **for each dataset**, **for each approach**.
 
---
 
## 1. Dataset: Facebook Ads
 
**File name**:  
```
2024_fb_ads_president_scored_anon.csv
```
 
**Recommended grouping columns**:  
```
"Page Id" "Ad Id"
```
 
These columns group by:
 
- The Facebook page running the ad
- The specific ad creative ID
 
---
 
### a) Run with Pure Python
 
```
python pure_python_stats.py 2024_fb_ads_president_scored_anon.csv "Page Id" "Ad Id"
```
 
---
 
### b) Run with Pandas
 
```
python pandas_stats.py 2024_fb_ads_president_scored_anon.csv "Page Id" "Ad Id"
```
 
---
 
### c) Run with Polars
 
```
python polars_stats.py 2024_fb_ads_president_scored_anon.csv "Page Id" "Ad Id"
```
 
---
 
## 2. Dataset: Facebook Posts
 
**File name**:  
```
2024_fb_posts_president_scored_anon.csv
```
 
**Recommended grouping columns**:  
```
"Facebook_Id" "post_id"
```
 
---
 
### a) Pure Python
 
```
python pure_python_stats.py 2024_fb_posts_president_scored_anon.csv "Facebook_Id" "post_id"
```
 
---
 
### b) Pandas
 
```
python pandas_stats.py 2024_fb_posts_president_scored_anon.csv "Facebook_Id" "post_id"
```
 
---
 
### c) Polars
 
```
python polars_stats.py 2024_fb_posts_president_scored_anon.csv "Facebook_Id" "post_id"
```
 
---
 
## 3. Dataset: Twitter Posts
 
**File name**:  
```
2024_tw_posts_president_scored_anon.csv
```
 
**Recommended grouping column**:  
```
"id"
```
 
---
 
### a) Pure Python
 
```
python pure_python_stats.py 2024_tw_posts_president_scored_anon.csv "id"
```
 
---
 
### b) Pandas
 
```
python pandas_stats.py 2024_tw_posts_president_scored_anon.csv "id"
```
 
---
 
### c) Polars
 
```
python polars_stats.py 2024_tw_posts_president_scored_anon.csv "id"
```
 
---
 
 
The notebook offers **clear, polished, and interactive visualizations** to support a professional research presentation.
 
---
 
### 📌 How to Use
 
1️⃣ Open Jupyter Notebook  
2️⃣ Launch `visualization.ipynb`  
3️⃣ Run all cells top-to-bottom
 
All plots render **inline** for easy review and export.
 
---
 
### 📊 Included Visualizations (Dataset-specific)
 
#### ⭐ Facebook Ads
- **Spend Distribution**: Histograms with *log scale* to reveal typical spend levels despite outliers.
- **Impressions Distribution**: Interactive plots with *log scale* to highlight the long tail of high-reach ads.
- **Audience Size**: Visualization of estimated audience targeting range.
- **Top Advertisers**: Bar charts of the top 10 Pages by ad count, with options for truncating or ranking IDs for readability.
 
#### ⭐ Facebook Posts
- **Total Interactions Distribution**: Histograms with *log scale* to display right-skewed engagement.
- **Boxplots & Violin Plots**: Show spread, median, and outliers for interactions across posts.
 
#### ⭐ Twitter Posts
- **Engagement Metrics**: Boxplots for retweets, likes, replies, and quotes—highlighting low median values but high outliers.
- **Distribution Plots**: Histograms to explore engagement metric spread with log scaling.
 
---
 
 
---
 
#### ⭐ Combined Visuals Include:
- **Boxplots (Static & Interactive)**: Compare medians, IQRs, and outliers across platforms and metrics with log scale.
- **Violin Plots**: Show distribution shapes for each platform's key metrics.
- **Swarm / Strip Plots**: Visualize every single ad/post/tweet, showing density and outliers.
- **Count Plots**: Compare number of observations per metric/platform.
- **Interactive Histograms**: Faceted by metric to compare value distributions across datasets.
- **Density Heatmaps**: Reveal where metrics cluster across platforms.
- **Pivot Heatmaps**: Summarize median metric values by platform and metric.
 
---
 
### 📌 Purpose and Storytelling
 
These visualizations are designed to:
 
- Reveal *distributional differences* between Facebook Ads, Facebook Posts, and Twitter Posts.
- Handle **extreme skew** with **log scales** for more meaningful insights.
- Enable **cross-platform storytelling** for senior stakeholders, clearly showing:
  - How Facebook Ads have low typical spend with a few very large campaigns.
  - How Facebook Posts interactions are variable but less extreme.
  - How Twitter engagement is generally lower but contains significant outliers.
 
---
 
 
---
 
### ⚡️ Takeaways
 
- **Professional-grade visuals** with both static and interactive options.
- **Log scaling** to handle real-world skew.
- **Clean, labeled charts** suitable for sharing with non-technical audiences.
- **Insights ready for presentation** or written reporting.
 
---
