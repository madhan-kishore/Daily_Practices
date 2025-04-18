from db_config import get_connection

def add_player_performance(match_id, player_id, runs, wickets):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO player_performance (match_id, player_id, runs, wickets)
        VALUES (%s, %s, %s, %s)
    """, (match_id, player_id, runs, wickets))
    conn.commit()
    conn.close()