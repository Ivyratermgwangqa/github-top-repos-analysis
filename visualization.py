import matplotlib.pyplot as plt

def plot_language_distribution(languages):
    """
    Plots a bar chart showing the distribution of programming languages among repositories.
    
    Args:
        languages (dict): A dictionary containing programming languages as keys and their counts as values.
    """
    plt.figure(figsize=(10, 6))
    languages_sorted = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    langs, counts = zip(*languages_sorted)
    plt.bar(langs, counts, color='skyblue')
    plt.xlabel('Programming Language')
    plt.ylabel('Number of Repositories')
    plt.title('Distribution of Programming Languages')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
visualize_repo_stars(repo_df):
plot_sentiment_pie_chart(sentiment_df):
visualize_most_used_languages(username, most_used_languages):
if __name__ == "__main__":
    # Example usage:
    languages = {'Python': 50, 'JavaScript': 30, 'Java': 20, 'C++': 15}
    plot_language_distribution(languages)
