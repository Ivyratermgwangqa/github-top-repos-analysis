import pandas as pd
import requests

def fetch_owner(url):
    """
    Fetches the owner of a GitHub repository from its URL.
    
    Args:
        url (str): The URL of the GitHub repository.
    
    Returns:
        str: The owner of the GitHub repository.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-2xx status codes
        data = response.json()
        return data['owner']['login']
    except requests.RequestException as e:
        print(f"Failed to fetch owner for {url}: {e}")
        return None

import pandas as pd

# Sample data
data = {
    'Repository Name': ['project1', 'project2', 'project3'],
    'Description': ['Description of project1', 'Description of project2', 'Description of project3'],
    'Stars': [100, 200, 150],
    'Forks': [50, 100, 80],
    'Watchers': [80, 120, 90],
    'Issues': [10, 20, 15],
    'URL': [],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Language': ['Python', 'JavaScript', 'Java']
}

# Prompt the user to enter URLs
for i in range(len(data['Repository Name'])):
    url = input(f"Enter the URL for project {i+1}: ")
    data['URL'].append(url)

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('github_data.csv', index=False)
