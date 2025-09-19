import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter

# Set page configuration
st.set_page_config(
    page_title="COVID-19 Research Explorer",
    page_icon=":microscope:",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/cleaned_metadata.csv')

# Title and description
st.title("COVID-19 Research Explorer")
st.write("Interactive exploration of COVID-19 research papers from the CORD-19 dataset")

try:
    df = load_data()
    
    # Sidebar with filters
    st.sidebar.header("Filters")
    min_year, max_year = int(df['publication_year'].min()), int(df['publication_year'].max())
    year_range = st.sidebar.slider(
        "Select publication year range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Filter data based on selection
    filtered_df = df[(df['publication_year'] >= year_range[0]) & (df['publication_year'] <= year_range[1])]

    # Display basic statistics
    st.header("Dataset Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Papers", len(filtered_df))
    col2.metric("Date Range", f"{year_range[0]} - {year_range[1]}")
    col3.metric("Average Title Length", f"{filtered_df['title_word_count'].mean():.1f} words")

    # Tabs for different visualizations
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Publications Over Time", 
        "Top Journals", 
        "Word Analysis", 
        "Top Sources",
        "Sample Data"
    ])

    with tab1:
        st.header("COVID-19 Publications Over Time")
        yearly_counts = filtered_df['publication_year'].value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(yearly_counts.index.astype(str), yearly_counts.values)
        ax.set_title('Number of COVID-19 Publications by Year')
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Publications')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with tab2:
        st.header("Top Journals Publishing COVID-19 Research")
        top_journals = filtered_df['journal'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        top_journals.plot(kind='bar', ax=ax)
        ax.set_title('Top 10 Journals by Number of COVID-19 Publications')
        ax.set_xlabel('Journal')
        ax.set_ylabel('Number of Publications')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    with tab3:
        st.header("Word Analysis of COVID-19 Paper Titles")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Word Cloud")
            all_titles = ' '.join(filtered_df['title'].dropna().astype(str))
            wordcloud = WordCloud(width=400, height=300, background_color='white').generate(all_titles)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            ax.set_title('Word Cloud of COVID-19 Paper Titles')
            st.pyplot(fig)
        
        with col2:
            st.subheader("Most Frequent Words")
            words = re.findall(r'\b[a-zA-Z]+\b', all_titles.lower())
            stop_words = {'the', 'and', 'of', 'in', 'to', 'a', 'for', 'on', 'with', 'by', 
                         'an', 'as', 'at', 'from', 'is', 'are', 'that', 'this', 'was', 'were',
                         'study', 'research', 'analysis', 'using', 'based', 'results', 'method'}
            filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
            word_freq = Counter(filtered_words).most_common(15)
            
            words, counts = zip(*word_freq)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.barh(words, counts)
            ax.set_title('Top 15 Words in COVID-19 Paper Titles')
            ax.set_xlabel('Frequency')
            st.pyplot(fig)

    with tab4:
        st.header("Top Sources of COVID-19 Publications")
        source_counts = filtered_df['source_x'].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        source_counts.plot(kind='bar', ax=ax)
        ax.set_title('Top 10 Sources of COVID-19 Publications')
        ax.set_xlabel('Source')
        ax.set_ylabel('Number of Publications')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)

    with tab5:
        st.header("Sample COVID-19 Research Papers")
        st.dataframe(filtered_df[['title', 'journal', 'publication_year', 'abstract_word_count']].head(20))

except FileNotFoundError:
    st.error("Error: cleaned_metadata.csv not found. Please run data_cleaning.py first.")

# Footer
st.markdown("---")
st.markdown("COVID-19 Research Dataset Analysis | Created with Streamlit")