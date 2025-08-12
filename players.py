import mysql.connector

class combined_DB:
    database_connector = mysql.connector.connect(
           host="localhost",
           user="root",
           password="Sairam@123",
           database="MarvelUniver"
    )

    cur=database_connector.cursor()



    def insert_players(self):
        sql = """INSERT INTO Alldata (Name, Height_cm, Weight_kg, Games_played)
        SELECT Name, Height_cm, Weight_kg, Games_played FROM Marvel
        UNION ALL
        SELECT Name, Height_cm, Weight_kg, Games_played FROM Team_DC
        
        """
        try:
            self.cur.execute(sql)
            self.database_connector.commit()
            print("Combined players inserted into Alldata using UNION.")
        except Exception as e:
            print("Error inserting players:", e)

    

    def display_players(self):
        dis_sql="Select * FROM Alldata"
        self.cur.execute(dis_sql)
        result =self.cur.fetchall()
        for i in result:
            print(i)


    def delete_players(self):
        delete_query="delete from Alldata"
        self.cur.execute(delete_query)
        self.database_connector.commit()
       # print("data deleted")


db = combined_DB()
db.insert_players()
# db.display_players()
# db.delete_players()
