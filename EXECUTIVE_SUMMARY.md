- **# Customer Retention Analysis:** Telco Churn Dataset
### Understanding customer behavior and identifying churn drivers for a telecommunications company

---


## **Project Overview**

Customer churn - the rate at which customers stop using a company's services - is a critical challenge for subscription-based businesses like Telco. High churn can result from dissatisfaction, competitive offers, or other factors, and reducing it is essential for maintaining steady revenue growth.

The goal of this project is to identify the key drivers of churn and provide actionable insights to improve customer retention. Using SQL for structured queries and Python for data analysis, the project explores patterns in customer demographics, account information, and service usage within the Telco Customer Churn dataset. Findings inform data-driven recommendations to reduce churn and enhance retention strategies.

**Analytical Objectives**

- Identify customer characteristics most strongly associated with churn.

- Analyze the impact of contract type, payment method, and tenure on churn.

- Quantify churn rates across different customer segments.

- Provide actionable, business-oriented recommendations for retention programs.

### **Executive Summary**

This project combines exploratory data analysis and predictive modeling to understand customer churn and proactively identify high-risk customers. The analysis integrates a reproducible machine-learning pipeline, cross-validation, threshold optimization, and interpretable feature-level insights.

**1.** **Key Findings**

- **Churn is imbalanced:** only a minority of customers leave, so precision-recall metrics are more informative than overall accuracy.

- Top churn drivers include tenure, contract type, monthly charges, internet service, and add-on technical support.

- **Highest-risk groups:** month-to-month contract holders, customers with higher monthly charges, and those without technical support.

**2.** **Modeling Results**

- A logistic regression pipeline with ColumnTransformer provides a stable, interpretable baseline:

  - **Cross-validated ROC-AUC:** ~0.85

  - **Cross-validated PR-AUC:** substantially above the baseline churn rate

- Tree-based models (Random Forest, Gradient Boosting) perform similarly or slightly better in PR-AUC but offer less interpretability.

- Feature importance (permutation & SHAP) confirms that contract type, tenure, and financial metrics are the strongest predictors of churn.

**3.** **Operational Insights**

- The default 0.5 probability threshold is not optimal for retention campaigns.

- Adjusting the threshold can materially increase net savings, depending on the cost of outreach and the monetary value of retaining a customer.

**4.** **Recommended Actions**

- **Focus retention programs on:**

  - Short-tenure customers

  - Month-to-month contract holders

  - High monthly charge customers

  - Customers without support add-ons

- Consider incentives such as discounted long-term contracts or service bundles for high-risk customers.

**5.** **Next Steps**

- Deploy the model in a monitoring workflow, updating predictions monthly or quarterly.

- Integrate SHAP explanations for deeper, interpretable insights at the customer level.

- Incorporate Customer Lifetime Value (CLV) to refine threshold optimization and maximize ROI.

- Explore uplift modeling to target customers whose behavior is most likely to change when contacted.
