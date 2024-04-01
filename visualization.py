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

if __name__ == "__main__":
    # Example usage:
    repositories = [
        {'name': 'repo1', 'stars': 100, 'forks': 50, 'watchers': 80, 'issues': 10},
        {'name': 'repo2', 'stars': 200, 'forks': 70, 'watchers': 120, 'issues': 20},
        {'name': 'repo3', 'stars': 150, 'forks': 60, 'watchers': 100, 'issues': 15}
    ]
    plot_repository_stats(repositories)
