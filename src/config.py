# src/config.py

USE_COLS = [
    "Total Value",
    "Property Use Type",
    "Year Built",
    "Square Footage",
    "Number of Bedrooms",
    "Number of Bathrooms",
    "Number of Units",
    "Improvement Value",
    "Land Value",
    "Total Value Land Improvement",
    "Taxable Value",
    "Zip Code",
]

DTYPES = {
    "Total Value": "float32",
    "Property Use Type": "string",
    "Year Built": "float32",
    "Square Footage": "float32",
    "Number of Bedrooms": "float32",
    "Number of Bathrooms": "float32",
    "Number of Units": "float32",
    "Improvement Value": "float32",
    "Land Value": "float32",
    "Total Value Land Improvement": "float32",
    "Taxable Value": "float32",
    "Zip Code": "string",
}

ZIP_TARGET = "91766"
SFR_CODE = "SFR"
CURRENT_YEAR = 2026

FEATURES = ["Year Built","Square Footage","Number of Bedrooms","Number of Bathrooms","Number of Units"]
TARGET = "Total Value"
CV_MAE = 46532.09