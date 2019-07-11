# Modules
from jinja2 import Template
import json
import re

# Read rankings
with open('Data/rankings.json') as json_file:  
    rankings = json.load(json_file)

# Read competitions
with open('Data/completed.json') as json_file:  
    completed_competitions = json.load(json_file)
with open('Data/upcoming.json') as json_file:  
    upcoming_competitions = json.load(json_file)

# Clean competition names
for c in completed_competitions:
    c['name'] = re.sub(r" par.*$", "", c['name'])
    c['name'] = re.sub(r"monde", "Monde", c['name'])
    if not any(ext in c['name'] for ext in ['Monde', 'Championnats']):
        c['name'] = 'Coupe du Monde'
for c in upcoming_competitions:
    c['name'] = re.sub(r" par.*$", "", c['name'])
    c['name'] = re.sub(r"monde", "Monde", c['name'])
    if not any(ext in c['name'] for ext in ['Monde', 'Championnats']):
        c['name'] = 'Coupe du Monde'


# Read and jinjify template
with open('template.html') as template_file:
    template = Template(template_file.read())
template = template.render(
    rankings = rankings, 
    completed_competitions = completed_competitions, 
    upcoming_competitions = upcoming_competitions
)

# Write output html
with open('index.html', 'wb') as output_file:
    output_file.write(template.encode('utf8', 'replace'))
