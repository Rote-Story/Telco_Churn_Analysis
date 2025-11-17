# Telco Customer Churn Analysis
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

### Dataset Organization

- `data/raw/`: Original dataset (`WA_Fn-UseC_-Telco-Customer-Churn.csv`) downloaded from Kaggle.  
- `data/processed/`: Cleaned and preprocessed datasets:
  - `readable_telco_churn_data.csv` — cleaned and human-readable.
  - `encoded_telco_churn_data.csv` — encoded for modeling purposes.

> **Note:** The raw dataset is included to ensure reproducibility. All transformations and preprocessing steps are documented in the Jupyter notebooks.


## Analysis & Approach

The project follows an exploratory data analysis (EDA) approach to uncover patterns and correlations related to churn:

1. Data cleaning and preprocessing

2. Feature exploration across demographics, services, contracts, and spending

3. Identification of churn drivers through correlation analysis and visualizations

4. Synthesis of actionable business insights

## Key Findings

- Month-to-month contracts, short tenure (<24 months), and paperless billing are strongly associated with higher churn.

- Higher monthly charges increase churn risk, particularly for new customers.

- Multi-service customers tend to be more loyal, though streaming services show a slight positive correlation with churn.

- Tech support and online security services are associated with higher retention.

## Business Impact & Recommendations

- Target high-risk segments with loyalty programs or contract incentives.

- Focus retention efforts on first-year customers with onboarding and proactive engagement.

- Enhance internet and tech support experiences, especially for Fiber customers.

- Optimize pricing transparency and flexible service bundles to reduce perceived cost concerns.

- Future opportunity: implement predictive models to proactively flag at-risk customers.

**Expected outcome:** A potential 5–10% reduction in churn among high-risk segments, improved customer lifetime value, and increased overall satisfaction.

## How to Run

This project is organized into four Jupyter notebooks that cover the full analysis pipeline:

- **01_dataset_overview.ipynb** – Overview of the raw dataset

- **02_data_preparation.ipynb** – Cleaning and preprocessing

- **03_exploratory_data_analysis.ipynb** – Visual exploration and churn patterns

- **04_insights_and_recommendations.ipynb** – Final insights and conclusions

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

- Build a predictive churn model using logistic regression, random forest, or gradient boosting.

- Test retention interventions and simulate potential impact on revenue.

- Extend the analysis to include customer feedback or support ticket data.

## Author

Thomas Ricketts 

Email: tbrricketts@gmail.com \
LinkedIn: https://www.linkedin.com/in/thomas-ricketts7/ \
GitHub: https://github.com/Rote-Story 

