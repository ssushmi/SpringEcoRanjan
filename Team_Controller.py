import numpy as np
from sklearn.linear_model import LinearRegression
import Marvelmodel
import TeamModel

class Team_Controller:
    def __init__(self):
        self.marvel = Marvelmodel.Marvel_Player().Marveldata
        self.dc = TeamModel.Team_Player().Teamdata
        self.all_players = self.marvel + self.dc

    def mean_median(self):
        heights = [p.get_player_height() for p in self.all_players]
        weights = [p.get_player_weight() for p in self.all_players]
        games = [p.get_player_no_of_games() for p in self.all_players]

        mean_vals = {
            "height": np.mean(heights),
            "weight": np.mean(weights),
            "games_played": np.mean(games)
        }
        median_vals = {
            "height": np.median(heights),
            "weight": np.median(weights),
            "games_played": np.median(games)
        }
        return mean_vals, median_vals
    
    def deviation_std(self):
        heights = [p.get_player_height() for p in self.all_players]
        weights = [p.get_player_weight() for p in self.all_players]

        deviation_vals = {
            "height": np.var(heights),  
            "weight": np.var(weights)
        }
        std_vals = {
            "height": np.std(heights),
            "weight": np.std(weights)
        }
        return deviation_vals, std_vals

    # 3. Linear Regression of weight (x) on games played (y)
    def linear_regression_weight_vs_games(self):
        weights = np.array([p.get_player_weight() for p in self.all_players]).reshape(-1,1)
        games = np.array([p.get_player_no_of_games() for p in self.all_players])

        model = LinearRegression()
        model.fit(weights, games)

        coef = model.coef_[0]
        intercept = model.intercept_

        score = model.score(weights, games)
        return coef, intercept, score   