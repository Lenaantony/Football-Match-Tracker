import requests

API_KEY="bcf4590cebdb4c619fa1cf7b3e371cbe"
headers={"X-Auth-Token":API_KEY}

def get_competitions():
    url = "https://api.football-data.org/v4/competitions"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["competitions"]

def get_all_teams(competition_code):
    url = f"https://api.football-data.org/v4/competitions/{competition_code}/teams"

    response = requests.get(url, headers=headers)

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print("API ERROR RESPONSE:")
        print(response.text)
        return []

    try:
        data = response.json()
        return data.get("teams", [])
    except Exception:
        print("Invalid JSON response:", response.text)
        return []


def get_team_squad(team_name):
    team=search_team(team_name)
    if team:
        return team["squad"]
    return None


def search_team(name, competition_code):
    teams=get_all_teams(competition_code)
    for team in teams:
        if name.lower() in team["name"].lower():
            return team
    return None
