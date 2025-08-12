
import mysql.connector


class MarvelConnector:
    database_connector = mysql.connector.connect(
           host="localhost",
           user="root",
           password="Sairam@123",
           database="MarvelUniver"
    )
    cur=database_connector.cursor()

    
    def insert_marvel_data(self):
        marvel_team_data = [
            (1, "Ironman", 182, 90, 105),
            (2, "Thor", 187, 120, 75),
            ( 0,  0 , 0  , 0, 0  ),
            (3, "Captain America", 184, 85, 205),
            (4, "Spider Man", 175, 75, 45),
            (5, "Hulk", 179, 290, 210)
        ]
        sql = "INSERT INTO Marvel (S_No, Name, Height_cm, Weight_kg, Games_Played) VALUES (%s, %s, %s, %s, %s)"
        self.cur.executemany(sql, marvel_team_data)
        self.database_connector.commit()
        print("Data inserted successfully.")


    # def insert_marvel(self):
    #     sql = "insert into Marvel value(%s,%s,%s,%s,%s)"
    #     data=(5,"Hulk", 179,290,210)
    #     self.cur.execute(sql,data)
    #     self.database_connector.commit()


    # def display_marvel(self):
    #     fetch_query="select * from Marvel"
    #     self.cur.execute(fetch_query)
    #     result=self.cur.fetchall()
    #     for i in result:
    #         print(i)

    

    #def delete_marvel(self):
        #delete_query="delete from Marvel where S_no=21"
        #self.cur.execute(delete_query)
        #self.database_connector.commit()
       ## print("data deleted")





MarvelConnector().insert_marvel_data()
# MarvelConnector().display_marvel()








