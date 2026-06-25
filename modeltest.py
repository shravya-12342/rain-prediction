import joblib
import numpy as np

# Load trained KNN model
model = joblib.load("knn_model.pkl")

print("=" * 50)
print("      Rain Prediction System")
print("=" * 50)

print("\nInstructions:")
print("1. Enter 24 feature values separated by spaces.")
print("2. Use numeric values only.")
print("3. Example:")
print("   1 23.5 65 1012 4.5 0 0 1 0 12 25 60 1008 3.2 0 0 1 0 15 22 70 1010 5.1 0")
print()

try:
    user_input = input("Enter 24 feature values: ")

    # Convert input to list of floats
    values = list(map(float, user_input.strip().split()))

    # Check number of features
    if len(values) != 24:
        print(f"\nError: Expected 24 values, but received {len(values)}.")
        exit()

    # Convert to NumPy array
    features = np.array(values).reshape(1, -1)

    # Predict
    prediction = model.predict(features)[0]

    print("\nPrediction Result")
    print("-" * 30)

    if prediction == 1:
        print("Rain Expected")
        print("Prediction: YES, it will rain.")
    else:
        print("No Rain Expected")
        print("Prediction: NO, it will not rain.")

except ValueError:
    print("\nInvalid input!")
    print("Please enter only numeric values separated by spaces.")

except Exception as e:
    print("\nAn error occurred:")
    print(e)