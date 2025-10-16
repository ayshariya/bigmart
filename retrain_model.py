import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# 1️⃣ Load your cleaned dataset
df = pd.read_excel("cleaned_bigmart.xlsx")

# 2️⃣ Define features (X) and target (y)
X = df.drop("Item_Outlet_Sales", axis=1)
y = df["Item_Outlet_Sales"]

# 3️⃣ Encode categorical columns if needed
X = pd.get_dummies(X)

# 4️⃣ Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5️⃣ (Optional) Standardize numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6️⃣ Train the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 7️⃣ Save the model and scaler
with open("big_mart.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Random Forest model retrained and saved successfully!")