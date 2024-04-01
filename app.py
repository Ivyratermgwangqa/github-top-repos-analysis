import streamlit as st
from github_data import get_most_starred_repositories
from visualization import plot_language_distribution

def main():
    st.title('GitHub Repository Explorer')

    # Fetch data from GitHub
    repositories = get_most_starred_repositories()

    # Display repository information
    st.subheader('Top Starred Repositories on GitHub')
    st.write(repositories)

    # Extract programming language distribution
    languages = extract_language_distribution(repositories)

    # Plot language distribution
    plot_language_distribution(languages)

if __name__ == "__main__":
    main()
