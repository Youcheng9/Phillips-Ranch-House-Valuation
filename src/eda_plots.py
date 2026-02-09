# src/eda_plots.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_histograms(df: pd.DataFrame):
    df.hist(figsize=(15, 10), bins=20, grid=True, edgecolor="black")
    plt.tight_layout()
    plt.show()

def plot_corr_heatmap(df: pd.DataFrame, title: str):
    corr_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(20, 15))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="Blues",
        linewidths=0.5
    )
    plt.title(title)
    plt.show()

def plot_distributions(df: pd.DataFrame):
    sns.displot(df["Square Footage"], color='#bce29e')
    plt.title("Distribution of Square Footage")
    plt.show()

    plt.hist(df["price/sqft"], bins=50)
    plt.xlabel("Price per Square Foot")
    plt.ylabel("Count")
    plt.title("Distribution of Price per Square Foot")
    plt.show()

    plt.hist(df["house_age"], bins=40)
    plt.xlabel("House Age")
    plt.ylabel("Count")
    plt.title("Distribution of House Age")
    plt.show()

def plot_relationships(df: pd.DataFrame):
    plt.scatter(df["Square Footage"], df["price/sqft"], alpha=0.5)
    plt.xlabel("Square Footage")
    plt.ylabel("Price per Sq Ft")
    plt.title("Square Footage vs Price per Square Foot")
    plt.show()

    plt.scatter(df["Square Footage"], df["Total Value"], alpha=0.5)
    plt.xlabel("Square Footage")
    plt.ylabel("Total Value")
    plt.title("Square Footage vs Total Value")
    plt.show()

    df.boxplot(column="Total Value", by="Number of Bedrooms", grid=False)
    plt.xlabel("Bedrooms")
    plt.ylabel("Total Value")
    plt.title("Total Value by Number of Bedrooms")
    plt.suptitle("")
    plt.show()

def plot_high_value_scatter(df: pd.DataFrame):
    high = df[df["is_high_value"]]
    normal = df[~df["is_high_value"]]

    plt.scatter(normal["Square Footage"], normal["Total Value"], alpha=0.5, label="Other Homes")
    plt.scatter(high["Square Footage"], high["Total Value"], alpha=0.7, label="Top 5% Homes")
    plt.xlabel("Square Footage")
    plt.ylabel("Total Value")
    plt.title("Square Footage vs Total Value (Top 5% Highlighted)")
    plt.legend()
    plt.show()
