import requests
from bs4 import BeautifulSoup
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# Dictionary to store user-defined alerts
alerts = {}

# Function to set an alert
def set_alert():
    console = Console()
    console.print("Set Alert")
    criteria = Prompt.ask("Enter the criteria for the alert:")
    message = Prompt.ask("Enter the alert message:")
    alerts[criteria] = message
    console.print(Panel(f"Alert set: {criteria} -> {message}", title="Alert Set"))

# Function to check for alerts
def check_alerts(region, deforestation):
    for criteria, message in alerts.items():
        if criteria.lower() in region.lower() and deforestation:
            console = Console()
            console.print(Panel(f"ALERT: {message}", title="Alert Triggered"))

# URL of deforestation data
url = "https://www.example.com/deforestation-data"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find and extract the relevant data
data = soup.find_all("div", class_="deforestation-entry")

# Set alerts
set_alert()

# Check alerts based on deforestation data
for entry in data:
    region = entry.find("span", class_="region").text.strip()
    deforestation_status = entry.find("span", class_="status").text.strip()
    check_alerts(region, deforestation_status == "Deforestation Detected")
