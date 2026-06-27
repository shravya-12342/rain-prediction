"""
Rain Prediction System
======================
Real-time prediction interface for KNN Rain Prediction model
Load model → Get user input → Make predictions → Display results
"""

import joblib
import numpy as np
import json
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load trained KNN model
model = joblib.load("knn_model.pkl")

def get_confidence_bar(confidence: float) -> str:
    """Generate ASCII confidence bar"""
    bar_length = 30
    filled = int(bar_length * confidence)
    empty = bar_length - filled

    if confidence > 0.8:
        bar = "✓" * filled + "░" * empty
    elif confidence > 0.6:
        bar = "•" * filled + "░" * empty
    else:
        bar = "○" * filled + "░" * empty

    return bar

def save_prediction(features, prediction, confidence):
    """Save prediction to log file"""
    try:
        log_file = Path("predictions_log.json")

        prediction_record = {
            'timestamp': datetime.now().isoformat(),
            'features': features,
            'prediction': str(prediction),
            'confidence': float(confidence)
        }

        if log_file.exists():
            with open(log_file, 'r') as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(prediction_record)

        with open(log_file, 'w') as f:
            json.dump(logs, f, indent=2)

        logger.info(f"✓ Prediction saved to {log_file}")

    except Exception as e:
        logger.warning(f"⚠ Could not save prediction log: {str(e)}")


# ==================== MAIN ====================

print("\n" + "=" * 80)
print("🌧️  RAIN PREDICTION SYSTEM".center(80))
print("=" * 80)
print(f"\n  📊 Algorithm : K-Nearest Neighbors (KNN)")
print(f"  🔢 Features  : 24")
print(f"  ⏰ Loaded    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\n" + "=" * 80)

print("\n📋 Instructions:")
print("  1. Enter 24 feature values separated by spaces.")
print("  2. Use numeric values only.")
print("  3. Example:")
print("     1 23.5 65 1012 4.5 0 0 1 0 12 25 60 1008 3.2 0 0 1 0 15 22 70 1010 5.1 0")
print("  4. Type 'quit' to exit.\n")

while True:
    try:
        print("Enter 24 feature values (space-separated):")
        print(">>> ", end="", flush=True)
        user_input = input().strip()

        if user_input.lower() in ['quit', 'q', 'exit']:
            break

        # Convert input to list of floats
        values = list(map(float, user_input.split()))

        # Validate feature count
        if len(values) != 24:
            print(f"\n❌ Error: Expected 24 values, but received {len(values)}.\n")
            continue

        # Convert to NumPy array
        features = np.array(values).reshape(1, -1)

        # Predict
        prediction = model.predict(features)[0]

        # Calculate confidence using KNN distances (same method as reference)
        distances, indices = model.kneighbors(features)
        avg_distance = distances[0].mean()
        confidence = 1.0 / (1.0 + avg_distance)

        # ---- Display Result ----
        print("\n" + "=" * 80)
        print("🎯 PREDICTION RESULT".center(80))
        print("=" * 80)

        # Input features summary
        print("\n📊 Input Features:")
        print("-" * 40)
        for i, val in enumerate(values, 1):
            print(f"  {i:2d}. Feature {i:<20}: {val:>10.4f}")

        # Prediction
        print("\n🔮 Classification Result:")
        print("-" * 40)

        if prediction == 1:
            print(f"  Predicted Class: Rain Expected")
            print(f"  Prediction     : ✅ YES, it will rain.")
        else:
            print(f"  Predicted Class: No Rain Expected")
            print(f"  Prediction     : 🌤️  NO, it will not rain.")

        print(f"  Confidence     : {confidence:.2%}")

        # Confidence bar
        confidence_bar = get_confidence_bar(confidence)
        print(f"  [{confidence_bar}]")

        # Recommendation
        print("\n💡 Recommendation:")
        print("-" * 40)
        if confidence > 0.8:
            print(f"  ✅ HIGH CONFIDENCE prediction")
        elif confidence > 0.6:
            print(f"  ⚠️  MEDIUM CONFIDENCE prediction")
        else:
            print(f"  ⚠️  LOW CONFIDENCE prediction")

        print("\n" + "=" * 80 + "\n")

        # Save prediction log
        save_prediction(values, prediction, confidence)

        # Continue or quit
        print("Press Enter for next prediction, or type 'quit' to exit...")
        next_input = input(">>> ").strip().lower()
        if next_input in ['quit', 'q', 'exit']:
            break

    except ValueError:
        print("\n❌ Invalid input! Please enter only numeric values separated by spaces.\n")

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        break

    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")

# Exit summary
print("\n" + "=" * 80)
print("📊 SESSION ENDED".center(80))
print("=" * 80)
print(f"  Session ended : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Logs saved to : predictions_log.json")
print("\n  ✅ Thank you for using Rain Prediction System!")
print("=" * 80 + "\n")