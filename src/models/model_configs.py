# src/models/model_configs.py

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# Models used in machine learning
# Churn target class is imbalanced (26% churn vs not churn)
models = {
    'logistic_regression': LogisticRegression(max_iter=2000, class_weight='balanced'),
    'random_forest': RandomForestClassifier(n_estimators=300, random_state=42, class_weight='balanced'),
    'gradient_boosting': GradientBoostingClassifier()
}

# Tune hyperparameters to improve model performance
hyperparams = {
    'logistic_regression': {
        'model__C': [0.01, 0.1, 1, 10],
        'model__penalty': ['l2'],
        'model__solver': ['lbfgs'],
        'model__max_iter': [200, 500]    
    },
    'random_forest': {
        'model__n_estimators': [200, 300, 500],
        'model__max_depth': [None, 5, 10],
        'min_samples_split': [2, 10, 20],
        'max_features': ['sqrt', 'log2', 0.3]
    },
    'gradient_boosting': {
        'model__learning_rate': [0.01, 0.05, 0.1],
        'model__n_estimators': [100, 200, 300],
        'max_depth': [2, 3, 4],
        'subsample': [0.6, 0.8, 1.0]
    }
}
