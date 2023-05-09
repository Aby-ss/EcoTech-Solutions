import requests

# Step 1: Obtain an API key from the NASA API website
api_key = 'zn7zrliY4VNTpdyFD34bu0NekSxareOwbn75VphA'

# Step 2: Install the requests package
# You can use pip to install it: `pip install requests`

# Step 3: Make a request to the Earth Imagery API
latitude = 40.7128  # Replace with the latitude of the location you want to retrieve the satellite picture for
longitude = -74.0060  # Replace with the longitude of the location you want to retrieve the satellite picture for

url = f'https://api.nasa.gov/planetary/earth/assets?lon={longitude}&lat={latitude}&dim=0.15&api_key={api_key}'
# The `dim` parameter specifies the size of the satellite picture in degrees, with 0.15 being the smallest size available.

response = requests.get(url)
data = response.json()

# Step 4: Print the satellite picture information
print(data[0]['date'])
print(data[0]['url'])