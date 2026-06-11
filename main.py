teams = {
    "Argentina": {
        "confederation": "CONMEBOL",
        "world_cups": 3
    },
    "Brazil": {
        "confederation": "CONMEBOL",
        "world_cups": 5
    },
    "France": {
        "confederation": "UEFA",
        "world_cups": 2
    }
}

def view_teams():
    print("\nTeams:")
    for team in teams:
        print(team)
def search_team():
    team_name = input("Enter team name: ")

    if team_name in teams:

        print("\nTeam Details")
        print("Name:", team_name)
        print("Confederation:", teams[team_name]["confederation"])
        print("World Cups:", teams[team_name]["world_cups"])

    else:
        print("Team not found.")


while True:
    print("\n=== FOOTBALL TRACKER ===")
    print("1. View Teams")
    print("2. Search Team")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_teams()

    elif choice == "2":
        search_team()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")