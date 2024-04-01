def calculate_average_stars(repositories):
    """
    Calculates the average number of stars across all repositories.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        float: The average number of stars.
    """
    total_stars = sum(repo['stars'] for repo in repositories)
    return total_stars / len(repositories)

def find_most_popular_language(repositories):
    """
    Finds the most popular programming language among the repositories.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        str: The most popular programming language.
    """
    languages = {}
    for repo in repositories:
        lang = repo['language']
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
    
    if languages:
        return max(languages, key=languages.get)
    else:
        return "Unknown"

if __name__ == "__main__":
    # Example usage:
    repositories = [
        {'name': 'repo1', 'stars': 100, 'language': 'Python'},
        {'name': 'repo2', 'stars': 200, 'language': 'JavaScript'},
        {'name': 'repo3', 'stars': 150, 'language': 'Python'}
    ]
    avg_stars = calculate_average_stars(repositories)
    most_popular_language = find_most_popular_language(repositories)
    print(f"Average stars: {avg_stars}")
    print(f"Most popular language: {most_popular_language}")
