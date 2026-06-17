import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("house_data.csv")

print("\nDATASET CHECK")
print("-" * 30)
print("Total Records:", len(df))
print("Minimum Price: ₹{:,.0f}".format(df["Price"].min()))
print("Maximum Price: ₹{:,.0f}".format(df["Price"].max()))
print("Average Price: ₹{:,.0f}".format(df["Price"].mean()))

X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)

print("\nLINEAR REGRESSION RESULTS")
print("-" * 30)

linear_mae = mean_absolute_error(y_test, linear_predictions)
linear_r2 = r2_score(y_test, linear_predictions)

print("Mean Absolute Error: ₹{:,.2f}".format(linear_mae))
print("R2 Score:", round(linear_r2, 4))

tree_model = DecisionTreeRegressor(
    max_depth=12,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)

tree_model.fit(X_train, y_train)

tree_predictions = tree_model.predict(X_test)

print("\nDECISION TREE RESULTS")
print("-" * 30)

tree_mae = mean_absolute_error(y_test, tree_predictions)
tree_r2 = r2_score(y_test, tree_predictions)

print("Mean Absolute Error: ₹{:,.2f}".format(tree_mae))
print("R2 Score:", round(tree_r2, 4))

if linear_r2 > tree_r2:
    best_model = linear_model
    print("\nBest Model: Linear Regression")
else:
    best_model = tree_model
    print("\nBest Model: Decision Tree")

joblib.dump(best_model, "house_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model saved successfully")