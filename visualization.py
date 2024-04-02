import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

def plot_repository_stats(repositories):
    """
    Plots a bar chart of the number of stars, forks, watchers, and open issues for each repository.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    """
    names = [repo['name'] for repo in repositories]
    stars = [repo['stars'] for repo in repositories]
    forks = [repo['forks'] for repo in repositories]
    watchers = [repo['watchers'] for repo in repositories]
    issues = [repo['issues'] for repo in repositories]

    plt.figure(figsize=(10, 6))
    plt.bar(names, stars, color='skyblue', label='Stars')
    plt.bar(names, forks, color='orange', label='Forks')
    plt.bar(names, watchers, color='green', label='Watchers')
    plt.bar(names, issues, color='red', label='Open Issues')

    plt.xlabel('Repository')
    plt.ylabel('Count')
    plt.title('GitHub Repository Stats')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()

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
    repositories = [
        {'name': 'repo1', 'stars': 100, 'forks': 50, 'watchers': 80, 'issues': 10},
        {'name': 'repo2', 'stars': 200, 'forks': 70, 'watchers': 120, 'issues': 20},
        {'name': 'repo3', 'stars': 150, 'forks': 60, 'watchers': 100, 'issues': 15}
    ]
    plot_repository_stats(repositories)
