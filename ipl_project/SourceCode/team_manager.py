
from db_config import get_connection

def add_team(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO teams (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def list_teams():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teams")
    for (id, name) in cur.fetchall():
        print(f"ID: {id}, Name: {name}")
    conn.close()