import streamlit as st
from github_data import get_most_starred_repositories, get_most_used_languages

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
        analysis_options = ["Top Repositories", "Most Used Languages"]  # Update analysis options
        analysis_choice = st.sidebar.selectbox("Select Analysis Option", analysis_options)

        if analysis_choice == "Top Repositories":
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

        elif analysis_choice == "Most Used Languages":
            st.subheader("Most Used Languages Analysis")
            username = st.sidebar.text_input("Enter GitHub username")
            user_languages = get_most_used_languages(username)
            if user_languages:
                st.write("Most Used Languages:")
                for language, count in user_languages:
                    st.write(f"{language}: {count}")
            else:
                st.write("No language data found.")

    elif choice == "About":
        st.subheader("About Page")
        st.write("This app is created to analyze GitHub repositories.")
        # Add more content for the About page

if __name__ == "__main__":
    main()
