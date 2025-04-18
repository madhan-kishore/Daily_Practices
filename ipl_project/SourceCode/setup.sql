CREATE DATABASE IF NOT EXISTS ipl_analysis;
USE ipl_analysis;

CREATE TABLE IF NOT EXISTS teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS matches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    team1_id INT,
    team2_id INT,
    venue VARCHAR(100),
    winner_id INT,
    match_date DATE,
    FOREIGN KEY (team1_id) REFERENCES teams(id),
    FOREIGN KEY (team2_id) REFERENCES teams(id),
    FOREIGN KEY (winner_id) REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS player_performance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT,
    player_id INT,
    runs INT,
    wickets INT,
    FOREIGN KEY (match_id) REFERENCES matches(id),
    FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE IF NOT EXISTS venues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS umpires (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    nationality VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS match_umpires (
    match_id INT,
    umpire_id INT,
    FOREIGN KEY (match_id) REFERENCES matches(id),
    FOREIGN KEY (umpire_id) REFERENCES umpires(id)
);

CREATE TABLE IF NOT EXISTS team_stats (
    team_id INT PRIMARY KEY,
    matches_played INT DEFAULT 0,
    matches_won INT DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);