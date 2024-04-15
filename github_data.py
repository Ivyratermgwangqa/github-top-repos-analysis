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
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
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
    except requests.RequestException as e:
        print(f"Failed to fetch repositories: {e}")
        return []

def fetch_github_repositories(language='python', num_repos=10):
    """
    Fetches GitHub repositories based on the specified language and number.
    
    Args:
        language (str): The programming language to filter repositories (default: 'python').
        num_repos (int): The number of repositories to fetch (default: 10).
    
    Returns:
        list: A list of dictionaries containing information about the fetched repositories.
    """
    url = f'https://api.github.com/search/repositories?q=language:{language}&per_page={num_repos}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        data = response.json()
        repositories = []
        for item in data['items']:
            repository = {
                'name': item['name'],
                'description': item['description'],
                'url': item['html_url'],
                'stars': item['stargazers_count'],
                'forks': item['forks_count'],
                'watchers': item['watchers_count'],
                'issues': item['open_issues_count']
            }
            repositories.append(repository)
        return repositories
    except requests.RequestException as e:
        print(f"Failed to fetch repositories: {e}")
        return []

def get_most_used_languages(username):
    """
    Retrieves the most used programming languages by a GitHub user.
    
    Args:
        username (str): The GitHub username.
    
    Returns:
        list: A list of tuples containing the most used languages and their usage count.
    """
    url = f'https://api.github.com/users/{username}/repos'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        repos = response.json()
        languages = {}
        for repo in repos:
            lang = repo['language']
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
        return sorted(languages.items(), key=lambda x: x[1], reverse=True)
    except requests.RequestException as e:
        print(f"Failed to fetch user repositories: {e}")
        return []

def fetch_github_user_info(username):
    """
    Fetches information about a GitHub user.
    
    Args:
        username (str): The GitHub username.
    
    Returns:
        dict: A dictionary containing information about the GitHub user.
    """
    url = f'https://api.github.com/users/{username}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch user information for {username}: {e}")
        return {}

def fetch_repository_info(owner, repo_name):
    """
    Fetches information about a GitHub repository.
    
    Args:
        owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
    
    Returns:
        dict: A dictionary containing information about the GitHub repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo_name}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch repository information for {owner}/{repo_name}: {e}")
        return {}

def fetch_repo_issues(owner, repo_name, state='open', per_page=10):
    """
    Fetches issues of a GitHub repository.
    
    Args:
        owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
        state (str): Optional. The state of the issues ('open', 'closed', or 'all').
        per_page (int): Optional. The number of issues per page (default: 10).
    
    Returns:
        list: A list of dictionaries containing information about the repository issues.
    """
    url = f'https://api.github.com/repos/{owner}/{repo_name}/issues'
    params = {'state': state, 'per_page': per_page}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch repository issues for {owner}/{repo_name}: {e}")
        return []

def fetch_repo_contributors(owner, repo_name):
    """
    Fetches contributors of a GitHub repository.
    
    Args:
        owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
    
    Returns:
        list: A list of dictionaries containing information about the repository contributors.
    """
    url = f'https://api.github.com/repos/{owner}/{repo_name}/contributors'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch repository contributors for {owner}/{repo_name}: {e}")
        return []

def fetch_user_details(username):
    """
    Fetches details of a GitHub user.
    
    Args:
        username (str): The GitHub username.
    
    Returns:
        dict: A dictionary containing details of the GitHub user.
    """
    url = f'https://api.github.com/users/{username}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch user details for {username}: {e}")
        return {}

def fetch_repository_details(owner, repo_name):
    """
    Fetches details of a GitHub repository.
    
    Args:
        owner (str): The owner of the repository.
        repo_name (str): The name of the repository.
    
    Returns:
        dict: A dictionary containing details of the GitHub repository.
    """
    url = f'https://api.github.com/repos/{owner}/{repo_name}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch repository details for {owner}/{repo_name}: {e}")
        return {}

if __name__ == "__main__":
    # Example usage:
    repositories = get_most_starred_repositories(language='python', limit=10)
    for repo in repositories:
        print(repo)
