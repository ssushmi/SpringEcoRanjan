# import Marvelmodel

# class MarvelView:
#     data=Marvelmodel.Marvel_Player().Marveldata

#     def get_view(self):
#         print(Marvelmodel.Marvel_Player().Marveldata)

from Marvel_Controller import Marvel_Controller

class MarvelView:
    def __init__(self):
        self.controller = Marvel_Controller()

    def display_all(self):
        print("1. Probability of selecting 2 Marvel and 3 DC:")
        prob = self.controller.probability(2, 3)
        print(f"   → Probability: {prob:.4f}\n")

        print("2. Stars heavier than SpiderMan and taller than Henergy:")
        result = self.controller.heavier_taller_stars()
        print("   →", result, "\n")

        print("3. Stars who played >100 games and are heavier than Captain America:")
        print("   →", self.controller.games_and_heavy(), "\n")

        print("4. Metaverse stars (sum of stats > 350):")
        print("   →", self.controller.metaverse_stars(), "\n")

        print("5. New Database")
        print("   →", self.controller.new_db(), "\n")


