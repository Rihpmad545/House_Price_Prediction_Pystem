import os

while True:
    print("\n" + "=" * 50)
    print("HOUSE PRICE PREDICTOR")
    print("=" * 50)
    print("1. Data Analysis")
    print("2. View Visualizations")
    print("3. Train Model")
    print("4. Predict House Price")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        os.system("python data_analysis.py")

    elif choice == "2":
        os.system("python visualization.py")

    elif choice == "3":
        os.system("python train_model.py")

    elif choice == "4":
        os.system("python prediction.py")

    elif choice == "5":
        print("\nThank you for using House Price Predictor!")
        break

    else:
        print("\nInvalid choice. Please try again.")