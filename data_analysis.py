# data_analysis.py

import pandas as pd
import numpy as np


def analyze_data():
    # Load dataset
    df = pd.read_csv("house_data.csv")

    print("\n" + "=" * 50)
    print("HOUSE PRICE DATA ANALYSIS")
    print("=" * 50)

    # Display first 5 rows
    print("\nFirst 5 Rows:")
    print(df.head())

    # Dataset information
    print("\nDataset Information:")
    print(df.info())

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Statistical summary
    print("\nStatistical Summary:")
    print(df.describe())

    # Mean
    print("\nMean Values:")
    print(df.mean(numeric_only=True))

    # Median
    print("\nMedian Values:")
    print(df.median(numeric_only=True))

    # Mode
    print("\nMode Values:")
    print(df.mode().iloc[0])

    # Standard Deviation
    print("\nStandard Deviation:")
    print(df.std(numeric_only=True))

    # Percentiles for Price
    if "Price" in df.columns:
        print("\nPrice Percentiles:")
        print(f"25th Percentile: {np.percentile(df['Price'], 25):,.2f}")
        print(f"50th Percentile (Median): {np.percentile(df['Price'], 50):,.2f}")
        print(f"75th Percentile: {np.percentile(df['Price'], 75):,.2f}")

    # Correlation Matrix
    print("\nCorrelation Matrix:")
    print(df.corr(numeric_only=True))

    print("\nData Analysis Completed Successfully!")


if __name__ == "__main__":
    analyze_data()