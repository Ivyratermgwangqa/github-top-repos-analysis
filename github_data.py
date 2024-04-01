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

if __name__ == "__main__":
    # Example usage:
    repositories = get_most_starred_repositories(language='python', limit=10)
    for repo in repositories:
        print(repo)
