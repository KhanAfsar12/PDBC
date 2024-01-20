import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost", port=3306, user='root', password='root', database='pythontest')
        query = "create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")


    # Insert query
    def insert_user(self, userid, username, phone):
        query = "Insert into user(userId, userName, phone) values({}, '{}', '{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to db") 

helper = DBHelper()
helper.insert_user(5200, "Ishtiyaque Hussain", "9876543210")
helper.insert_user(3306, "Ibrahim ", "3465433443")
helper.insert_user(4000, "Hussain", "98987646576")
helper.insert_user(2020, "Jibran", "2378972109")
helper.insert_user(1098, "Iqbal", "3406411135")
