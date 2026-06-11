import json
from football_api_test import search_team
from football_api_test import get_all_teams
from football_api_test import get_team_squad

def view_teams():
    teams=get_all_teams()
    print("\nTeams:")
    for i,team in enumerate(teams,1):
        print(f"{i}.{team['name']}")


def search_team_ui():
    team_name = input("Enter team name: ")
    details=search_team(team_name)
    if details:
        print("\nTeam:",details["name"])
        print("\nStadium:",details["venue"])
        print("\nFounded:",details["founded"])
        print("\nCoach:",details["coach"]["name"])
        print("Country:",details["area"]["name"])

        choice=input("\nView players? (y/n):")
        if choice.lower() =="y":
            for i,player in enumerate(details["squad"],1):
                print(f"{i}.{player['name']}|{player['position']}|No:{player.get('number','N/A')}")
    else:
        print("Team not found.")


def favourite_team():
    team_name=input("Enter team name: ")
    team=search_team(team_name)
    if team:
        with open("favourites.json","w")as file:
            json.dump(team,file)
        print("Favourite team saved")
    else:
        print("Team not found")


def view_favourite():
    try:
        with open("favourites.json","r")as file:
           team=json.load(file)
        if team:
            print("\nFavourite Team:")
            print("Team:", team.get("name", "N/A"))
            print("Stadium:", team.get("venue", "N/A"))
            print("Coach:", team.get("coach", {}).get("name", "N/A"))
        else:
           print("No favourite team saved.")
    except FileNotFoundError:
        print("No favourite team saved")
    except json.JSONDecodeError:
        print("Favourite file is corrupted. Please save again.")



while True:
    print("\n=== FOOTBALL MATCH TRACKER ===")
    print("1. View Teams")
    print("2. Search Team")
    print("3. Save Favourite Team")
    print("4. View favourite team")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_teams()

    elif choice == "2":
        search_team_ui()

    elif choice == "3":
        favourite_team()

    elif choice == "4":
        view_favourite()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")