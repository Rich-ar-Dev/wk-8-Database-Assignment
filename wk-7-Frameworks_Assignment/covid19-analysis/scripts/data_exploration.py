import pandas as pd
import numpy as np
from config import config
import os

# Get file paths from config
FILE_PATH = config.get_data_path(config.RAW_DATA_FILE)

print(f"Loading {FILE_PATH}...")
print(f"Project: {config.PROJECT_NAME} v{config.PROJECT_VERSION}")

# Check if file exists
if not os.path.exists(FILE_PATH):
    print(f"Error: {FILE_PATH} not found.")
    print("Creating sample data...")
    
    # Try to create sample data
    try:
        import create_sample_data
        print("Sample data created successfully")
    except:
        print("Could not create sample data. Please run create_sample_data.py first")
    exit()

try:
    # Try to read the file
    try:
        df = pd.read_csv(FILE_PATH, on_bad_lines='skip', encoding='utf-8')
    except:
        df = pd.read_csv(FILE_PATH, on_bad_lines='skip', encoding='latin-1')
    
    print("File loaded successfully!")
    
    # Basic exploration
    print(f"Dataset dimensions: {df.shape}")
    print("\nFirst few rows:")
    print(df.head())
    
    print("\nColumn names:")
    print(df.columns.tolist())
    
    print("\nData types:")
    print(df.dtypes)
    
    print("\nMissing values in each column:")
    print(df.isnull().sum())
    
    # Save the cleaned data for future use
    cleaned_path = config.get_data_path(config.CLEANED_DATA_FILE)
    df.to_csv(cleaned_path, index=False)
    print(f"\nCleaned data saved to: {cleaned_path}")

except Exception as e:
    print(f"Error loading file: {e}")
    print("The file may be corrupted or in wrong format")

print("\nExploration completed!")
