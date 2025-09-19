import pandas as pd
import numpy as np
from config import config

# Create realistic sample COVID-19 research data
sample_data = {
    'cord_uid': [f"uid{i:04d}" for i in range(1, 101)],
    'title': [f"COVID-19 Research Study #{i}" for i in range(1, 101)],
    'authors': [f"Researcher {i}; Scientist {i+1}" for i in range(1, 101)],
    'journal': ["Lancet", "BMJ", "Nature", "Science", "JAMA"] * 20,
    'publish_time': pd.date_range('2020-01-01', periods=100, freq='W').strftime('%Y-%m-%d'),
    'abstract': [f"This study examines aspect {i} of COVID-19 transmission and impact." for i in range(1, 101)],
    'url': [f"https://example.com/paper/{i}" for i in range(1, 101)],
    'source_x': ["PubMed", "arXiv", "bioRxiv", "medRxiv"] * 25
}

df = pd.DataFrame(sample_data)

# Add some missing values to make it realistic
df.loc[::10, 'abstract'] = np.nan
df.loc[::15, 'journal'] = np.nan

# Save the sample data
sample_path = config.get_data_path('sample_metadata.csv')
df.to_csv(sample_path, index=False)

print(f"Sample data created at: {sample_path}")
print(f"Dataset shape: {df.shape}")
print("\nSample data preview:")
print(df.head())
