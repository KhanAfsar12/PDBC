from dbhelper import DBHelper
        

def main():
    db = DBHelper()
    while True:
        print("******************WELCOME*******************")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display new user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()

        try:
            choice = int(input())
            if choice == 1:
                U_Id = int(input("Enter your Id: "))
                U_name = input("Enter your name: ")
                U_phone = input("Enter your phone: ")
                db.insert_user(U_Id,U_name,U_phone)
            elif choice == 2:
                db.fetch_all()
            elif choice == 3:
                U_Id = input("Enter user id which you want to delete")
                db.delete(U_Id)
            elif choice == 4:
                U_Id = int(input("Enter Id of uzer: "))
                U_name = input("Enter new user: ")
                U_phone = input("Enter new phone: ")

                db.update(U_Id, U_name, U_phone)
            elif choice == 5:
                break
            else:
                print("Invalid input! Try again")
        except Exception as e:
            print(e)
            print("Invalid details! try again")

if __name__=="__main__":
    main()














# helper = DBHelper()
# # helper.insert_user(5200, "Ishtiyaque Hussain", "9876543210")
# # helper.insert_user(3306, "Ibrahim ", "3465433443")
# # helper.insert_user(4000, "Hussain", "98987646576")
# # helper.insert_user(2020, "Jibran", "2378972109")
# # helper.insert_user(1098, "Iqbal", "3406411135")

# # helper.fetch_all()

# # helper.delete(3306)
# # helper.delete(1098)

# helper.update(2020, 'Noman', '2345945676')


