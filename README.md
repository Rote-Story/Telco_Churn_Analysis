# Telco Customer Churn Analysis

For a high-level overview of the project and key findings, see [EXECUTIVE_SUMMARY.md](./EXECUTIVE_SUMMARY.md)

## Project Overview

This project explores customer churn for a telecommunications company (Telco) using demographic, account, and service usage data. The goal is to identify key factors influencing churn and provide actionable insights to improve customer retention.

## Motivation

Customer churn is a critical metric in the telecom industry, as acquiring new customers is significantly more expensive than retaining existing ones. By understanding which factors drive churn, businesses can implement targeted strategies to increase loyalty and revenue.

## Dataset

The Telco dataset contains information on customer demographics, subscription services, contract details, billing, and usage patterns. Key feature categories include:

- **Demographics:** gender, age, partner status, dependents

- **Account & Contract:** contract type, tenure, payment method, paperless billing

- **Service Usage:** phone, internet, streaming, tech support, device protection

- **Financials:** monthly charges, total charges, charges per service

## Data

The dataset used in this project is the **Telco Customer Churn Dataset**, originally published by IBM and available on [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn). It contains customer demographics, account information, and service usage details for a telecommunications company. The target variable is `Churn`, which indicates whether a customer has discontinued the service.

## Analysis Approach

- Exploratory Data Analysis (EDA) to uncover patterns across demographics, services, contracts, and spending.
- Predictive modeling using logistic regression and tree-based models to identify high-risk customers.
- Threshold optimization to improve retention campaign efficiency.

## Key Insights

- Short-tenure and month-to-month contract customers are most at risk.
- Billing preferences and high monthly charges influence churn risk.
- Engagement through multi-service usage and support services correlates with higher retention.

## Business Impact

Implementing targeted retention strategies could reduce churn by 5–10% in high-risk segments and increase customer lifetime value. Detailed recommendations are provided in the [Executive Summary](EXECUTIVE_SUMMARY.md) and Notebook 05.


## How to Run

This project is organized into four Jupyter notebooks that cover the full analysis pipeline:

- **01_dataset_overview.ipynb** - Overview of the raw dataset

- **02_data_preparation.ipynb** - Cleaning and preprocessing

- **03_exploratory_data_analysis.ipynb** - Visual exploration and churn patterns

- **04_modeling.ipynb** - Modeling and 

- **05_insights_and_recommendations.ipynb** - Final insights and conclusions

Follow the steps below to set up the environment and run the notebooks.

1. **Clone the Repository**
    ```
    git clone https://github.com/Rote-Story/Telco_Churn_Analysis.git
    cd Telco_Churn_Analysis
    ```

2. **Create and Activate a Virtual Environment (Recommended)**

    **Using `conda`:**
    ```
    conda create -n myenv python=3.11
    conda activate myenv
    ```
    **Using `venv`:**
    ```
    python3 -m venv venv
    source venv/bin/activate    # macOs/Linux
    venv\Scripts\activate       # Windows
    ```
3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Launch Jupyter Notebook**
    ```
    jupyter notebook
    ```
    Open any notebook in the sequence (`01_...` through `04_...`) in your browser.
    > The notebook will download the required datasets automatically when run. 

## Future Work

- Test retention interventions and simulate potential impact on revenue.

- Extend the analysis to include customer feedback or support ticket data.

## Author

Thomas Ricketts 

Email: tbrricketts@gmail.com \
LinkedIn: https://www.linkedin.com/in/thomas-ricketts7/ \
GitHub: https://github.com/Rote-Story 

