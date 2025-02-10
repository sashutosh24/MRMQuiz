import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from textblob import TextBlob

# Setting up visualizations
sns.set(style="whitegrid")

# ---------- Analysis 1: Distribution of Star Ratings ----------
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x='overall', palette='viridis', order=data['overall'].value_counts().index)
plt.title('Distribution of Star Ratings', fontsize=16)
plt.xlabel('Star Rating', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()

# ---------- Analysis 2: Helpfulness Ratio Distribution ----------
data['helpfulness_ratio'] = data['helpful_yes'] / data['total_vote']
data['helpfulness_ratio'] = data['helpfulness_ratio'].fillna(0)  # Handle division by zero

plt.figure(figsize=(8, 5))
sns.histplot(data['helpfulness_ratio'], kde=True, bins=20, color='teal')
plt.title('Distribution of Helpfulness Ratios', fontsize=16)
plt.xlabel('Helpfulness Ratio', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()

# ---------- Analysis 3: Trends in Reviews Over Time ----------
data['reviewTime'] = pd.to_datetime(data['reviewTime'], format='%d-%m-%Y')
reviews_over_time = data.groupby(data['reviewTime'].dt.to_period('M')).size()

plt.figure(figsize=(10, 6))
reviews_over_time.plot(kind='line', marker='o', color='coral')
plt.title('Trend of Reviews Over Time', fontsize=16)
plt.xlabel('Time (Monthly)', fontsize=12)
plt.ylabel('Number of Reviews', fontsize=12)
plt.show()

# ---------- Analysis 4: Top 10 Products by Number of Reviews ----------
top_products = data['asin'].value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('Top 10 Products by Number of Reviews', fontsize=16)
plt.xlabel('Number of Reviews', fontsize=12)
plt.ylabel('Product ID', fontsize=12)
plt.show()

# ---------- Analysis 5: Sentiment Analysis of Reviews ----------
def get_sentiment(text):
    if pd.isna(text):
        return 'Neutral'
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

data['sentiment'] = data['reviewText'].apply(get_sentiment)
sentiment_counts = data['sentiment'].value_counts()

plt.figure(figsize=(8, 5))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='coolwarm')
plt.title('Sentiment Analysis of Reviews', fontsize=16)
plt.xlabel('Sentiment', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()

# ---------- Analysis 6: Word Cloud for Common Words in Reviews ----------
text = " ".join(review for review in data['reviewText'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Review Text', fontsize=16)
plt.show()

# ---------- Analysis 7: Correlation Between Ratings and Helpfulness ----------
plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x='overall', y='helpfulness_ratio', palette='muted')
plt.title('Correlation Between Star Ratings and Helpfulness Ratio', fontsize=16)
plt.xlabel('Star Rating', fontsize=12)
plt.ylabel('Helpfulness Ratio', fontsize=12)
plt.show()

# ---------- Analysis 8: Review Length vs. Star Ratings ----------
data['review_length'] = data['reviewText'].fillna('').apply(len)

plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x='overall', y='review_length', palette='coolwarm')
plt.title('Review Length vs. Star Ratings', fontsize=16)
plt.xlabel('Star Rating', fontsize=12)
plt.ylabel('Review Length (Characters)', fontsize=12)
plt.show()

# ---------- Analysis 9: Top Reviewers by Number of Reviews ----------
top_reviewers = data['reviewerID'].value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_reviewers.values, y=top_reviewers.index, palette='plasma')
plt.title('Top 10 Reviewers by Number of Reviews', fontsize=16)
plt.xlabel('Number of Reviews', fontsize=12)
plt.ylabel('Reviewer ID', fontsize=12)
plt.show()

# ---------- Analysis 10: Review Trends for Top Products ----------
top_product_ids = top_products.index
top_product_reviews = data[data['asin'].isin(top_product_ids)]
top_product_trends = top_product_reviews.groupby([top_product_reviews['reviewTime'].dt.to_period('M'), 'asin']).size().unstack()

top_product_trends.plot(kind='line', figsize=(12, 6), marker='o')
plt.title('Review Trends for Top Products Over Time', fontsize=16)
plt.xlabel('Time (Monthly)', fontsize=12)
plt.ylabel('Number of Reviews', fontsize=12)
plt.legend(title='Product ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
