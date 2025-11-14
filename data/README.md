# Data Folder Overview

This folder contains all data used in the Telco Customer Churn Analysis project. 

## Folder Structure

### `raw/`
Contains the original dataset downloaded from [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn):

- `WA_Fn-UseC_-Telco-Customer-Churn.csv`: Original CSV file containing customer demographics, account information, and service usage details.

### `processed/`
Contains datasets that have been cleaned or transformed for analysis and modeling:

- `readable_telco_churn_data.csv`: Cleaned and human-readable version of the original dataset.
- `encoded_telco_churn_data.csv`: Preprocessed version with categorical variables encoded, ready for machine learning modeling.

## Notes
- The raw dataset is included for reproducibility.  
- Processed datasets are generated using scripts in the `notebooks/` folder.  
- Any changes or transformations applied to the data are documented in the corresponding Jupyter notebooks.
