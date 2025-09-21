# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# -----------------------------
# Load the data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("metadata_sample.csv")
    # Convert dates
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    # Add abstract length
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()

# -----------------------------
# Streamlit App Layout
# -----------------------------
st.title("📊 CORD-19 Research Explorer")
st.write("Simple exploration of COVID-19 research papers (sample dataset)")

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")
year_range = st.sidebar.slider(
    "Select publication year range",
    int(df['year'].min()),
    int(df['year'].max()),
    (2020, 2021)
)

# Filter dataset
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"### Showing {len(filtered_df)} papers published between {year_range[0]} and {year_range[1]}")

# -----------------------------
# Chart 1: Publications by Year
# -----------------------------
st.subheader("Publications over time")
year_counts = filtered_df['year'].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("Publications by Year")
st.pyplot(fig)

# -----------------------------
# Chart 2: Top Journals
# -----------------------------
st.subheader("Top Journals Publishing COVID-19 Research")
top_journals = (
    filtered_df['journal']
    .value_counts()
    .head(10)
)

st.bar_chart(top_journals)

# -----------------------------
# Chart 3: Word Cloud of Titles
# -----------------------------
st.subheader("Word Cloud of Paper Titles")
text = " ".join(filtered_df['title'].dropna().astype(str))
if text:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("No titles available for word cloud.")

# -----------------------------
# Data sample
# -----------------------------
st.subheader("Sample of Data")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'year']].head(20))
