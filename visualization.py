import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("house_data.csv")

plt.figure(figsize=(10,6))
plt.hist(df["Price"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Number of Houses")
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df["Area_sqft"], df["Price"], color="green")

z = np.polyfit(df["Area_sqft"], df["Price"], 1)
p = np.poly1d(z)

plt.plot(df["Area_sqft"], p(df["Area_sqft"]), color="black")
plt.title("Do Bigger Houses Cost More?")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df["LocationRating"], df["Price"], color="purple")

z = np.polyfit(df["LocationRating"], df["Price"], 1)
p = np.poly1d(z)

plt.plot(df["LocationRating"], p(df["LocationRating"]), color="black")
plt.title("How Location Rating Affects House Prices")
plt.xlabel("Location Rating")
plt.ylabel("Price")
plt.grid(True, alpha=0.3)
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df["DistanceToCity"], df["Price"], color="red")

z = np.polyfit(df["DistanceToCity"], df["Price"], 1)
p = np.poly1d(z)

plt.plot(df["DistanceToCity"], p(df["DistanceToCity"]), color="black")
plt.title("How Distance from the City Affects House Prices")
plt.xlabel("Distance From City")
plt.ylabel("Price")
plt.grid(True, alpha=0.3)
plt.show()

avg_price_bedroom = df.groupby("Bedrooms")["Price"].mean()

plt.figure(figsize=(10,6))
avg_price_bedroom.plot(kind="bar", color="orange")
plt.title("Average House Price by Number of Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Average Price")
plt.grid(True, alpha=0.3)
plt.show()

avg_price_security = df.groupby("SecurityRating")["Price"].mean()

plt.figure(figsize=(10,6))
avg_price_security.plot(kind="bar", color="brown")
plt.title("Average House Price by Security Rating")
plt.xlabel("Security Rating")
plt.ylabel("Average Price")
plt.grid(True, alpha=0.3)
plt.show()