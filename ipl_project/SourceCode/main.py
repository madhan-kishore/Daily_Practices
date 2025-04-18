from team_manager import add_team, list_teams
from player_manager import add_player, list_players
from match_manager import record_match, list_matches
from performance_manager import add_player_performance
from report_manager import team_performance_report, player_performance_report, export_player_stats_to_csv

def menu():
    print("\n--- IPL Team Performance Analysis ---")
    print("1. Add Team")
    print("2. List Teams")
    print("3. Add Player")
    print("4. List Players")
    print("5. Record Match")
    print("6. Record Player Performance")
    print("7. View Match Results")
    print("8. Team Performance Report")
    print("9. Player Performance Report")
    print("10. Export Player Stats to CSV")
    print("0. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Team Name: ")
        add_team(name)
    elif choice == "2":
        list_teams()
    elif choice == "3":
        name = input("Enter Player Name: ")
        team_id = int(input("Enter Team ID: "))
        add_player(name, team_id)
    elif choice == "4":
        list_players()
    elif choice == "5":
        team1_id = int(input("Enter Team 1 ID: "))
        team2_id = int(input("Enter Team 2 ID: "))
        venue = input("Enter Venue: ")
        winner_id = int(input("Enter Winner Team ID: "))
        date = input("Enter Match Date (YYYY-MM-DD): ")
        record_match(team1_id, team2_id, venue, winner_id, date)
    elif choice == "6":
        match_id = int(input("Enter Match ID: "))
        player_id = int(input("Enter Player ID: "))
        runs = int(input("Enter Runs Scored: "))
        wickets = int(input("Enter Wickets Taken: "))
        add_player_performance(match_id, player_id, runs, wickets)
    elif choice == "7":
        list_matches()
    elif choice == "8":
        team_performance_report()
    elif choice == "9":
        player_performance_report()
    elif choice == "10":
        export_player_stats_to_csv()
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")