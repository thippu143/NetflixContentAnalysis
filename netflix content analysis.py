# Netflix Content Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Basic info
print("🔍 Dataset shape:", df.shape)
print("\n📄 Column names:", df.columns.tolist())
print("\n🧹 Null values:\n", df.isnull().sum())

# Fill NA values
df['country'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['director'].fillna('Unknown', inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'])

# Extract year and month
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Show distribution of content types
plt.figure(figsize=(6,4))
sns.countplot(x='type', data=df, palette='Set2')
plt.title("Content Type Distribution")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Show top 10 countries with most content
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title("Top 10 Countries with Most Content")
plt.xlabel("Number of Titles")
plt.show()

# Trend of content added over years
plt.figure(figsize=(10,5))
df['year_added'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title("Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")
plt.grid(True)
plt.show()

# Top genres
df['listed_in'].head()
genres = df['listed_in'].str.split(', ').explode()
top_genres = genres.value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='coolwarm')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.show()

# WordCloud for titles
title_words = ' '.join(df['title'])
wordcloud = WordCloud(background_color='black', width=1000, height=500).generate(title_words)

plt.figure(figsize=(15,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Most Common Words in Titles")
plt.show()

# Most frequent directors
top_directors = df['director'].value_counts().drop('Unknown').head(5)
print("\n🎬 Top 5 Directors:\n", top_directors)

# Most frequent actors
actors = df['cast'].str.split(', ').explode()
top_actors = actors.value_counts().drop('Unknown').head(5)
print("\n🎭 Top 5 Actors:\n", top_actors)
