import Marvelmodel
import TeamModel
import math
import numpy as np
import mysql.connector


class Marvel_Controller:
    def __init__(self):
        self.marvel = Marvelmodel.Marvel_Player().Marveldata
        self.dc = TeamModel.Team_Player().Teamdata

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sairam@123",
            database="MarvelUniver"
        )
        self.cur = self.db_connection.cursor()

#1.1 Implement a python code that finds the probability of selection of 2 from Marvel and 3 from DC teams.
    def probability(self, m, d):
        total_ways = math.comb(len(self.marvel) + len(self.dc), m + d)
        favorable_ways = math.comb(len(self.marvel), m) * math.comb(len(self.dc), d)
        return favorable_ways / total_ways

#1.2 List all those stars who are heavier than SpiderMan and taller than Henery
    def heavier_taller_stars(self):
        spiderman_weight = next(p.get_player_weight() for p in self.marvel if p.get_player_name() == "SpiderMan")
        henergy_height = next(p.get_player_height() for p in self.dc if p.get_player_name() == "Henergy")
        return [
            p.get_player_name() for p in self.marvel + self.dc 
            if p.get_player_weight() > spiderman_weight and p.get_player_height() > henergy_height]
    
#1.3 List all those stars who have played more than 100 games and are heavier than Captain America.
    def games_and_heavy(self):
        captain_weight = next(p.get_player_weight() for p in self.marvel if p.get_player_name() == "Captain America")
        return [
            p.get_player_name() for p in self.marvel + self.dc
            if p.number_of_games_played > 100 and p.get_player_weight() > captain_weight
        ]

# 1.4 ) For the given dataset representing stars from the Marvel and DC teams, if a metaverse is to be formed where the summation of the stats (height, weight, and
#games played) of any star is greater than 350 units, then display the names of all the stars meeting this criterion.

    def metaverse_stars(self):
        return [
            p.get_player_name()  for p in self.marvel + self.dc
            if (p.get_player_height() + p.get_player_weight() + p.number_of_games_played) > 350
        ]
    

#1.5) To store all data
    def new_db(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS final_team (
            S_no INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(50),
            Height_cm FLOAT,
            Weight_kg FLOAT,
            Games_Played INT
        )
        """
        self.cur.execute(create_table_sql)
         # Insert all players
        insert_sql = "INSERT INTO final_team (Name, Height_cm, Weight_kg, Games_Played) VALUES (%s, %s, %s, %s)"
        
        for p in self.marvel + self.dc:
            data = (p.get_player_name(), p.get_player_height(), p.get_player_weight(), p.get_player_no_of_games())
            self.cur.execute(insert_sql, data)
        
        self.db_connection.commit()
        print("All players are inserted into the database.")
    
