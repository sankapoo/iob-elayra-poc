import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    print("🔧 Training model...")
    df = pd.read_csv("diabetes.csv")
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = LogisticRegression(max_iter=300)
    model.fit(X_train, y_train)

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("test_data.pkl", "wb") as f:
        pickle.dump((X_test, y_test), f)

    print("✅ Model training complete. Files saved: model.pkl, test_data.pkl")