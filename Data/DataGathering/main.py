# Modules
import requests 
import json
from datetime import datetime

# Function to get competitions from the FIE calendar
def get_competitions(status, gender, weapon, comp_type, level, fromDate, toDate):
	# API endpoint
	URL = 'https://fie.org/competitions/search'
	# Search parameters
	PARAMS = {
		'name': "",
		'status': status,
		'gender': gender,
		'weapon': weapon,
		'type': comp_type,
		'season': "-1",
		'level': level,
		'competitionCategory': "",
		'fromDate': fromDate,
		'toDate': toDate,
		'fetchPage': 1
	} 
	# POST request
	r = requests.post(url = URL, json = PARAMS) 
	# Error if status is not 200
	r.raise_for_status()
	# Items
	return(r.json()['items'])

# Function to get the results of a specific competition
def get_results_of_competition(season, competition_id):
	# API endpoint
	URL = 'https://fie.org/competition/variation/results/search'
	# Search parameters
	PARAMS = {
		'season': season,
		'id': competition_id
	} 
	# POST request
	r = requests.post(url = URL, json = PARAMS) 
	# Error if status is not 200
	r.raise_for_status()
	# Items
	return(r.json()['athletes'])

def add_competition_to_ranking(competition, rankings, regions):
	# Check if link has results available
	if competition['hasResults'] == 0:
		return(rankings)
	# Get results
	results = get_results_of_competition(competition['season'], competition['competitionId'])
	ranking_index = rankings[competition['gender']][competition['weapon']]
	# For every participant update points
	for team_result in results:
		participant = team_result['fencer']['country']
		if participant in ranking_index:
			ranking_index[participant]['total_points'] = ranking_index[participant]['total_points'] + team_result['points']
		else:
			ranking_index[participant] = {
				'total_points': team_result['points'], 
				'region': regions[participant], 
				'competitions': [],
				'flag': team_result['fencer']['flag']
			}
		ranking_index[participant]['competitions'].append({
			'competitionId': competition['competitionId'],
			'season': competition['season'],
			'competitionName': competition['name'],
			'competitionDate': competition['endDate'],
			'competitionLocation': competition['location'],
			'rank': team_result['rank'],
			'points': team_result['points']
		})
	return(rankings)

# Get all competitions
completed_competitions = get_competitions('passed', ['f', 'm'], ['f', 'e', 's'], ['e'], 's', '2019-04-04', datetime.today().strftime('%Y-%m-%d'))
upcoming_competitions = get_competitions('', ['f', 'm'], ['f', 'e', 's'], ['e'], 's', datetime.today().strftime('%Y-%m-%d'), '2020-04-04')
# Initialize rankings
all_rankings = {
	'men': { 'foil': {}, 'epee': {}, 'sabre': {} },
	'women': { 'foil': {}, 'epee': {}, 'sabre': {} }
}
# Initialize regions
with open('Data/DataGathering/regions.json') as json_file:  
    regions = json.load(json_file)
# Calculate updated rankings
for competition in completed_competitions:
	all_rankings = add_competition_to_ranking(competition, all_rankings, regions)
# Save results
with open('Data/completed.json', 'w') as outfile:  
    json.dump(completed_competitions, outfile)
with open('Data/upcoming.json', 'w') as outfile:  
    json.dump(upcoming_competitions, outfile)
with open('Data/rankings.json', 'w') as outfile:  
    json.dump(all_rankings, outfile)



