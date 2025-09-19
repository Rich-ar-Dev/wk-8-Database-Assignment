import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Set style for plots
plt.style.use('default')
sns.set_palette("husl")

def analyze_data(df):
    print("Analyzing data...")
    
    # Analysis 1: Count papers by publication year
    yearly_counts = df['publication_year'].value_counts().sort_index()
    
    # Analysis 2: Top journals
    top_journals = df['journal'].value_counts().head(10)
    
    # Analysis 3: Most frequent words in titles
    print("Analyzing word frequencies...")
    all_titles = ' '.join(df['title'].dropna().astype(str))
    words = re.findall(r'\b[a-zA-Z]+\b', all_titles.lower())
    # Remove common stop words
    stop_words = {'the', 'and', 'of', 'in', 'to', 'a', 'for', 'on', 'with', 'by', 
                 'an', 'as', 'at', 'from', 'is', 'are', 'that', 'this', 'was', 'were',
                 'study', 'research', 'analysis', 'using', 'based', 'results', 'method'}
    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
    word_freq = Counter(filtered_words).most_common(20)
    
    return yearly_counts, top_journals, word_freq

def create_visualizations(df, yearly_counts, top_journals, word_freq):
    print("Creating visualizations...")
    
    # Visualization 1: Publications over time
    plt.figure(figsize=(10, 6))
    plt.bar(yearly_counts.index.astype(str), yearly_counts.values)
    plt.title('Number of COVID-19 Publications by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/publications_by_year.png')
    plt.close()
    
    # Visualization 2: Top journals
    plt.figure(figsize=(10, 6))
    top_journals.plot(kind='bar')
    plt.title('Top 10 Journals Publishing COVID-19 Research')
    plt.xlabel('Journal')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('images/top_journals.png')
    plt.close()
    
    # Visualization 3: Word cloud of titles
    all_titles = ' '.join(df['title'].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of COVID-19 Paper Titles')
    plt.tight_layout()
    plt.savefig('images/title_wordcloud.png')
    plt.close()
    
    # Visualization 4: Distribution of paper counts by source
    source_counts = df['source_x'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    source_counts.plot(kind='bar')
    plt.title('Top 10 Sources of COVID-19 Publications')
    plt.xlabel('Source')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('images/top_sources.png')
    plt.close()
    
    # Visualization 5: Most frequent words bar chart
    words, counts = zip(*word_freq)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title('Top 20 Most Frequent Words in COVID-19 Paper Titles')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('images/top_words.png')
    plt.close()
    
    print("Visualizations saved to images/ directory")

if __name__ == "__main__":
    try:
        df = pd.read_csv('data/cleaned_metadata.csv')
        yearly_counts, top_journals, word_freq = analyze_data(df)
        create_visualizations(df, yearly_counts, top_journals, word_freq)
        print("Analysis complete!")
        
    except FileNotFoundError:
        print("Error: cleaned_metadata.csv not found. Please run data_cleaning.py first.")