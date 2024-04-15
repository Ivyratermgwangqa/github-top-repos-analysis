import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_language_distribution(data):
    """
    Visualize the distribution of programming languages in GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    # Group repositories by language and count the number of repositories per language
    language_counts = data['Language'].value_counts()

    # Plot a bar chart
    plt.figure(figsize=(10, 6))
    language_counts.plot(kind='bar')
    plt.xlabel('Language')
    plt.ylabel('Number of Repositories')
    plt.title('Number of Repositories by Language')
    st.pyplot()

def visualize_stars_vs_forks(data):
    """
    Visualize the relationship between stars and forks in GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Stars'], data['Forks'])
    plt.xlabel('Stars')
    plt.ylabel('Forks')
    plt.title('Stars vs Forks')
    st.pyplot()

def visualize_repo_stats(data):
    """
    Visualize repository statistics such as stars, forks, watchers, and issues.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    plt.figure(figsize=(10, 6))
    data[['Stars', 'Forks', 'Watchers', 'Issues']].plot(kind='bar')
    plt.xlabel('Repository')
    plt.ylabel('Count')
    plt.title('GitHub Repository Statistics')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_yearly_trends(data):
    """
    Visualize yearly trends in GitHub repository activity.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    # Group by year and count repositories
    yearly_counts = data['Date'].dt.year.value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    yearly_counts.plot(kind='line', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Number of Repositories')
    plt.title('Yearly Trends in GitHub Repositories')
    st.pyplot()

def visualize_quarterly_trends(data):
    """
    Visualize quarterly trends in GitHub repository activity.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    # Group by quarter and count repositories
    quarterly_counts = data['Date'].dt.to_period('Q').value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    quarterly_counts.plot(kind='line', marker='o')
    plt.xlabel('Quarter')
    plt.ylabel('Number of Repositories')
    plt.title('Quarterly Trends in GitHub Repositories')
    st.pyplot()

def visualize_language_distribution(data):
    """
    Visualize the distribution of programming languages in GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    language_counts = data['Language'].value_counts()

    plt.figure(figsize=(10, 6))
    language_counts.plot(kind='bar')
    plt.xlabel('Programming Language')
    plt.ylabel('Number of Repositories')
    plt.title('Distribution of Programming Languages in GitHub Repositories')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_correlation_matrix(data):
    """
    Visualize the correlation matrix of numerical features in the GitHub repository data.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    numerical_features = data.select_dtypes(include=['int64', 'float64'])
    correlation_matrix = numerical_features.corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Numerical Features')
    st.pyplot()

def visualize_repo_distribution_by_owner(data):
    """
    Visualize the distribution of GitHub repositories by owner.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    owner_counts = data['Owner'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    owner_counts.plot(kind='bar')
    plt.xlabel('Repository Owner')
    plt.ylabel('Number of Repositories')
    plt.title('Distribution of GitHub Repositories by Owner (Top 10)')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_time_series(data, date_column):
    """
    Visualize time series data.

    Args:
        data (pd.DataFrame): DataFrame containing time series data.
        date_column (str): Name of the date column in the DataFrame.
    """
    data[date_column] = pd.to_datetime(data[date_column])

    plt.figure(figsize=(10, 6))
    plt.plot(data[date_column], data['Value'])
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Time Series Data')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_repo_stars_distribution(data):
    """
    Visualize the distribution of stars for GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Stars'], bins=20, kde=True)
    plt.xlabel('Stars')
    plt.ylabel('Frequency')
    plt.title('Distribution of Stars for GitHub Repositories')
    st.pyplot()

def visualize_repo_watchers_vs_stars(data):
    """
    Visualize the relationship between the number of watchers and stars for GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Stars', y='Watchers', data=data)
    plt.xlabel('Stars')
    plt.ylabel('Watchers')
    plt.title('Number of Watchers vs. Stars for GitHub Repositories')
    st.pyplot()

def visualize_repo_issues_vs_stars(data):
    """
    Visualize the relationship between the number of issues and stars for GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Stars', y='Issues', data=data)
    plt.xlabel('Stars')
    plt.ylabel('Issues')
    plt.title('Number of Issues vs. Stars for GitHub Repositories')
    st.pyplot()

def visualize_avg_stars_by_language(data):
    """
    Visualize the average number of stars for each programming language in GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
    """
    avg_stars_by_language = data.groupby('Language')['Stars'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=avg_stars_by_language.index, y=avg_stars_by_language.values)
    plt.xlabel('Programming Language')
    plt.ylabel('Average Stars')
    plt.title('Average Stars by Programming Language in GitHub Repositories')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_top_languages(data, n=5):
    """
    Visualize the top N programming languages used in GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        n (int): Number of top languages to visualize.
    """
    top_languages = data['Language'].value_counts().head(n)
    plt.figure(figsize=(10, 6))
    top_languages.plot(kind='bar')
    plt.xlabel('Programming Language')
    plt.ylabel('Number of Repositories')
    plt.title(f'Top {n} Programming Languages in GitHub Repositories')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()
