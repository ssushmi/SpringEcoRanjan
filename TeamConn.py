import mysql.connector


class TeamConnector:
    database_connector = mysql.connector.connect(
           host="localhost",
           user="root",
           password="Sairam@123",
           database="MarvelUniver"
    )
    cur=database_connector.cursor()

    
    def insert_teamdc(self):
        teamdc_data = [
            (1, "Batman", 180, 85, 105),
            (2, "Superman", 189, 95, 305),
            (3, "Harvedent", 81, 75, 55),
            (4, "Henery", 176, 37, 125),
            (5, "Heralt", 184, 200, 145)
        ]
        sql = "INSERT INTO Team_DC (S_No, Name, Height_cm, Weight_kg, Games_Played) VALUES (%s, %s, %s, %s, %s)"
        self.cur.executemany(sql, teamdc_data)
        self.database_connector.commit()
        print("Data inserted successfully.")



    # def insert_teamdc(self):
    #     sql = "insert into Team_DC value(%s,%s,%s,%s,%s)"
    #     data=(5,"Heralt", 184,100,145)
    #     self.cur.execute(sql,data)
    #     self.database_connector.commit()


    # def display_team(self):
    #     fetch_query="select * from Team_DC"
    #     self.cur.execute(fetch_query)
    #     result=self.cur.fetchall()
    #     for i in result:
    #         print(i)

    

    # def delete_team(self):
    #     delete_query="delete from Marvel where S_no=5"
    #     self.cur.execute(delete_query)
    #     self.database_connector.commit()
    #     print("data deleted")

TeamConnector().insert_teamdc()
#TeamConnector().display_team()