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
    visualize_repo_distribution_by_owner,
    visualize_language_distribution,
    visualize_stars_vs_forks,
    visualize_repo_stats,
    visualize_yearly_trends,
    visualize_quarterly_trends,
    visualize_correlation_matrix,
    visualize_time_series,
    visualize_repo_stars_distribution,
    visualize_repo_watchers_vs_stars,
    visualize_repo_issues_vs_stars,
    visualize_avg_stars_by_language,
    visualize_top_languages
)
# Set page title and favicon
st.set_page_config(page_title="GitHub Top Repos Analysis", page_icon=":chart:")

# Load GitHub repository data
data = pd.read_csv('github_data.csv')

# Sidebar for selecting programming language
language = st.sidebar.selectbox('Select Programming Language', data['Language'].unique())

# Sidebar for entering GitHub username or access token
github_username = st.sidebar.text_input('Enter GitHub Username or Access Token')

# Visualize distribution of GitHub repositories by owner
visualize_repo_distribution_by_owner(data, language)

# Load sample GitHub repository data
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

def about_page():
    """
    Render the About page.
    """
    st.header("About Page")
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
    
    st.write("Created by [Lerato Mgwangqa]")
    st.write("GitHub Repository: [https://github.com/Ivyratermgwangqa/github-top-repos-analysis.git]")

def main():
    # Load GitHub repository data
    data = pd.read_csv('github_data.csv')

    # Sidebar for selecting programming language
    language = st.sidebar.selectbox('Select Programming Language', data['Language'].unique())

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

    # Visualizations based on selected options
    if "Language Distribution" in selected_visualizations:
        visualize_language_distribution(data, language)
    if "Stars vs Forks" in selected_visualizations:
        visualize_stars_vs_forks(data, language)
    if "Repository Stats" in selected_visualizations:
        visualize_repo_stats(data, language)
    if "Yearly Trends" in selected_visualizations:
        visualize_yearly_trends(data, language)
    if "Quarterly Trends" in selected_visualizations:
        visualize_quarterly_trends(data, language)
    if "Correlation Matrix" in selected_visualizations:
        visualize_correlation_matrix(data, language)
    if "Repo Distribution by Owner" in selected_visualizations:
        visualize_repo_distribution_by_owner(data, language)
    if "Time Series" in selected_visualizations:
        visualize_time_series(data, 'Date', language)
    if "Repo Stars Distribution" in selected_visualizations:
        visualize_repo_stars_distribution(data, language)
    if "Repo Watchers vs Stars" in selected_visualizations:
        visualize_repo_watchers_vs_stars(data, language)
    if "Repo Issues vs Stars" in selected_visualizations:
        visualize_repo_issues_vs_stars(data, language)
    if "Average Stars by Language" in selected_visualizations:
        visualize_avg_stars_by_language(data)
    if "Top Languages" in selected_visualizations:
        visualize_top_languages(data)

    # Handle navigation to the About page
    if "About" in selected_visualizations:
        about_page()

    if "Top Repositories" in selected_visualizations:
        st.title("GitHub Top Repos Analysis")
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

    elif not selected_visualizations:  # If no visualization is selected, show the home page
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

if __name__ == "__main__":
    main()
