class Team_Player:
    Teamdata=[]
    player_name=""
    height=0.0
    weight=0.0
    number_of_games_played=0

    def set_player_name(self,name):
        self.player_name=name

    def get_player_name(self):
        return self.player_name
    

    def set_player_height(self,height):
        self.height=height

    def get_player_height(self):
        return self.height
    
    def set_player_weight(self,weight):
        self.weight=weight

    def get_player_weight(self):
        return self.weight
    
    def set_player_no_of_games(self,number):
        self.number_of_games_played=number

    def get_player_no_of_games(self):
        return self.number_of_games_played


player1 = Team_Player()
player1.set_player_name("Batman")
player1.set_player_height(180)
player1.set_player_weight(85)
player1.set_player_no_of_games(105)

player2 = Team_Player()
player2.set_player_name("Superman")
player2.set_player_height(189)
player2.set_player_weight(95)
player2.set_player_no_of_games(305)

player3 = Team_Player()
player3.set_player_name("Harvedent")
player3.set_player_height(181)
player3.set_player_weight(75)
player3.set_player_no_of_games(55)

player4 = Team_Player()
player4.set_player_name("Henergy")
player4.set_player_height(176)
player4.set_player_weight(87)
player4.set_player_no_of_games(125)

player5 = Team_Player()
player5.set_player_name("Heralt")
player5.set_player_height(184)
player5.set_player_weight(100)
player5.set_player_no_of_games(145)


# Add players to Teamdata list
Team_Player.Teamdata.extend([player1, player2, player3, player4, player5])

# Print all player names and stats to confirm
for player in Team_Player.Teamdata:
    print(f"Name: {player.get_player_name()}, Height: {player.get_player_height()}, Weight: {player.get_player_weight()}, Games Played: {player.get_player_no_of_games()}")