from db_config import get_connection

def record_match(team1_id, team2_id, venue, winner_id, match_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO matches (team1_id, team2_id, venue, winner_id, match_date)
        VALUES (%s, %s, %s, %s, %s)
    """, (team1_id, team2_id, venue, winner_id, match_date))
    conn.commit()
    conn.close()

def list_matches():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT m.id, t1.name, t2.name, m.venue, tw.name, m.match_date
        FROM matches m
        JOIN teams t1 ON m.team1_id = t1.id
        JOIN teams t2 ON m.team2_id = t2.id
        JOIN teams tw ON m.winner_id = tw.id
    """)
    for row in cur.fetchall():
        print(f"Match ID: {row[0]}, {row[1]} vs {row[2]}, Venue: {row[3]}, Winner: {row[4]}, Date: {row[5]}")
    conn.close()