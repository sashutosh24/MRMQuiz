# Checking the data for time series analysis
if 'reviewTime' in data.columns:
    # Aggregating review counts by month and year for time series analysis
    time_series_data = data.groupby(data['reviewTime'].dt.to_period('M')).size().reset_index(name='review_count')
    time_series_data['reviewTime'] = time_series_data['reviewTime'].dt.to_timestamp()

    # Plotting the time series of review counts
    plt.figure(figsize=(12, 6))
    plt.plot(time_series_data['reviewTime'], time_series_data['review_count'], marker='o', linestyle='-', color='b')
    plt.title('Monthly Review Counts Over Time', fontsize=16)
    plt.xlabel('Time (Months)', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
else:
    print("Time series analysis is not possible as the 'reviewTime' column is missing or not in datetime format.")
