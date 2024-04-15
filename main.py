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
    analysis_option = st.sidebar.selectbox("Select Analysis", ["Yearly Trends", "Quarterly Trends", "Regression Analysis", "Volatility Analysis", "About"])
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
    elif analysis_option == "About":
        st.subheader("About Page")
        st.write("This app is created to analyze GitHub repositories.")
        # Add more content for the About page

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

if __name__ == "__main__":
    main()
