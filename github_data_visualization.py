import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_language_distribution(data, language):
    """
    Visualize the distribution of programming languages in GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    # Filter repositories by language
    language_data = data[data['Language'].str.lower() == language.lower()]
    
    # Check if there are repositories for the selected language
    if language_data.empty:
        st.write(f"No repositories found for {language.capitalize()}")
    else:
        # Group repositories by language and count the number of repositories per language
        language_counts = language_data['Language'].value_counts()

        # Plot a bar chart
        plt.figure(figsize=(10, 6))
        language_counts.plot(kind='bar')
        plt.xlabel('Language')
        plt.ylabel('Number of Repositories')
        plt.title(f'Number of Repositories for {language.capitalize()}')
        st.pyplot()

# Define other visualization functions with similar modifications to accept the language argument and filter the data based on it.

def visualize_repo_stats(data, language):
    """
    Visualize repository statistics such as stars, forks, watchers, and issues.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    # Filter repositories by language
    language_data = data[data['Language'].str.lower() == language.lower()]
    
    # Check if there are repositories for the selected language
    if language_data.empty:
        st.write(f"No repositories found for {language.capitalize()}")
    else:
        # Plot a bar chart
        plt.figure(figsize=(10, 6))
        language_data[['Stars', 'Forks', 'Watchers', 'Issues']].plot(kind='bar')
        plt.xlabel('Repository')
        plt.ylabel('Count')
        plt.title(f'GitHub Repository Statistics for {language.capitalize()} Repositories')
        plt.xticks(rotation=45, ha='right')
        st.pyplot()

def visualize_repo_stats(data, language):
    """
    Visualize repository statistics such as stars, forks, watchers, and issues.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]
    plt.figure(figsize=(10, 6))
    language_data[['Stars', 'Forks', 'Watchers', 'Issues']].plot(kind='bar')
    plt.xlabel('Repository')
    plt.ylabel('Count')
    plt.title(f'GitHub Repository Statistics for {language.capitalize()} Repositories')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_yearly_trends(data, language):
    """
    Visualize yearly trends in GitHub repository activity.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]
    yearly_counts = language_data['Date'].dt.year.value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    yearly_counts.plot(kind='line', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Number of Repositories')
    plt.title(f'Yearly Trends in GitHub Repositories for {language.capitalize()}')
    st.pyplot()

def visualize_quarterly_trends(data, language):
    """
    Visualize quarterly trends in GitHub repository activity.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]
    quarterly_counts = language_data['Date'].dt.to_period('Q').value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    quarterly_counts.plot(kind='line', marker='o')
    plt.xlabel('Quarter')
    plt.ylabel('Number of Repositories')
    plt.title(f'Quarterly Trends in GitHub Repositories for {language.capitalize()}')
    st.pyplot()

def visualize_correlation_matrix(data, language):
    """
    Visualize the correlation matrix of numerical features in the GitHub repository data.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]
    numerical_features = language_data.select_dtypes(include=['int64', 'float64'])
    correlation_matrix = numerical_features.corr()

    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f'Correlation Matrix of Numerical Features for {language.capitalize()} Repositories')
    st.pyplot()

def visualize_repo_distribution_by_owner(data, language):
    """
    Visualize the distribution of GitHub repositories by owner.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]
    owner_counts = language_data['Owner'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    owner_counts.plot(kind='bar')
    plt.xlabel('Repository Owner')
    plt.ylabel('Number of Repositories')
    plt.title(f'Distribution of GitHub Repositories by Owner (Top 10) for {language.capitalize()}')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_time_series(data, date_column, language):
    """
    Visualize time series data.

    Args:
        data (pd.DataFrame): DataFrame containing time series data.
        date_column (str): Name of the date column in the DataFrame.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]
    language_data[date_column] = pd.to_datetime(language_data[date_column])

    plt.figure(figsize=(10, 6))
    plt.plot(language_data[date_column], language_data['Value'])
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(f'Time Series Data for {language.capitalize()} Repositories')
    plt.xticks(rotation=45, ha='right')
    st.pyplot()

def visualize_repo_stars_distribution(data, language):
    """
    Visualize the distribution of stars for GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]

    plt.figure(figsize=(10, 6))
    sns.histplot(language_data['Stars'], bins=20, kde=True)
    plt.xlabel('Stars')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of Stars for {language.capitalize()} Repositories')
    st.pyplot()

def visualize_repo_watchers_vs_stars(data, language):
    """
    Visualize the relationship between the number of watchers and stars for GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Stars', y='Watchers', data=language_data)
    plt.xlabel('Stars')
    plt.ylabel('Watchers')
    plt.title(f'Number of Watchers vs. Stars for {language.capitalize()} Repositories')
    st.pyplot()

def visualize_repo_issues_vs_stars(data, language):
    """
    Visualize the relationship between the number of issues and stars for GitHub repositories.

    Args:
        data (pd.DataFrame): DataFrame containing GitHub repository data.
        language (str): The programming language to filter repositories.
    """
    language_data = data[data['Language'].str.lower() == language.lower()]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Stars', y='Issues', data=language_data)
    plt.xlabel('Stars')
    plt.ylabel('Issues')
    plt.title(f'Number of Issues vs. Stars for {language.capitalize()} Repositories')
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

def main():
    # Load GitHub repository data
    data = pd.read_csv('github_data.csv')

    # Sidebar for selecting programming language
    language = st.sidebar.selectbox('Select Programming Language', data['Language'].unique())

    # Visualizations based on selected programming language
    visualize_language_distribution(data, language)
    visualize_stars_vs_forks(data, language)
    visualize_repo_stats(data, language)
    visualize_yearly_trends(data, language)
    visualize_quarterly_trends(data, language)
    visualize_correlation_matrix(data, language)
    visualize_repo_distribution_by_owner(data, language)
    visualize_time_series(data, 'Date', language)
    visualize_repo_stars_distribution(data, language)
    visualize_repo_watchers_vs_stars(data, language)
    visualize_repo_issues_vs_stars(data, language)
    visualize_avg_stars_by_language(data)
    visualize_top_languages(data)
    # Call other visualization functions with the language argument

if __name__ == '__main__':
    main()
