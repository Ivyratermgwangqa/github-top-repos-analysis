# analysis.py
import pandas as pd
from langdetect import detect
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
    # Calculate the standard deviation of stars over time
    stars_std = data['Stars'].std()
    
    # Determine if the volatility is high or low based on some threshold
    if stars_std > 100:
        volatility_level = "High"
    else:
        volatility_level = "Low"
    
    # Prepare analysis results
    analysis_results = {
        "Stars Volatility": stars_std,
        "Volatility Level": volatility_level
    }
    
    return analysis_results

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
    Find the most popular programming language among the repositories.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        str: The most popular programming language, or "Unknown" if no language information is found.
    """
    language_counts = {}
    
    # Count occurrences of each language
    for repo in repositories:
        if 'language' in repo:
            language = repo['language']
            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1
    
    # Find the most popular language
    if language_counts:
        most_popular_language = max(language_counts, key=language_counts.get)
    else:
        most_popular_language = "Unknown"
    
    return most_popular_language

def helper_function():
    """
    A helper function to support the analysis operations.
    """
    pass

def calculate_total_forks(repositories):
    """
    Calculate the total number of forks across all repositories.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        int: The total number of forks.
    """
    total_forks = 0
    
    # Calculate total forks, skipping repositories without 'forks' information
    for repo in repositories:
        if 'forks' in repo:
            total_forks += repo['forks']
    
    return total_forks
    
def count_repositories_by_language(repositories):
    """
    Count the number of repositories for each programming language.
    
    Args:
        repositories (list): A list of dictionaries containing information about GitHub repositories.
    
    Returns:
        dict: A dictionary where keys are programming languages and values are the corresponding counts.
    """
    language_counts = {}
    
    # Count repositories by language, skipping repositories without 'language' information
    for repo in repositories:
        if 'language' in repo:
            lang = repo['language']
            language_counts[lang] = language_counts.get(lang, 0) + 1
    
    return language_counts
# You can add more analysis functions as needed

if __name__ == "__main__":
    # Example usage with the DataFrame 'data'
    avg_stars = calculate_average_stars(data)
    most_popular_language = find_most_popular_language(data)
    print(f"Average stars: {avg_stars}")
    print(f"Most popular language: {most_popular_language}")
    total_forks = calculate_total_forks(data)
    print(f"Total forks: {total_forks}")
    
    language_counts = count_repositories_by_language(data)
    print("Repository counts by language:")
    for language, count in language_counts.items():
        print(f"{language}: {count}")
        
    # Check if 'Language' column exists and print value counts if it does
    print("\nChecking 'Language' column:")
    if 'Language' in data.columns:
        language_counts = data['Language'].value_counts()
        print(language_counts)
    else:
        print("Error: 'Language' column not found.")
