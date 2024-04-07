import matplotlib.pyplot as plt
import pandas as pd
import requests

def get_most_starred_repositories(language='python', limit=10):
    """
    Fetches data about the most starred GitHub repositories for a given programming language.
    
    Args:
        language (str): The programming language for which repositories are to be fetched. Default is 'python'.
        limit (int): The maximum number of repositories to fetch. Default is 10.
    
    Returns:
        list: A list of dictionaries containing information about the most starred repositories.
    """
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc&per_page={limit}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        repositories = []
        for item in data['items']:
            repository = {
                'name': item['name'],
                'url': item['html_url'],
                'description': item['description'],
                'stars': item['stargazers_count'],
                'forks': item['forks_count'],
                'watchers': item['watchers_count'],
                'issues': item['open_issues_count']
            }
            repositories.append(repository)
        return repositories
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")
        return []

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

def fetch_github_user_info(username):
    """
    Fetches information about a GitHub user.
    
    Args:
        username (str): The GitHub username.
    
    Returns:
        dict: A dictionary containing information about the GitHub user.
    """
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch user information. Status code: {response.status_code}")
        return {}

def fetch_user_repositories(username, per_page=10):
    """
    Fetches repositories owned by a GitHub user.
    
    Args:
        username (str): The GitHub username.
        per_page (int): Optional. The number of repositories per page (default: 10).
    
    Returns:
        list: A list of dictionaries containing information about the user's repositories.
    """
    url = f'https://api.github.com/users/{username}/repos?per_page={per_page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch user repositories. Status code: {response.status_code}")
        return []

def visualize_most_used_languages(username, most_used_languages):
    """
    Visualizes the most used programming languages by a GitHub user.
    
    Args:
        username (str): GitHub username.
        most_used_languages (list): List of tuples containing language and its usage count.
    """
    languages, counts = zip(*most_used_languages)
    plt.figure(figsize=(10, 6))
    plt.bar(languages, counts, color='skyblue')
    plt.xlabel('Programming Language')
    plt.ylabel('Usage Count')
    plt.title(f'Most Used Languages by {username}')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage:
    username = 'your_username_here'  # Replace with your GitHub username
    repositories = get_most_starred_repositories(language='python', limit=10)
    plot_repository_stats(repositories)
    user_info = fetch_github_user_info(username)
    user_repos = fetch_user_repositories(username)
    most_used_languages = [('Python', 50), ('JavaScript', 30), ('Java', 20), ('C++', 15)]  # Example data
    visualize_most_used_languages(username, most_used_languages)
