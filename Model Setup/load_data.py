import pandas as pd

df = pd.read_csv("mumbai_house_prices.csv")
print("Columns before removal : ",df.columns)
df.drop(columns=["Unnamed: 0"], inplace=True)
print("Columns after removal : ",df.columns)
df.rename(columns={
    "Price": "price",
    "Area": "area",
    "Location": "loc",
    "No. of Bedrooms": "bd",
    "New/Resale": "nr",
    "Gymnasium": "g",
    "Lift Available": "la",
    "Car Parking": "cp",
    "24x7 Security": "se",
    "Swimming Pool": "sp"
}, inplace=True)

df = df[
    ["price","area","loc","bd","nr","g","la","cp","se","sp"]
]
binary_cols = ["nr","g","la","cp","se","sp"]

for col in binary_cols:
    df[col] = df[col].map({"Yes":1, "No":0})
print(df["loc"].value_counts())
top_locs = df["loc"].value_counts().head(10).index
df = df[df["loc"].isin(top_locs)]
df.dropna(inplace=True)
print(df.head())
print(df.info())

# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split
# import joblib

# X = df.drop("price", axis=1)
# y = df["price"]

# num_features = ["area","bd","nr","g","la","cp","se","sp"]
# cat_features = ["loc"]

# preprocessor = ColumnTransformer(
#     transformers=[
#         ("num", "passthrough", num_features),
#         ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
#     ]
# )

# model = Pipeline([
#     ("prep", preprocessor),
#     ("rf", RandomForestRegressor(
#         n_estimators=300,
#         random_state=42,
#         n_jobs=-1
#     ))
# ])

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# model.fit(X_train, y_train)

# print("Train Score:", model.score(X_train, y_train))
# print("Test Score:", model.score(X_test, y_test))

# joblib.dump(model, "real_estate_model.joblib")
