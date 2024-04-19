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
    menu = ["Home", "Top Repositories", "Analysis", "Visualizations", "About"]  # Add "Visualizations" option
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
        
        # Get user input for programming language
        language = st.sidebar.text_input("Enter programming language", "python")
        
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

    elif choice == "Visualizations":  # Add "Visualizations" option
        st.subheader("Visualization Page")
        st.write("Select visualization options from the sidebar.")

        # Visualization options
        visualization_options = [
            "Language Distribution",
            "Stars vs Forks",
            "Repository Stats",
            "Yearly Trends",
            "Quarterly Trends",
            "Correlation Matrix",
            "Repo Distribution by Owner",
            "Time Series",
            "Repo Stars Distribution",
            "Repo Watchers vs Stars",
            "Repo Issues vs Stars",
            "Average Stars by Language",
            "Top Languages",
            "About"
        ]
        selected_visualizations = st.sidebar.multiselect("Select Visualizations", visualization_options)

        data = load_data()  # Load data

        # Visualizations based on selected options
        if not selected_visualizations:  # If no visualization is selected, show the home page
            st.write("Welcome to the Home page.")

            st.header("Introduction to the App")
            st.write("This Streamlit app analyzes GitHub repositories. Explore the navigation sidebar to access different features and analysis options.")

            st.header("Recent Updates")
            st.write("Check out the latest updates to the app:")
            st.write("- Improved visualization performance.")
            st.write("- Added new analysis options.")
            st.write("- Enhanced user interface.")

            st.header("Tutorial or Getting Started Guide")
            st.write("New to the app? Follow this guide to get started:")
            st.write("1. Choose a programming language from the sidebar.")
            st.write("2. Explore the 'Top Repositories' section to discover popular GitHub projects.")
            st.write("3. Dive into detailed analysis using the 'Analysis' section.")
            st.write("4. Learn more about the app features in the 'About' section.")

            st.header("Featured Analysis")
            st.write("Discover interesting insights from GitHub repository data:")
            st.write("- Trending programming languages.")
            st.write("- Most starred repositories.")
            st.write("- Correlation between stars and forks.")

            st.header("Feedback Form")
            st.write("We value your feedback! Share your thoughts and suggestions:")
            feedback_form = st.text_area("Enter your feedback here:")
            submit_button = st.button("Submit Feedback")
            if submit_button:
                st.write("Thank you for your feedback!")

                st.header("Links to External Resources")
                st.write("Explore more resources related to GitHub repositories and data analysis:")
                st.write("- [GitHub API Documentation](https://developer.github.com/v3/)")
                st.write("- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)")
                st.write("- [Streamlit Documentation](https://docs.streamlit.io/en/stable/index.html)")

                st.header("Contact Information")
                st.write("Need assistance? Contact us:")
                st.write("- Email: contact@example.com")
                st.write("- Twitter: @example_handle")

        else:  # Show selected visualizations
            # Visualizations based on selected options
            if "Language Distribution" in selected_visualizations:
                visualize_language_distribution(data)
            if "Stars vs Forks" in selected_visualizations:
                visualize_stars_vs_forks(data)
            if "Repository Stats" in selected_visualizations:
                visualize_repo_stats(data)
            if "Yearly Trends" in selected_visualizations:
                visualize_yearly_trends(data)
            if "Quarterly Trends" in selected_visualizations:
                visualize_quarterly_trends(data)
            if "Correlation Matrix" in selected_visualizations:
                visualize_correlation_matrix(data)
            if "Repo Distribution by Owner" in selected_visualizations:
                visualize_repo_distribution_by_owner(data)
            if "Time Series" in selected_visualizations:
                visualize_time_series(data, 'Date')
            if "Repo Stars Distribution" in selected_visualizations:
                visualize_repo_stars_distribution(data)
            if "Repo Watchers vs Stars" in selected_visualizations:
                visualize_repo_watchers_vs_stars(data)
            if "Repo Issues vs Stars" in selected_visualizations:
                visualize_repo_issues_vs_stars(data)
            if "Average Stars by Language" in selected_visualizations:
                visualize_avg_stars_by_language(data)
            if "Top Languages" in selected_visualizations:
                visualize_top_languages(data)
            
            elif choice == "About":
                st.subheader("About Page")
                st.write("This Streamlit app is designed for analyzing GitHub repositories. It provides various analysis options and visualizations based on the data obtained from GitHub.")
                
                st.write("Features:")
                st.write("- Top Repositories Analysis: Retrieve and display information about the top repositories on GitHub based on programming language.")
                st.write("- Analysis: Perform different types of analysis such as yearly trends, quarterly trends, regression analysis, and volatility analysis.")
                st.write("- Additional Analysis: Calculate average stars, find the most popular programming language, count repositories by language, and more.")
                st.write("- Data Visualization: Visualize the data using various charts and plots.")
                
                st.write("Technologies Used:")
                st.write("- Streamlit: Used for building the web application and creating an interactive user interface.")
                st.write("- Pandas: Utilized for data manipulation and analysis.")
                st.write("- Matplotlib and Seaborn: Employed for data visualization.")
                st.write("- GitHub API: Access GitHub repositories data for analysis.")

if __name__ == "__main__":
    main()
