from django.shortcuts import render
from .forms import NawForm
import joblib
import os
import pandas as pd


# ===============================
# LOAD MODEL ONCE (IMPORTANT)
# ===============================
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "real_estate_price_model.joblib"
)

model = joblib.load(MODEL_PATH)


# ===============================
# PREDICTION VIEW
# ===============================
from django.shortcuts import render
from .forms import NawForm
import joblib
import os
import pandas as pd

# Load the model ONCE
MODEL_PATH = os.path.join(os.path.dirname(__file__), "real_estate_price_model.joblib")
model = joblib.load(MODEL_PATH)


def prediction(request):
    msg = "Please fill property details to get price prediction"

    if request.method == "POST":
        fm = NawForm(request.POST)
        if fm.is_valid():
            data = fm.cleaned_data

            # Build DataFrame in the same order as training
            input_df = pd.DataFrame([{
                "area": int(data["area"]),
                "bd": int(data["bd"]),
                "nr": int(data["nr"]),
                "g": int(data["g"]),
                "la": int(data["la"]),
                "cp": int(data["cp"]),
                "ms": int(data["ms"]),
                "se": int(data["se"]),
                "ca": int(data["ca"]),
                "cl": int(data["cl"]),
                "inte": int(data["inte"]),
                "lg": int(data["lg"]),
                "ig": int(data["ig"]),
                "gc": int(data["gc"]),
                "jt": int(data["jt"]),
                "sp": int(data["sp"]),
                "loc": data["loc"]
            }])

            # Prediction
            predicted_price = model.predict(input_df)[0]

            # Format price
            if predicted_price >= 1_00_00_000:
                price = round(predicted_price / 1_00_00_000, 2)
                msg = f"Predicted price: ₹ {price} Crore"
            else:
                price = round(predicted_price / 1_00_000, 2)
                msg = f"Predicted price: ₹ {price} Lakh"

            return render(request, "result.html", {"msg": msg})

    else:
        # For GET request
        fm = NawForm()

    return render(request, "prediction.html", {"fm": fm, "msg": msg})


def result(request):
    return render(request, "result.html")
