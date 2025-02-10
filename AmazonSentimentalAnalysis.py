from textblob import TextBlob

# Performing sentiment analysis on the 'reviewText' column
data['review_sentiment'] = data['reviewText'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity if pd.notnull(x) else 0
)

# Categorizing sentiment into positive, neutral, and negative
data['sentiment_category'] = data['review_sentiment'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)

# Aggregating sentiment distribution
sentiment_distribution = data['sentiment_category'].value_counts()

# Sentiment category proportions
plt.figure(figsize=(8, 6))
sentiment_distribution.plot(kind='bar', color=['green', 'gray', 'red'], edgecolor='black')
plt.title('Sentiment Distribution of Reviews', fontsize=14)
plt.xlabel('Sentiment Category', fontsize=12)
plt.ylabel('Number of Reviews', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# Sentiment analysis summary statistics
sentiment_summary = data.groupby('sentiment_category')['review_sentiment'].agg(['mean', 'count'])

tools.display_dataframe_to_user(name="Sentiment Analysis Summary", dataframe=sentiment_summary)
