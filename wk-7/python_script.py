# 📌 Assignment: Data Analysis & Visualization with Pandas and Matplotlib

# --- Import Libraries ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Task 1: Load and Explore the Dataset ---

try:
    # Load dataset (replace 'your_dataset.csv' with your actual file path)
    df = pd.read_csv("your_dataset.csv")

except FileNotFoundError:
    print("⚠️ Dataset not found! Loading Iris dataset instead.")
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    df = iris.frame  # converts sklearn dataset to DataFrame

# Display first 5 rows
print("📊 First 5 rows of dataset:")
display(df.head())

# Dataset info
print("\nℹ️ Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔍 Missing Values:")
print(df.isnull().sum())

# Handle missing values (fill with mean or drop)
df = df.fillna(df.mean(numeric_only=True))

# --- Task 2: Basic Data Analysis ---

print("\n📈 Summary Statistics:")
display(df.describe())

# Example grouping (adjust based on your dataset)
if "target" in df.columns:  # Iris dataset
    group_col = "target"
else:
    # Pick a categorical column automatically
    group_col = df.select_dtypes(include="object").columns[0]

print(f"\n📊 Grouping by '{group_col}':")
grouped = df.groupby(group_col).mean(numeric_only=True)
display(grouped)

# --- Task 3: Data Visualization ---

# 1️⃣ Line Chart (trend over index or time)
plt.figure(figsize=(8,5))
df.iloc[:, 0].plot(kind='line')
plt.title("Line Chart Example")
plt.xlabel("Index")
plt.ylabel(df.columns[0])
plt.show()

# 2️⃣ Bar Chart (grouped means)
plt.figure(figsize=(8,5))
grouped[df.columns[0]].plot(kind="bar")
plt.title(f"Bar Chart of {df.columns[0]} by {group_col}")
plt.xlabel(group_col)
plt.ylabel(f"Average {df.columns[0]}")
plt.show()

# 3️⃣ Histogram (distribution of a numeric column)
plt.figure(figsize=(8,5))
sns.histplot(df.iloc[:, 0], bins=20, kde=True)
plt.title(f"Histogram of {df.columns[0]}")
plt.xlabel(df.columns[0])
plt.show()

# 4️⃣ Scatter Plot (relationship between two numeric columns)
plt.figure(figsize=(8,5))
sns.scatterplot(x=df.columns[0], y=df.columns[1], data=df, hue=group_col if group_col in df.columns else None)
plt.title(f"Scatter Plot: {df.columns[0]} vs {df.columns[1]}")
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.show()

# --- Findings ---
print("\n🔎 Observations:")
print("1. Numerical features vary across categories.")
print("2. Distribution of values shows patterns that may help classification/regression.")
print("3. Scatter plot suggests correlations between features.")
