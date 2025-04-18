import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from db_config import get_connection

def team_performance_report():
    conn = get_connection()
    df = pd.read_sql("""
        SELECT t.name AS team, COUNT(m.id) AS played,
        SUM(CASE WHEN t.id = m.winner_id THEN 1 ELSE 0 END) AS won
        FROM teams t
        LEFT JOIN matches m ON t.id = m.team1_id OR t.id = m.team2_id
        GROUP BY t.id
    """, conn)

    df["lost"] = df["played"] - df["won"]
    print(df)
    df.plot(x="team", y=["won", "lost"], kind="bar", stacked=True, title="Team Performance")
    plt.ylabel("Matches")
    plt.tight_layout()
    plt.show()
    conn.close()

def player_performance_report():
    conn = get_connection()
    df = pd.read_sql("""
        SELECT p.name, SUM(pp.runs) AS total_runs, SUM(pp.wickets) AS total_wickets
        FROM player_performance pp
        JOIN players p ON pp.player_id = p.id
        GROUP BY p.id
    """, conn)

    print(df.sort_values(by="total_runs", ascending=False).head(5))
    df.set_index("name")[["total_runs", "total_wickets"]].plot(kind="bar", title="Top Player Stats")
    plt.tight_layout()
    plt.show()
    conn.close()

def export_player_stats_to_csv(filename="player_stats.csv"):
    conn = get_connection()
    df = pd.read_sql("""
        SELECT p.name, t.name AS team, SUM(pp.runs) AS total_runs, SUM(pp.wickets) AS total_wickets
        FROM player_performance pp
        JOIN players p ON pp.player_id = p.id
        JOIN teams t ON p.team_id = t.id
        GROUP BY p.id
    """, conn)
    df.to_csv(filename, index=False)
    print(f"Player stats exported to {filename}")
    conn.close()