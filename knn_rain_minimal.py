"""
ULTRA-SIMPLE KNN RAIN PREDICTION
=================================
Minimal version - just the essentials!

Install: pip install pandas numpy scikit-learn
Run: python knn_rain_minimal.py
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

print("\n🌧️  KNN RAIN PREDICTION\n")

# 1. LOAD DATA
print("1️⃣  Loading data...")
df = pd.read_csv('weatherdatafinal.csv')
print(f"   Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. PREPARE DATA
print("2️⃣  Preparing data...")

# Create target: Rain (1) or No Rain (0)
df['rain_target'] = ((df['precip'] > 0) | (df['precipprob'] > 50)).astype(int)

# Drop unnecessary columns
df = df.drop(columns=['name', 'datetime', 'preciptype', 'description', 
                      'icon', 'stations', 'sunrise', 'sunset'], errors='ignore')

# Fill missing values
df = df.fillna(df.median(numeric_only=True))

# Select features (only numerical columns)
feature_cols = [col for col in df.columns if col != 'rain_target' and col != 'conditions']
X = df[feature_cols].select_dtypes(include=[np.number])
y = df['rain_target']

print(f"   Features: {len(X.columns)}")
print(f"   Rain: {(y == 1).sum()}, No Rain: {(y == 0).sum()}")

# 3. SPLIT DATA
print("3️⃣  Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"   Train: {len(X_train)}, Test: {len(X_test)}")

# 4. SCALE
print("4️⃣  Scaling features...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. TRAIN
print("5️⃣  Training KNN model...")
model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train, y_train)

# 6. EVALUATE
print("6️⃣  Evaluating model...")
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print(f"\n📊 RESULTS:")
print(f"   Accuracy:  {accuracy:.2%}")
print(f"   Precision: {precision:.2%}")
print(f"   Recall:    {recall:.2%}")
print(f"   F1-Score:  {f1:.2%}")

# 7. SAVE
print("\n💾 Saving model...")
import joblib
joblib.dump(model, 'knn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(X.columns.tolist(), 'features.pkl')
print("   ✓ Saved!")

# 8. PREDICT
print("\n🔮 Making a prediction...")
sample = pd.DataFrame({
    'tempmax': [28.5],
    'tempmin': [18.2],
    'temp': [23.3],
    'humidity': [70.0],
    'cloudcover': [45.0],
    'windspeed': [12.5],
    'dew': [15.0],
})

# Add missing columns
for col in X.columns:
    if col not in sample.columns:
        sample[col] = X[col].median()

sample_scaled = scaler.transform(sample[X.columns])
pred = model.predict(sample_scaled)[0]
prob = model.predict_proba(sample_scaled)[0]

if pred == 0:
    print(f"   ☀️  NO RAIN ({prob[0]:.0%} confident)")
else:
    print(f"   🌧️  RAIN ({prob[1]:.0%} confident)")

print("\n✅ DONE!\n")
