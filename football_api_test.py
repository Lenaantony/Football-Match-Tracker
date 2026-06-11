import requests

API_KEY="bcf4590cebdb4c619fa1cf7b3e371cbe"
headers={"X-Auth-Token":API_KEY}

def get_all_teams():
    response = requests.get("https://api.football-data.org/v4/competitions/2021/teams",headers=headers)
    data=response.json()
    print(data)
    return data["teams"]


def get_team_squad(team_name):
    team=search_team(team_name)
    if team:
        return team["squad"]
    return None


def search_team(name):
    teams=get_all_teams()
    for team in teams:
        if name.lower() in team["name"].lower():
            return team
    return None
