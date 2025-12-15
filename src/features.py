# src/features.py

def get_eda_only_features():
    return [
        'tenure_group',
        'monthly_charge_group',
        'total_charge_group',
        'loyal_high_spender',
        'revenue_per_year',
        'avg_monthly_charges',
        'tenure_years'
    ]

def get_target(df):
    return [col for col in df.columns if 'churn' in col]

def get_model_features(df):
    eda_only = get_eda_only_features()
    target = get_target(df)
    return [col for col in df.columns if col not in eda_only + target]

def get_numeric_features(df):
    return [col for col in df.columns if df[col].dtype in ('int64', 'float64')]

def get_categorical_features(df):
    return [col for col in df.columns if df[col].dtype == 'object']