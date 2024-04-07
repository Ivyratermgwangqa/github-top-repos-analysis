import streamlit as st
from github_data import get_most_starred_repositories
from analysis import (
    analyze_yearly_trends,
    analyze_quarterly_trends,
    perform_regression_analysis,
    conduct_volatility_analysis,
)

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

        if analysis_choice == "Yearly Trends":
            st.subheader("Yearly Trends Analysis")
            # Perform yearly trends analysis
            # Assuming 'data' is the DataFrame containing GitHub repository data
            # Replace 'data' with your actual DataFrame
            yearly_results = analyze_yearly_trends(data)
            st.write(yearly_results)

        elif analysis_choice == "Quarterly Trends":
            st.subheader("Quarterly Trends Analysis")
            # Perform quarterly trends analysis
            # Assuming 'data' is the DataFrame containing GitHub repository data
            # Replace 'data' with your actual DataFrame
            quarterly_results = analyze_quarterly_trends(data)
            st.write(quarterly_results)

        elif analysis_choice == "Regression Analysis":
            st.subheader("Regression Analysis")
            # Perform regression analysis
            # Assuming 'data' is the DataFrame containing GitHub repository data
            # Replace 'data' with your actual DataFrame
            regression_results = perform_regression_analysis(data)
            st.write(regression_results)

        elif analysis_choice == "Volatility Analysis":
            st.subheader("Volatility Analysis")
            # Perform volatility analysis
            # Assuming 'data' is the DataFrame containing GitHub repository data
            # Replace 'data' with your actual DataFrame
            volatility_results = conduct_volatility_analysis(data)
            st.write(volatility_results)

    elif choice == "About":
        st.subheader("About Page")
        st.write("This app is created to analyze GitHub repositories.")
        # Add more content for the About page

if __name__ == "__main__":
    main()
