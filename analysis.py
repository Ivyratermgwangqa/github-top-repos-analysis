# analysis.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from langdetect import detect

# Sample data
data = [
    {'Name': 'streamlit', 'Description': 'The fastest way to build and share data apps', 'Stars': 15000, 'Forks': 2500, 'Watchers': 20000, 'Issues': 300, 'URL': 'https://github.com/streamlit/streamlit', 'Date': '2024-04-15'},
    {'Name': 'pytorch', 'Description': 'Deep learning framework for fast flexible experimentation', 'Stars': 35000, 'Forks': 5000, 'Watchers': 40000, 'Issues': 500, 'URL': 'https://github.com/pytorch/pytorch', 'Date': '2024-04-15'},
    {'Name': 'tensorflow', 'Description': 'An open-source machine learning framework', 'Stars': 50000, 'Forks': 8000, 'Watchers': 60000, 'Issues': 1000, 'URL': 'https://github.com/tensorflow/tensorflow', 'Date': '2024-04-15'},
    {'Name': 'keras', 'Description': 'Deep Learning for humans', 'Stars': 25000, 'Forks': 4000, 'Watchers': 30000, 'Issues': 400, 'URL': 'https://github.com/keras-team/keras', 'Date': '2024-04-15'},
    {'Name': 'scikit-learn', 'Description': 'Simple and efficient tools for predictive data analysis', 'Stars': 20000, 'Forks': 3000, 'Watchers': 25000, 'Issues': 200, 'URL': 'https://github.com/scikit-learn/scikit-learn', 'Date': '2024-04-15'},
    {'Name': 'matplotlib', 'Description': 'A Python 2D plotting library', 'Stars': 18000, 'Forks': 2000, 'Watchers': 22000, 'Issues': 150, 'URL': 'https://github.com/matplotlib/matplotlib', 'Date': '2024-04-15'},
    {'Name': 'pandas', 'Description': 'Powerful data structures for data manipulation and analysis', 'Stars': 22000, 'Forks': 3500, 'Watchers': 27000, 'Issues': 250, 'URL': 'https://github.com/pandas-dev/pandas', 'Date': '2024-04-15'},
    {'Name': 'numpy', 'Description': 'The fundamental package for scientific computing with Python', 'Stars': 25000, 'Forks': 4000, 'Watchers': 30000, 'Issues': 300, 'URL': 'https://github.com/numpy/numpy', 'Date': '2024-04-15'}
]

# Convert data to DataFrame
df = pd.DataFrame(data)

def detect_language(description):
    try:
        return detect(description)
    except:
        return 'Unknown'

# Add 'Language' column based on 'Description'
df['Language'] = df['Description'].apply(detect_language)


# Print the modified DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('github_data_with_language.csv', index=False)

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
