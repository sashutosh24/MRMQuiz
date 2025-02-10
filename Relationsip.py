# Analyzing the relationship between overall ratings and helpful votes
rating_helpful_votes = data.groupby('overall').agg(
    avg_helpful_votes=('helpful_yes', 'mean'),
    avg_total_votes=('total_vote', 'mean'),
    count=('overall', 'size')
).reset_index()

# Plotting average helpful votes by overall rating
plt.figure(figsize=(8, 6))
plt.bar(rating_helpful_votes['overall'], rating_helpful_votes['avg_helpful_votes'], color='lightblue', edgecolor='black')
plt.title('Average Helpful Votes by Overall Rating', fontsize=14)
plt.xlabel('Overall Rating', fontsize=12)
plt.ylabel('Average Helpful Votes', fontsize=12)
plt.xticks(rating_helpful_votes['overall'])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# Plotting average total votes by overall rating
plt.figure(figsize=(8, 6))
plt.bar(rating_helpful_votes['overall'], rating_helpful_votes['avg_total_votes'], color='salmon', edgecolor='black')
plt.title('Average Total Votes by Overall Rating', fontsize=14)
plt.xlabel('Overall Rating', fontsize=12)
plt.ylabel('Average Total Votes', fontsize=12)
plt.xticks(rating_helpful_votes['overall'])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# Distribution of review length
data['review_length'] = data['reviewText'].apply(lambda x: len(str(x)) if pd.notnull(x) else 0)

plt.figure(figsize=(8, 6))
plt.hist(data['review_length'], bins=30, color='mediumseagreen', edgecolor='black', alpha=0.7)
plt.title('Distribution of Review Length', fontsize=14)
plt.xlabel('Review Length (Number of Characters)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Average review length by overall rating
avg_review_length_by_rating = data.groupby('overall')['review_length'].mean()

plt.figure(figsize=(8, 6))
avg_review_length_by_rating.plot(kind='bar', color='goldenrod', edgecolor='black')
plt.title('Average Review Length by Overall Rating', fontsize=14)
plt.xlabel('Overall Rating', fontsize=12)
plt.ylabel('Average Review Length (Characters)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
