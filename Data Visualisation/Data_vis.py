import requests
from rich.console import Console
from rich.table import Table

# Set API endpoint URL
url = 'https://api.spacexdata.com/v4/launches/past'

# Set number of missions to retrieve
num_missions = 10

# Make HTTP request to API
response = requests.get(url)

# Check status code of response
if response.status_code == 200:
    # Parse response data as JSON
    data = response.json()[:num_missions]  # only retrieve the last `num_missions` missions
    # Create table
    table = Table(title=f'Last {num_missions} SpaceX Missions')
    table.add_column('Flight Number', style='cyan', justify='right')
    table.add_column('Mission Name', style='magenta', justify='left')
    table.add_column('Launch Date (UTC)', style='green', justify='left')
    table.add_column('Rocket', style='blue', justify='left')
    table.add_column('Launch Site', style='yellow', justify='left')
    # Add rows to table
    for mission in data:
        flight_number = mission['flight_number']
        mission_name = mission['name']
        launch_date_utc = mission['date_utc']
        rocket_name = mission['rocket']['name']
        launch_site_name = mission['launchpad']['name']
        table.add_row(flight_number, mission_name, launch_date_utc, rocket_name, launch_site_name)
    # Display table
    console = Console()
    console.print(table)
else:
    # Handle error condition
    print(f'Request failed with status code {response.status_code}')
