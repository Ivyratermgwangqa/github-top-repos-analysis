import streamlit as st
import pandas as pd
from datetime import datetime
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
from github_data_visualization import (
    visualize_language_distribution,
    visualize_stars_vs_forks,
    visualize_repo_stats,
    visualize_yearly_trends,
    visualize_quarterly_trends,
    visualize_correlation_matrix,
    visualize_repo_distribution_by_owner,
    visualize_time_series,
    visualize_repo_stars_distribution,
    visualize_repo_watchers_vs_stars,
    visualize_repo_issues_vs_stars,
    visualize_avg_stars_by_language,
    visualize_top_languages
)

# Disable the PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    """
    Load sample GitHub repository data.
    """
    # Get current date
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Load your data here or use a sample DataFrame for testing
    data = pd.read_csv("github_repos.csv")
    
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])  # No need to specify format
    
    # Print data types of all columns
    print(data.dtypes)
    
    return data

def main():
    # Set page title and favicon
    st.set_page_config(page_title="GitHub Top Repos Analysis", page_icon=":chart:")

    # Add title and description
    st.title("GitHub Top Repos Analysis")
    st.write("This app analyzes GitHub repositories.")

    # Add navigation sidebar
    menu = ["Home", "Top Repositories", "Analysis", "About"]
    choice = st.sidebar.selectbox("Navigation", menu)

    # Handle navigation choices
    if choice == "Home":
        st.write("Welcome to the Home page.")
        # Add content for the Home page

    elif choice == "Top Repositories":
        st.subheader("Top Repositories Analysis")
        language = st.sidebar.text_input("Enter programming language", "python")
        limit = st.sidebar.slider("Select number of repositories", 1, 100, 10)
        repositories = get_most_starred_repositories(language, limit)
        if repositories:
            st.write("Top Repositories:")
            for repo in repositories:
                st.write(f"Name: {repo['name']}")
                st.write(f"Description: {repo['description']}")
                st.write(f"Stars: {repo['stars']}")
                st.write(f"Forks: {repo['forks']}")
                st.write(f"Watchers: {repo['watchers']}")
                st.write(f"Issues: {repo['issues']}")
                st.write("---")
        else:
            st.write("No repositories found.")

    elif choice == "Analysis":
        st.subheader("Analysis Page")
        st.write("Select analysis options from the sidebar.")

        # Add content for the Analysis page
        analysis_options = ["Yearly Trends", "Quarterly Trends", "Regression Analysis", "Volatility Analysis"]  # Update analysis options
        analysis_choice = st.sidebar.selectbox("Select Analysis Option", analysis_options)

        data = load_data()

        if analysis_choice == "Yearly Trends":
            st.header("Yearly Trends Analysis")
            visualize_yearly_trends(data)
            yearly_results = analyze_yearly_trends(data)
            st.write(yearly_results)
        elif analysis_choice == "Quarterly Trends":
            st.header("Quarterly Trends Analysis")
            visualize_quarterly_trends(data)
            quarterly_results = analyze_quarterly_trends(data)
            st.write(quarterly_results)
        elif analysis_choice == "Regression Analysis":
            st.header("Regression Analysis")
            visualize_correlation_matrix(data)
            regression_results = perform_regression_analysis(data)
            st.write(regression_results)
        elif analysis_choice == "Volatility Analysis":
            st.header("Volatility Analysis")
            visualize_time_series(data, 'Date')
            volatility_results = conduct_volatility_analysis(data)
            st.write(volatility_results)

        # Additional analysis
        st.header("Additional Analysis")
        if not data.empty:
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
            
            # Visualize additional analysis
            st.subheader("Additional Analysis Visualizations")
            visualize_language_distribution(data)
            visualize_stars_vs_forks(data)
            visualize_repo_stats(data)
            visualize_correlation_matrix(data)
            visualize_repo_distribution_by_owner(data)
            visualize_repo_stars_distribution(data)
            visualize_repo_watchers_vs_stars(data)
            visualize_repo_issues_vs_stars(data)
            visualize_avg_stars_by_language(data)
            visualize_top_languages(data)
        else:
            st.write("No data available for additional analysis.")

    elif choice == "About":
        st.subheader("About Page")
        st.write("This app is created to analyze GitHub repositories.")
        # Add more content for the About page

if __name__ == "__main__":
    main()
