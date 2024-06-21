from django.shortcuts import render
import pandas as pd
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    # Load dataset
    data = pd.read_csv(r"C:\Users\abhis\Desktop\PROJECT_EXPOSYS_DATA_LABS\project\dataset.csv")
    x = data.drop("Outcome", axis=1)
    y = data['Outcome']

    # Train-test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # Train the model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Get input values from the form
    val1 = request.GET.get('n1', '').strip()
    val2 = request.GET.get('n2', '').strip()
    val3 = request.GET.get('n3', '').strip()
    val4 = request.GET.get('n4', '').strip()
    val5 = request.GET.get('n5', '').strip()
    val6 = request.GET.get('n6', '').strip()
    val7 = request.GET.get('n7', '').strip()
    val8 = request.GET.get('n8', '').strip()

    # Validate input fields
    if not val1 or not val2 or not val3 or not val4 or not val5 or not val6 or not val7 or not val8:
        return render(request, 'predict.html', {"result2": "Error: All fields are required."})

    try:
        # Convert inputs to float
        val1 = float(val1)
        val2 = float(val2)
        val3 = float(val3)
        val4 = float(val4)
        val5 = float(val5)
        val6 = float(val6)
        val7 = float(val7)
        val8 = float(val8)

        # Make prediction
        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
        result1 = "Positive" if pred == [1] else "Negative"

    except ValueError:
        result1 = "Error: Invalid input values. Please enter valid numbers."

    return render(request, 'predict.html', {"result2": result1})
