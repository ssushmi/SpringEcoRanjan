class Marvel_Player:
    Marveldata=[]
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



player1 = Marvel_Player()
player1.set_player_name("Ironman")
player1.set_player_height(182)
player1.set_player_weight(90)
player1.set_player_no_of_games(105)

player2 = Marvel_Player()
player2.set_player_name("Thor")
player2.set_player_height(187)
player2.set_player_weight(120)
player2.set_player_no_of_games(75)

player = Marvel_Player()
player.set_player_name(0 )
player.set_player_height(0 )
player.set_player_weight(0 )
player.set_player_no_of_games(0 )

player3 = Marvel_Player()
player3.set_player_name("Captain America")
player3.set_player_height(184)
player3.set_player_weight(85)
player3.set_player_no_of_games(205)

player4 = Marvel_Player()
player4.set_player_name("SpiderMan")
player4.set_player_height(175)
player4.set_player_weight(75)
player4.set_player_no_of_games(45)

player5 = Marvel_Player()
player5.set_player_name("Hulk")
player5.set_player_height(179)
player5.set_player_weight(290)
player5.set_player_no_of_games(210)

# add players to Marveldata list
Marvel_Player.Marveldata.extend([player1, player2, player3, player4, player5])

for player in Marvel_Player.Marveldata:
    print(f"Name: {player.get_player_name()}, Height: {player.get_player_height()}, Weight: {player.get_player_weight()}, Games Played: {player.get_player_no_of_games()}")
