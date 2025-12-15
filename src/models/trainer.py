# src/models/trainer.py

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from .model_configs import models, hyperparams
from src.preprocessing import build_preprocessor

def build_pipeline(model, categorical_features, numeric_features):
    
    preprocessor = build_preprocessor(
        numeric_features=numeric_features,
        categorical_features=categorical_features
        )
    
    return Pipeline([
        ('preprocess', preprocessor),
        ('model', model)
    ])

def train_model(model_name, df, feature_cols, target_col, categorical_features, numeric_features, tune=False):
    X = df[feature_cols]
    y = df[target_col].values.ravel() # Set shape to (n, )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    pipeline = build_pipeline(
        model=models[model_name], 
        numeric_features=numeric_features,
        categorical_features=categorical_features
        )

    if tune:
        param_grid = hyperparams.get(model_name, {})
        search = GridSearchCV(
            pipeline,
            param_grid=param_grid,
            cv=3,
            scoring='roc_auc',
            n_jobs=-1
        )
        search.fit(X_train, y_train)
        return search.best_estimator_, (X_train, X_test, y_train, y_test)

    pipeline.fit(X_train, y_train)
    return pipeline, (X_train, X_test, y_train, y_test)
