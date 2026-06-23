# 🏠 House Price Prediction and Property Analysis System

A Machine Learning project that predicts house prices based on property features and generates detailed property insights using a locally hosted language model.

---

# 📌 Project Overview

This project estimates the market value of a house using Machine Learning techniques and various property characteristics.

The system analyzes features such as :-

* Area
* Bedrooms
* Bathrooms
* Floors
* Property Age
* Garage Availability
* Balcony Availability
* Furnishing Status
* Garden Availability
* Swimming Pool Availability
* Distance from City
* Nearby Schools
* Nearby Hospitals
* Crime Rate
* Population Density
* Public Transport Score
* Property Tax
* Location Rating
* Electricity Backup
* Security Rating

The application also provides a detailed property assessment to help users better understand the strengths and weaknesses of a property.

---

# 🚀 Features

## Data Analysis

* Dataset inspection
* Statistical summaries
* Minimum and maximum prices
* Dataset overview

## Data Visualization

* Price distribution analysis
* Feature relationship analysis
* Visual representation of housing data

## Model Training

* Data preprocessing
* Feature scaling
* Machine Learning model training
* Model evaluation
* Automatic model saving

## House Price Prediction

* User-input based predictions
* Real-time price estimation
* Property value comparison with dataset averages

## Property Assessment

Provides:

* Property Overview
* Advantages
* Disadvantages
* Suitable Buyer Profile
* Investment Potential
* Rental Potential

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Joblib
* Ollama
* Llama 3.2

---

# 📂 Project Structure

House-Price-Predictor/

├── main.py

├── data_analysis.py

├── visualization.py

├── train_model.py

├── prediction.py

├── house_data.csv

├── house_price_model.pkl

├── scaler.pkl

├── README.md

├── requirements.txt

└── .gitignore

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
cd House-Price-Predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download Ollama:

https://ollama.com

Pull the model:

```bash
ollama pull llama3.2
```

---

# ▶️ Running the Project

Run:

```bash
python main.py
```

Menu:

```text
HOUSE PRICE PREDICTOR

1. Data Analysis
2. View Visualizations
3. Train Model
4. Predict House Price
5. Exit
```

Select the desired option and follow the prompts.

---

# 📊 Machine Learning Workflow

1. Load Dataset
2. Analyze Dataset
3. Visualize Data
4. Scale Features
5. Train Model
6. Save Model
7. Predict House Price
8. Generate Property Assessment

---

# 📈 Dataset Information

Dataset Size: 3000 Records

Features Used:

* Area_sqft
* Bedrooms
* Bathrooms
* Floors
* Age
* Garage
* Balcony
* Furnished
* Garden
* SwimmingPool
* DistanceToCity
* NearbySchools
* NearbyHospitals
* CrimeRate
* PopulationDensity
* PublicTransportScore
* PropertyTax
* LocationRating
* ElectricityBackup
* SecurityRating

Target Variable:

* Price

---

# 📚 Learning Outcomes

This project was developed as a practical learning experience in Machine Learning and Python development.

Skills developed during this project:

* Data preprocessing and analysis using Pandas
* Data visualization using Matplotlib
* Machine Learning model development using Scikit-Learn
* Feature scaling and model evaluation
* Model persistence using Joblib
* Building a menu-driven Python application
* Working with locally hosted language models through Ollama
* Combining Machine Learning predictions with automated property assessment

This was my first project involving integration with a locally hosted Large Language Model (LLM), making it an important milestone in my learning journey toward Artificial Intelligence and Machine Learning development.

---

# 👨‍💻 Author

Shreeyash Sawant

Computer Engineering Student

Areas of Interest:

* Artificial Intelligence
* Machine Learning
* Data Science
* Software Development

---

# 📜 License

This project is intended for educational and learning purposes.
