# Update the simple test script

try:
    import pandas as pd
    print("✓ Pandas installed successfully")
    print("Pandas version:", pd.__version__)
except ImportError:
    print("✗ Pandas not installed")

try:
    import matplotlib
    print("✓ Matplotlib installed successfully")
    print("Matplotlib version:", matplotlib.__version__)
except ImportError:
    print("✗ Matplotlib not installed")

try:
    import seaborn as sns
    print("✓ Seaborn installed successfully")
    print("Seaborn version:", sns.__version__)
except ImportError:
    print("✗ Seaborn not installed")

try:
    import streamlit as st
    print("✓ Streamlit installed successfully")
    print("Streamlit version:", st.__version__)
except ImportError:
    print("✗ Streamlit not installed")

print("\nBasic environment test completed!")

