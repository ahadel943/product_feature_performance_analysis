# **Product Feature Performance Analysis**

## **Project Overview**
This project analyzes the performance of six newly launched product features in an e-commerce platform. The analysis focuses on understanding how each feature influences user behavior, engagement, adoption, conversion, revenue generation, and user retention. Using large-scale datasets (**6.6 GB+**) and Python for data analysis, the project provides actionable business insights to help stakeholders evaluate feature success and make data-driven product decisions.

## **Business Problem**
Over the past year, the company launched six new product features across its e-commerce platform. However, not all features contribute equally to business goals. Product managers need to understand which features successfully drive user engagement, conversions, repeat purchases, and revenue, and which ones require further improvements.

The company seeks to answer several critical business questions:
- **Which features achieve the highest adoption rates ?**
- **Which features drive meaningful user engagement ?**
- **How do product features impact conversion and revenue ?**
- **Are premium users interacting differently with product features compared to non-premium users ?**
- **Which features perform better for new users versus returning users ?**
- **How do feature performance and adoption vary across countries and over time ?**
- **Which features encourage repeat purchases and long-term user activity ?**

By answering these questions, the company can make informed product decisions, prioritize feature investments, and improve the overall user experience.

## **Project Goal**
The goal of this project is to evaluate the performance of product features by analyzing user adoption, engagement, conversion, and revenue impact. Through large-scale behavioral data, the project aims to identify which features create the most business value, understand how different user segments interact with each feature, and uncover opportunities to improve product performance, user retention, and overall customer experience.

Additionally, the project demonstrates practical techniques for analyzing large datasets efficiently using Python, with a focus on memory optimization, selective data loading, and scalable analytical workflows.

## **Executive Summary**
**NO SUMMARY YET**

## **Dataset Description**
| Table | Description | Rows |
|--------|-------------|------:|
| **users** | User profile information including signup date, subscription status, country, customer type, and premium membership details. | 300,000 |
| **products** | Product catalog containing product information such as category, price, and brand. | 15,000 |
| **features** | Product features available within the platform, including launch dates and feature metadata. | 6 |
| **sessions** | User browsing sessions capturing session duration, device type, pages viewed, and conversion status. | 6,000,000 |
| **feature_events** | Detailed event-level interactions between users and product features throughout each session. | 12,000,000 |
| **orders** | Customer orders including purchase date, payment method, order status, and total order value. | 420,000 |
| **order_items** | Individual products purchased within each order along with quantity and pricing information. | 1,500,000 |
| **feature_adoptions** | Records indicating when users first adopted or started using a specific feature. | 1,200,000 |
| **subscriptions** | Premium subscription history including subscription plans, start dates, and renewal information. | 200,000 |
| **user_daily_activity** | Daily user activity logs used to analyze engagement, active users, retention, and behavioral trends. | 15,000,000 |
> **Note:** This project uses a synthetic dataset (**~6.6 GB**) designed to simulate a real-world product analytics environment. The data follows realistic business rules, user behavior patterns, and intentional distribution imbalances to support practical feature performance analysis.

## **Schema Design**
![erd](./assets/erd.png)

## **Data Preparation**
### **Data Quality Assessment**
The first step is to evaluate the quality of the users dataset before conducting any exploratory analysis.

The following checks will be performed:
- Exact duplicate records
- Missing values
- Primary key uniqueness
- Domain validation
- Business rule validation

### **Issues Found**
| Table          | Result                                    |
| -------------- | ----------------------------------------- |
| `users` | No duplicate records, missing values, primary key violations, or data type inconsistencies were identified. |

### **Data Cleaning and Issue Handling**
**NO ACTIONS REQUIRED SO FAR**

## **Exploratory Data Analysis (EDA)**
### **Users Distribution by Country**
![users_distribution_by_country](./charts/1.users_distribution_by_country.png)
#### **Key Findings**
- **Egypt** has the largest user base, accounting for **31.92%** of all registered users.
- **Saudi Arabia** ranks second with **23.03%**, followed by the **UAE** at **18.04%**.
- **Bahrain** represents the smallest user segment, contributing only **3.01%** of the total user population.
- The user base is unevenly distributed across countries, with **Egypt** and **Saudi Arabia** together accounting for **more than half** of all registered users.
#### **Business Interpretation**
The user acquisition strategy appears to be concentrated in a limited number of markets, particularly **Egypt** and **Saudi Arabia**, where the majority of users are located. This geographic imbalance should be considered when interpreting downstream metrics such as feature adoption, engagement, conversion rate, and revenue. Cross-country comparisons should rely on normalized metrics (e.g., percentages or rates) rather than absolute user counts to avoid misleading conclusions driven by differences in market size.
### **Users Distribution by City**
![users_distribution_by_city](./charts/2.users_distribution_by_city.png)
#### **Key Findings**
- User distribution across cities within each country is highly balanced, with only minor differences in user counts between cities.
- **Egypt**, **Saudi Arabia**, **UAE**, and **Kuwait** all exhibit a nearly uniform distribution of users across their major cities, indicating no single city dominates the user base.
- **Bahrain** has the **smallest** overall user base, while **Egypt** has the **largest**. This pattern is consistent with the country-level distribution observed previously.
#### **Business Interpretation**
The user base appears to have been intentionally distributed evenly across cities within each country rather than concentrated in a few major metropolitan areas. This balanced geographic distribution reduces location bias in subsequent analyses, allowing comparisons between cities without one city disproportionately influencing the results. At the same time, the overall differences in user volume between countries remain evident, with Egypt contributing the largest share of users and Bahrain the smallest, reflecting the country-level distribution rather than differences in city-level concentration.
### **Users Distribution by Age Group**
![users_distribution_by_age_group](./charts/3.users_distribution_by_age_group.png)
#### **Key Findings**
- The **25–34** age group represents the largest user segment, accounting for **41.14%** of the total user base.
- Users aged **35–44** represent the second-largest segment at **23.95%**, followed by the **18–24** group at **18.00%**.
- **Older users** are underrepresented in the dataset, with the **55+** age group contributing only **5.95%** of total users.
- **The age distribution is not uniform, indicating a clear concentration of users within the 25–44 age range**.
#### **Business Interpretation**
The dataset is heavily concentrated around users aged **25–44**, suggesting that the platform primarily serves a working-age audience. Since this segment represents nearly two-thirds of all registered users, overall platform metrics such as feature adoption, conversion, and engagement are likely to be driven primarily by these age groups. Consequently, age-based analyses should account for this imbalance, as results for older age groups may be less representative due to their relatively small sample sizes.
### **Users Distribution by Customer Type**
![users_distribution_by_customer_type](./charts/4.users_distribution_by_customer_type.png)
#### **Key Findings**
- **New** customers represent **61.00%** of the user base, while **Returning** customers account for **39.00%**.
- The customer type distribution is imbalanced, with new customers forming the majority of registered users.
- The difference between the two segments is substantial, indicating that the dataset contains considerably more new users than returning users.
#### **Business Interpretation**
The dataset contains a larger proportion of users labeled as **New** compared to **Returning** customers. At this stage, this observation should be treated as a characteristic of the dataset rather than evidence of actual customer acquisition behavior. Since the customer type is a predefined categorical attribute, additional analysis is required to determine whether this distribution reflects genuine business performance or simply the dataset's labeling and generation logic. This imbalance should, however, be considered when comparing metrics between the two customer segments.









