import streamlit as st
import pandas as pd
from github_data import get_most_starred_repositories
from analysis import (
    analyze_yearly_trends,
    analyze_quarterly_trends,
    perform_regression_analysis,
    calculate_average_stars,
    find_most_popular_language,
    calculate_total_forks,
    count_repositories_by_language,
    conduct_volatility_analysis
)
import matplotlib.pyplot as plt

def load_data():
    """
    Load sample GitHub repository data.
    """
    # Load your data here or use a sample DataFrame for testing
    data = pd.read_csv("github_repos.csv")
    return data

def main():
    st.title("GitHub Repository Analysis")
    st.sidebar.title("Options")

    data = load_data()

    # Sidebar options
    analysis_option = st.sidebar.selectbox("Select Analysis", ["Yearly Trends", "Quarterly Trends", "Regression Analysis", "Volatility Analysis"])
    if analysis_option == "Yearly Trends":
        st.header("Yearly Trends Analysis")
        yearly_results = analyze_yearly_trends(data)
        st.write(yearly_results)
    elif analysis_option == "Quarterly Trends":
        st.header("Quarterly Trends Analysis")
        quarterly_results = analyze_quarterly_trends(data)
        st.write(quarterly_results)
    elif analysis_option == "Regression Analysis":
        st.header("Regression Analysis")
        regression_results = perform_regression_analysis(data)
        st.write(regression_results)
    elif analysis_option == "Volatility Analysis":
        st.header("Volatility Analysis")
        volatility_results = conduct_volatility_analysis(data)
        st.write(volatility_results)

    # Additional analysis
    st.header("Additional Analysis")
    repositories = data.to_dict('records')  # Convert DataFrame to list of dictionaries
    avg_stars = calculate_average_stars(repositories)
    most_popular_language = find_most_popular_language(repositories)
    total_forks = calculate_total_forks(repositories)
    language_counts = count_repositories_by_language(repositories)

    st.write(f"Average Stars: {avg_stars}")
    st.write(f"Most Popular Language: {most_popular_language}")
    st.write(f"Total Forks: {total_forks}")
    st.write("Repository Counts by Language:")
    st.write(language_counts)

    # Data visualization
    st.header("Data Visualization")

    # Plot repository stats
    st.subheader("Repository Stats")
    plot_repository_stats(repositories)

    # Fetch GitHub user info and repositories
    username = st.text_input("Enter GitHub username")
    user_info = fetch_github_user_info(username)
    if user_info:
        st.subheader("GitHub User Info")
        st.write(user_info)
        
        st.subheader("GitHub User Repositories")
        user_repos = fetch_user_repositories(username)
        if user_repos:
            st.write(user_repos)
        else:
            st.write("No repositories found for this user.")

        # Visualize most used languages by the user
        st.subheader("Most Used Languages")
        most_used_languages = [('Python', 50), ('JavaScript', 30), ('Java', 20), ('C++', 15)]  # Example data
        visualize_most_used_languages(username, most_used_languages)

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

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(names, stars, color='skyblue', label='Stars')
    ax.bar(names, forks, color='orange', label='Forks')
    ax.bar(names, watchers, color='green', label='Watchers')
    ax.bar(names, issues, color='red', label='Open Issues')

    ax.set_xlabel('Repository')
    ax.set_ylabel('Count')
    ax.set_title('GitHub Repository Stats')
    ax.set_xticklabels(names, rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()

    return fig

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
from github_data import get_most_starred_repositories
from analysis import (
    analyze_yearly_trends,
    analyze_quarterly_trends,
    perform_regression_analysis,
    calculate_average_stars,
    find_most_popular_language,
    calculate_total_forks,
    count_repositories_by_language
)
import matplotlib.pyplot as plt

def load_data():
    """
    Load sample GitHub repository data.
    """
    # Load your data here or use a sample DataFrame for testing
    data = pd.read_csv("github_repos.csv")
    return data

def main():
    st.title("GitHub Repository Analysis")
    st.sidebar.title("Options")

    data = load_data()

    # Sidebar options
    analysis_option = st.sidebar.selectbox("Select Analysis", ["Yearly Trends", "Quarterly Trends", "Regression Analysis"])
    if analysis_option == "Yearly Trends":
        st.header("Yearly Trends Analysis")
        yearly_results = analyze_yearly_trends(data)
        st.write(yearly_results)
    elif analysis_option == "Quarterly Trends":
        st.header("Quarterly Trends Analysis")
        quarterly_results = analyze_quarterly_trends(data)
        st.write(quarterly_results)
    elif analysis_option == "Regression Analysis":
        st.header("Regression Analysis")
        regression_results = perform_regression_analysis(data)
        st.write(regression_results)

    # Additional analysis
    st.header("Additional Analysis")
    repositories = data.to_dict('records')  # Convert DataFrame to list of dictionaries
    avg_stars = calculate_average_stars(repositories)
    most_popular_language = find_most_popular_language(repositories)
    total_forks = calculate_total_forks(repositories)
    language_counts = count_repositories_by_language(repositories)

    st.write(f"Average Stars: {avg_stars}")
    st.write(f"Most Popular Language: {most_popular_language}")
    st.write(f"Total Forks: {total_forks}")
    st.write("Repository Counts by Language:")
    st.write(language_counts)

    # Data visualization
    st.header("Data Visualization")

    # Plot repository stats
    st.subheader("Repository Stats")
    plot_repository_stats(repositories)

    # Fetch GitHub user info and repositories
    username = st.text_input("Enter GitHub username")
    user_info = fetch_github_user_info(username)
    if user_info:
        st.subheader("GitHub User Info")
        st.write(user_info)
        
        st.subheader("GitHub User Repositories")
        user_repos = fetch_user_repositories(username)
        if user_repos:
            st.write(user_repos)
        else:
            st.write("No repositories found for this user.")

        # Visualize most used languages by the user
        st.subheader("Most Used Languages")
        most_used_languages = [('Python', 50), ('JavaScript', 30), ('Java', 20), ('C++', 15)]  # Example data
        visualize_most_used_languages(username, most_used_languages)

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
    main()
