# src/prep.py
from __future__ import annotations
import pandas as pd
import numpy as np
from src.config import SFR_CODE, CURRENT_YEAR

def clean_and_engineer(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Filter to Single Family Residence
    df = df[df["Property Use Type"] == SFR_CODE]

    # Drop duplicates + missing values
    df = df.drop_duplicates()
    df = df.dropna()

    # Drop ZIP (not needed after filtering)
    if "Zip Code" in df.columns:
        df = df.drop(columns=["Zip Code"])

    # Feature engineering
    df["price/sqft"] = df["Total Value"] / df["Square Footage"]
    df["house_age"] = CURRENT_YEAR - df["Year Built"]

    df["improvement_to_land_ratio"] = df["Improvement Value"] / df["Land Value"]

    # Remove impossible values / division issues
    df = df.replace([np.inf, -np.inf], np.nan).dropna()
    df = df[
        (df["Square Footage"] > 0) &
        (df["Total Value"] > 0) &
        (df["house_age"] >= 0)
    ]

    return df

def add_high_value_flag(df: pd.DataFrame, quantile: float = 0.95) -> pd.DataFrame:
    """
    Adds 'is_high_value' boolean flag using Total Value quantile threshold.
    """
    df = df.copy()
    threshold = df["Total Value"].quantile(quantile)
    df["is_high_value"] = df["Total Value"] >= threshold
    return df
