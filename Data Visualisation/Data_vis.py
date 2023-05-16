from asciichartpy import plot
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress

import time

# Example deforestation data
years = [2018, 2019, 2020, 2021]
deforestation_values = [500, 600, 800, 700]

# Bar chart
chart = plot(deforestation_values, {'height': 10})
console = Console()
console.print(Panel(chart, title="Deforestation Data"))

# Table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Year")
table.add_column("Deforestation")
for year, value in zip(years, deforestation_values):
    table.add_row(str(year), str(value))
console.print(table)

# Progress bar
with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=len(years))
    for year in years:
        progress.update(task, completed=years.index(year) + 1)
        progress.refresh()
        # Simulate processing time
        time.sleep(0.5)
console.print(Panel.fit("Processing complete!", title="[bold green]Status"))

# Rich text
console.print("[bold]Trends and Patterns in Deforestation:")
console.print("[red]• Deforestation has been increasing steadily in recent years.")
console.print("[red]• The highest deforestation value was observed in 2020.")
