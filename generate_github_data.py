import pandas as pd

# Sample data with Owner column added
data = {
    'Repository Name': ['project1', 'project2', 'project3'],
    'Description': ['Description of project1', 'Description of project2', 'Description of project3'],
    'Stars': [100, 200, 150],
    'Forks': [50, 100, 80],
    'Watchers': [80, 120, 90],
    'Issues': [10, 20, 15],
    'URL': ['https://github.com/user/project1', 'https://github.com/user/project2', 'https://github.com/user/project3'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Language': ['Python', 'JavaScript', 'Java'],
    'Owner': ['owner1', 'owner2', 'owner3']  # Add owner information here
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('github_data.csv', index=False)
