from db_config import get_connection

def add_player(name, team_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO players (name, team_id) VALUES (%s, %s)", (name, team_id))
    conn.commit()
    conn.close()

def list_players():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT players.id, players.name, teams.name FROM players JOIN teams ON players.team_id = teams.id")
    for (pid, pname, tname) in cur.fetchall():
        print(f"ID: {pid}, Name: {pname}, Team: {tname}")
    conn.close()