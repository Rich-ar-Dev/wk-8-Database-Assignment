import pandas as pd
import numpy as np
from datetime import datetime
from config import config
import os

def clean_data(df):
    # Create a copy to avoid modifying the original
    cleaned_df = df.copy()
    
    # Display initial info
    print(f"Original data shape: {cleaned_df.shape}")
    
    # Handle missing values
    print("\nHandling missing values...")
    
    # Drop rows where title is missing (essential for analysis)
    initial_count = len(cleaned_df)
    cleaned_df = cleaned_df.dropna(subset=['title'])
    print(f"Removed {initial_count - len(cleaned_df)} rows with missing titles")
    
    # Fill missing abstracts with empty string
    if 'abstract' in cleaned_df.columns:
        cleaned_df['abstract'] = cleaned_df['abstract'].fillna('')
        print("Filled missing abstracts with empty strings")
    
    # Convert publish_time to datetime and extract year
    print("Processing publication dates...")
    if 'publish_time' in cleaned_df.columns:
        def parse_date(date_str):
            if pd.isna(date_str):
                return np.nan
            try:
                # Try to parse as full date
                return pd.to_datetime(date_str)
            except:
                try:
                    # Try to parse as year only
                    return pd.to_datetime(str(int(float(date_str))), format='%Y')
                except:
                    return np.nan
        
        cleaned_df['publish_time_parsed'] = cleaned_df['publish_time'].apply(parse_date)
        cleaned_df['publication_year'] = cleaned_df['publish_time_parsed'].dt.year
        print("Added publication year column")
    else:
        # Add a dummy year column if not present
        cleaned_df['publication_year'] = 2020
        print("Added dummy publication year column")
    
    # Create abstract word count column
    if 'abstract' in cleaned_df.columns:
        cleaned_df['abstract_word_count'] = cleaned_df['abstract'].apply(lambda x: len(str(x).split()))
        print("Added abstract word count column")
    
    # Create title word count column
    cleaned_df['title_word_count'] = cleaned_df['title'].apply(lambda x: len(str(x).split()))
    print("Added title word count column")
    
    print(f"Cleaned data shape: {cleaned_df.shape}")
    return cleaned_df

if __name__ == "__main__":
    try:
        # Try to load cleaned data from exploration first
        cleaned_path = config.get_data_path(config.CLEANED_DATA_FILE)
        if os.path.exists(cleaned_path):
            df = pd.read_csv(cleaned_path)
            print("Loaded cleaned data from previous exploration")
        else:
            # If no cleaned data, load raw data
            raw_path = config.get_data_path(config.RAW_DATA_FILE)
            if os.path.exists(raw_path):
                df = pd.read_csv(raw_path)
                print("Loaded raw data")
            else:
                print("No data files found. Creating sample data...")
                # Create sample data
                exec(open('scripts/create_sample_data.py').read())
                df = pd.read_csv(config.get_data_path(config.RAW_DATA_FILE))
        
        cleaned_df = clean_data(df)
        
        # Save cleaned data for later use
        cleaned_df.to_csv(config.get_data_path(config.CLEANED_DATA_FILE), index=False)
        print("Cleaned data saved to data/cleaned_metadata.csv")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Please make sure you have data files or run create_sample_data.py first")
