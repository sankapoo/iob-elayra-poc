import pickle
from sklearn.metrics import classification_report

if __name__ == "__main__":
    print("📊 Evaluating model...")

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("test_data.pkl", "rb") as f:
        X_test, y_test = pickle.load(f)

    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)

    print("Classification Report:\n", report)
    with open("report.txt", "w") as f:
        f.write(report)
    print("✅ Saved classification report to report.txt")
