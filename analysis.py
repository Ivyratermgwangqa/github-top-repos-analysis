# analysis.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def analyze_yearly_trends(data):
    """
    Analyze yearly trends in GitHub repository data.
    
    Args:
        data (DataFrame): DataFrame containing GitHub repository data.
    
    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Extract year from the date column
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    
    # Group by year and calculate mean stars and forks
    yearly_stats = data.groupby('Year').agg({'Stars': 'mean', 'Forks': 'mean'}).reset_index()
    
    # Convert to dictionary
    results = yearly_stats.to_dict(orient='records')
    
    return results

def analyze_quarterly_trends(data):
    """
    Analyze quarterly trends in GitHub repository data.
    
    Args:
        data (DataFrame): DataFrame containing GitHub repository data.
    
    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Extract quarter from the date column
    data['Quarter'] = pd.to_datetime(data['Date']).dt.to_period('Q')
    
    # Group by quarter and calculate median stars and forks
    quarterly_stats = data.groupby('Quarter').agg({'Stars': 'median', 'Forks': 'median'}).reset_index()
    
    # Convert to dictionary
    results = quarterly_stats.to_dict(orient='records')
    
    return results

def perform_regression_analysis(data):
    """
    Perform regression analysis on GitHub repository data.
    
    Args:
        data (DataFrame): DataFrame containing GitHub repository data.
    
    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Prepare data for regression analysis
    X = data['Stars'].values.reshape(-1, 1)
    y = data['Forks'].values
    
    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Get regression coefficients
    coefficient = model.coef_[0]
    intercept = model.intercept_
    r_squared = model.score(X, y)
    
    # Construct results dictionary
    results = {
        'Coefficient': coefficient,
        'Intercept': intercept,
        'R-squared': r_squared
    }
    
    return results

def conduct_volatility_analysis(data):
    """
    Conduct volatility analysis on GitHub repository data.
    
    Args:
        data (DataFrame): DataFrame containing GitHub repository data.
    
    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Placeholder for volatility analysis logic
    pass

# Other analysis functions as needed

def helper_function():
    """
    A helper function to support the analysis operations.
    """
    pass

def calculate_average_stars(repositories):
    """
    Calculate the average number of stars across all repositories.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        float: The average number of stars.
    """
    total_stars = 0
    num_repositories = 0
    
    # Check if 'stars' key exists in each repository
    for repo in repositories:
        if 'stars' in repo:
            total_stars += repo['stars']
            num_repositories += 1
    
    # Calculate average stars
    if num_repositories > 0:
        average_stars = total_stars / num_repositories
    else:
        average_stars = 0
    
    return average_stars

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

# Other analysis functions as needed

# Other analysis functions as needed

def helper_function():
    """
    A helper function to support the analysis operations.
    """
    pass

def calculate_total_forks(repositories):
    """
    Calculates the total number of forks across all repositories.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        int: The total number of forks.
    """
    total_forks = sum(repo['forks'] for repo in repositories)
    return total_forks

def count_repositories_by_language(repositories):
    """
    Counts the number of repositories for each programming language.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        dict: A dictionary mapping programming languages to their repository counts.
    """
    language_counts = {}
    for repo in repositories:
        lang = repo['language']
        if lang:
            language_counts[lang] = language_counts.get(lang, 0) + 1
    return language_counts

# You can add more analysis functions as needed

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
    total_forks = calculate_total_forks(repositories)
    print(f"Total forks: {total_forks}")
    
    language_counts = count_repositories_by_language(repositories)
    print("Repository counts by language:")
    for language, count in language_counts.items():
        print(f"{language}: {count}")
