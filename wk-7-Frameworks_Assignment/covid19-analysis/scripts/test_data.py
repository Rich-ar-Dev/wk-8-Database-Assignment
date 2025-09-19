import pandas as pd
from config import config

print("Testing data loading...")

# Check if files exist
import os
raw_path = config.get_data_path(config.RAW_DATA_FILE)
cleaned_path = config.get_data_path(config.CLEANED_DATA_FILE)

print(f"Raw data path: {raw_path}")
print(f"Raw data exists: {os.path.exists(raw_path)}")
print(f"Cleaned data path: {cleaned_path}")
print(f"Cleaned data exists: {os.path.exists(cleaned_path)}")

if os.path.exists(raw_path):
    df = pd.read_csv(raw_path)
    print(f"Raw data shape: {df.shape}")
    print("Raw data columns:", df.columns.tolist())

if os.path.exists(cleaned_path):
    df = pd.read_csv(cleaned_path)
    print(f"Cleaned data shape: {df.shape}")
    print("Cleaned data columns:", df.columns.tolist())
