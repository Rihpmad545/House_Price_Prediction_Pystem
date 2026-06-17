
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")
df = pd.read_csv("house_data.csv")

print("\nHOUSE PRICE PREDICTION")
print("-" * 40)


# =========================
# INPUT SECTION
# =========================
area = float(input("Area (sq ft): "))
bedrooms = int(input("Bedrooms: "))
bathrooms = int(input("Bathrooms: "))
floors = int(input("Floors: "))
age = int(input("Age: "))
garage = int(input("Garage (0/1): "))
balcony = int(input("Balcony (0/1): "))

furnished = int(input("Furnished (0/1): "))
garden = int(input("Garden (0/1): "))
swimming_pool = int(input("Swimming Pool (0/1): "))

distance_to_city = float(input("Distance To City: "))
nearby_schools = int(input("Nearby Schools: "))
nearby_hospitals = int(input("Nearby Hospitals: "))
crime_rate = float(input("Crime Rate: "))
population_density = int(input("Population Density: "))
public_transport_score = float(input("Public Transport Score: "))
property_tax = float(input("Property Tax: "))
location_rating = float(input("Location Rating: "))
electricity_backup = int(input("Electricity Backup (0/1): "))
security_rating = float(input("Security Rating: "))


# DATAFRAME FOR MODEL

house_data = pd.DataFrame([[ 
    area, bedrooms, bathrooms, floors, age,
    garage, balcony, furnished, garden, swimming_pool,
    distance_to_city, nearby_schools, nearby_hospitals,
    crime_rate, population_density, public_transport_score,
    property_tax, location_rating, electricity_backup,
    security_rating
]], columns=[
    "Area_sqft","Bedrooms","Bathrooms","Floors","Age",
    "Garage","Balcony","Furnished","Garden","SwimmingPool",
    "DistanceToCity","NearbySchools","NearbyHospitals",
    "CrimeRate","PopulationDensity","PublicTransportScore",
    "PropertyTax","LocationRating","ElectricityBackup",
    "SecurityRating"
])

# =========================
# PREDICTION
# =========================
house_scaled = scaler.transform(house_data)
predicted_price = float(model.predict(house_scaled)[0])

print("\nRaw Predicted Price:", predicted_price)

# safety clamp
if predicted_price < 0:
    predicted_price = df["Price"].min()

print("\n==============================")
print("ESTIMATED PRICE:", f"₹{predicted_price:,.0f}")
print("==============================")

# =========================
# OPENAI ANALYSIS
# =========================
prompt = f"""
You are a real estate expert.

Property:
Area: {area}
Bedrooms: {bedrooms}
Bathrooms: {bathrooms}
Age: {age}
Location Rating: {location_rating}
Crime Rate: {crime_rate}

Predicted Price: ₹{predicted_price:,.0f}

Explain in:
1. Overview
2. Pros
3. Cons
4. Buyer type
5. Investment value
6. Rental value
"""
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
)

ai_reply = response.json()["response"]

print("\n" + "=" * 60)
print("AI PROPERTY CONSULTANT")
print("=" * 60)
print(ai_reply)

# GRAPH

avg_price = float(df["Price"].mean())

plt.figure(figsize=(8,5))

bars = plt.bar(
    ["Average Price", "Your House"],
    [avg_price, predicted_price]
)

plt.title("House Price Comparison")
plt.ylabel("Price (₹)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             height,
             f"₹{height:,.0f}",
             ha="center",
             va="bottom")

plt.tight_layout()
plt.show()