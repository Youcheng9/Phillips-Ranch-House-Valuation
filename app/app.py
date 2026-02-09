import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "xgb_final_model.pkl"
CV_MAE = 46157.47

FEATURES = [
    "Year Built",
    "Square Footage",
    "Number of Bedrooms",
    "Number of Bathrooms",
    "Number of Units",
]

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

def valuation_label(listing_price, predicted_price, mae=CV_MAE, pct=0.05):
    threshold = max(mae, pct * predicted_price)
    diff = listing_price - predicted_price
    diff_pct = diff / predicted_price if predicted_price != 0 else 0.0

    if diff > threshold:
        status = "Overvalued"
    elif diff < -threshold:
        status = "Undervalued"
    else:
        status = "Fairly priced"

    return status, diff, diff_pct, threshold

st.set_page_config(page_title="Phillips Ranch Home Valuation")
st.title("Phillips Ranch Home Valuation")

model = load_model()

st.subheader("Enter home features")

year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=1985, step=1)
sqft = st.number_input("Square Footage", min_value=100.0, max_value=20000.0, value=1500.0, step=25.0)
beds = st.number_input("Number of Bedrooms", min_value=0, max_value=20, value=3, step=1)
baths = st.number_input("Number of Bathrooms", min_value=0.0, max_value=20.0, value=2.0, step=0.5)
units = st.number_input("Number of Units", min_value=1, max_value=50, value=1, step=1)

listing_price = st.number_input("Listing Price ($)", min_value=0.0, value=800000.0, step=5000.0)

input_df = pd.DataFrame([{
    "Year Built": float(year_built),
    "Square Footage": float(sqft),
    "Number of Bedrooms": float(beds),
    "Number of Bathrooms": float(baths),
    "Number of Units": float(units),
}], columns=FEATURES)

if st.button("Evaluate"):
    pred_price = float(model.predict(input_df)[0])
    status, diff, diff_pct, threshold = valuation_label(listing_price, pred_price)

    st.metric("Estimated Fair Value", f"${pred_price:,.0f}")
    st.metric("Listing − Fair Value", f"${diff:,.0f}", f"{diff_pct*100:.1f}%")
    st.write(f"Decision threshold: **±${threshold:,.0f}**")

    if status == "Overvalued":
        st.error("Status: Overvalued 🔴")
    elif status == "Undervalued":
        st.success("Status: Undervalued 🟢")
    else:
        st.warning("Status: Fairly priced 🟡")
