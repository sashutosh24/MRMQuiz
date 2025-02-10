# Sentiment Category Distribution Pie Chart
plt.figure(figsize=(8, 6))
sentiment_distribution.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=140,
    colors=['#4CAF50', '#FFC107', '#F44336'],
    labels=['Positive', 'Neutral', 'Negative'],
    explode=(0.1, 0, 0.1)
)
plt.title('Sentiment Category Distribution', fontsize=14)
plt.ylabel('')  # Hide y-axis label for a cleaner pie chart
plt.show()

# Average Sentiment Score by Overall Rating
avg_sentiment_by_rating = data.groupby('overall')['review_sentiment'].mean()

plt.figure(figsize=(8, 6))
avg_sentiment_by_rating.plot(kind='bar', color='cornflowerblue', edgecolor='black')
plt.title('Average Sentiment Score by Overall Rating', fontsize=14)
plt.xlabel('Overall Rating', fontsize=12)
plt.ylabel('Average Sentiment Score', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# Sentiment Score Distribution (Histogram)
plt.figure(figsize=(8, 6))
plt.hist(data['review_sentiment'], bins=30, edgecolor='black', alpha=0.7, color='mediumorchid')
plt.title('Sentiment Score Distribution', fontsize=14)
plt.xlabel('Sentiment Score', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Sentiment Categories vs. CLV
sentiment_clv = data.groupby('sentiment_category')['CLV'].mean()

plt.figure(figsize=(8, 6))
sentiment_clv.plot(kind='bar', color='teal', edgecolor='black')
plt.title('Average CLV by Sentiment Category', fontsize=14)
plt.xlabel('Sentiment Category', fontsize=12)
plt.ylabel('Average CLV', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
