import pandas as pd
import numpy as np
from src.pipeline.db import connect
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

engine = connect()
df = pd.read_sql(sql="SELECT * FROM patient_cleaned;", con=engine)

x = df.drop("admission_type", axis=1)
y = df["admission_type"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

numeric_features = ["age", "room_number"]
categorical_features = [
    "gender", "blood_type", "medical_condition",
    "medication", "test_results", "name"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000))
    ]
)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
