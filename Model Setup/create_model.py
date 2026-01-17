import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor


# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("mumbai_house_prices.csv")

print("Initial shape:", df.shape)


# =========================
# 2. RENAME COLUMNS
# =========================
df.rename(columns={
    "Price": "price",
    "Area": "area",
    "Location": "loc",
    "No. of Bedrooms": "bd",
    "New/Resale": "nr",
    "Gymnasium": "g",
    "Lift Available": "la",
    "Car Parking": "cp",
    "Maintenance Staff": "ms",
    "24x7 Security": "se",
    "Children's Play Area": "ca",
    "Clubhouse": "cl",
    "Intercom": "inte",
    "Landscaped Gardens": "lg",
    "Indoor Games": "ig",
    "Gas Connection": "gc",
    "Jogging Track": "jt",
    "Swimming Pool": "sp"
}, inplace=True)


# =========================
# 3. SELECT FINAL FEATURES
# =========================
FEATURES = [
    "area", "bd", "nr", "g", "la", "cp", "ms", "se", "ca",
    "cl", "inte", "lg", "ig", "gc", "jt", "sp", "loc"
]

df = df[["price"] + FEATURES]


# =========================
# 4. CLEAN BINARY COLUMNS
# =========================
binary_cols = [
    "nr", "g", "la", "cp", "ms", "se", "ca",
    "cl", "inte", "lg", "ig", "gc", "jt", "sp"
]

for col in binary_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({
            "yes": 1,
            "no": 0,
            "new": 1,
            "resale": 0,
            "1": 1,
            "0": 0
        })
    )


# =========================
# 5. DROP INVALID ROWS
# =========================
df.dropna(inplace=True)

print("After cleaning:", df.shape)


# =========================
# 6. SPLIT FEATURES & TARGET
# =========================
X = df.drop("price", axis=1)
y = df["price"]

num_features = [
    "area", "bd", "nr", "g", "la", "cp", "ms", "se",
    "ca", "cl", "inte", "lg", "ig", "gc", "jt", "sp"
]

cat_features = ["loc"]


# =========================
# 7. PREPROCESSING PIPELINE
# =========================
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", num_features),
        ("cat", OneHotEncoder(
            categories=[[
                "Ambivali", "Shahad", "Andheri", "Asangaon", "Dombivali",
                "Ghatkopar", "Kalyan", "Malad", "Powai", "Thane", "Worli"
            ]],
            handle_unknown="ignore"
        ), cat_features)
    ]
)


# =========================
# 8. MODEL PIPELINE
# =========================
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    ))
])


# =========================
# 9. TRAIN / TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# =========================
# 10. TRAIN MODEL
# =========================
model.fit(X_train, y_train)


# =========================
# 11. EVALUATION
# =========================
print("Train R²:", model.score(X_train, y_train))
print("Test  R²:", model.score(X_test, y_test))


# =========================
# 12. SAVE MODEL
# =========================
joblib.dump(model, "real_estate_price_model.joblib")

print("✅ Model saved as real_estate_price_model.joblib")
