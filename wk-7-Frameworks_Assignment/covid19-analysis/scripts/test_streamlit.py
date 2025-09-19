import streamlit as st
import pandas as pd

print("Testing Streamlit functionality...")

# Test basic Streamlit components
st.title("COVID-19 Research Explorer Test")
st.write("This is a test of Streamlit functionality")

# Test DataFrame display
sample_df = pd.DataFrame({
    'Category': ['Cases', 'Deaths', 'Recovered'],
    'Count': [1000, 50, 950]
})
st.dataframe(sample_df)

# Test chart
st.bar_chart(sample_df.set_index('Category'))

print("Streamlit test completed successfully!")
