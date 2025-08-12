# import TeamModel
# class TeamView:
#     data=TeamModel.Team_Player().Teamdata

#     def get_view(self):
#         print(TeamModel.Team_Player().Teamdata)



from Team_Controller import Team_Controller

class Team_view:
    def __init__(self):
        self.controller = Team_Controller()

    def get_view(self):
        mean_vals, median_vals = self.controller .mean_median()
        print(f"Mean values: {mean_vals}")
        print(f"Median values:  {median_vals}\n")

        # Deviation and Std Dev
        print("Deviation and Standard deviation of height and weight")
        deviation_vals, std_vals = self.controller .deviation_std()
        print("Variance (Deviation squared):", deviation_vals)
        print(f"Standard Deviation: {std_vals}\n")

        # Linear Regression
        coef, intercept, r2,= self.controller .linear_regression_weight_vs_games()
        print(f"Linear Regression Model: games_played = {coef:.2f} * weight + {intercept:.2f}")
        print(f"R-squared score: {r2:.4f}")
