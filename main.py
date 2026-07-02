import bcrypt
import sqlite3
import pandas as pd

from app_model.database import connection
from app_model.users import add_user, get_user
from hashing import generate_hash, is_valid_hash

#hashing using bcrypt
# def generate_hash(psw):
#     byte_psw = psw.encode("utf-8")
#     salt = bcrypt.gensalt()
#     hash = bcrypt.hashpw(byte_psw, salt)
#     return hash.decode("utf-8")


# def is_valid_hash(psw, hash):
#     hash_psw = hash.encode("utf-8")
#     byte_psw = psw.encode("utf-8")
#     is_valid = bcrypt.checkpw(byte_psw, hash_psw)
#     return is_valid

#psw = "Hola456"
#hash = generate_hash(psw)
#new_psw = "Hola456"
#print(is_valid_hash(new_psw, hash))


#user registration
def register_user(connection):
    name = input("Enter your name:")
    password = input("Enter your password:")
    role = input("Enter your role:")

    hash_password = generate_hash(password)
    add_user(connection,name,hash_password,role)

    with open("DATA/users.txt","a") as file:
        file.write(f"{name},{hash_password},{role}\n")
    print("User successfully registered")


#user login
def login_user(connection):
    name = input("Enter your name:")
    password = input("Enter your password:")
    role = input("Enter your role:")

    id, user_name, user_hash, user_role = get_user(connection,name)
    print(f"Welcome {user_name}")
    if name == user_name and is_valid_hash(password,user_hash) and role == user_role:
        return True
    return False

def main():
    while True:
        print("Welcome to system!")
        print("Choose 1 of the following options")
        print("1. Tp Register")
        print("2. To Login")
        print("3. To Exit")

        choice = input (": > ")

        if choice == "1":
            register_user(connection)

        elif choice == "2":
            if login_user(connection):
                print("Logged in successfully!")
            else:
                print("Incorrect Login.Please try again.")

        elif choice == "3":
            print("GoodBye")
            break

if __name__ == "__main__":
    main()

#create table
#
# connection = sqlite3.connect("DATA/project_data.db")

# def create_user_table(connection):
#     cur = connection.cursor()
#     sql = '''CREATE TABLE users (
#     id            INTEGER PRIMARY KEY AUTOINCREMENT,
#     username      TEXT    NOT NULL UNIQUE,
#     password_hash TEXT    NOT NULL,
#     role          TEXT    DEFAULT 'user');
#     '''
#     cur.execute(sql)
#     connection.commit()


# #Adding data
# def add_user(connection, name, hash, role):
#     cur = connection.cursor()
#     sql = '''INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)'''
#     parametres = (name, hash, role)
#     cur.execute(sql, parametres)
#     connection.commit()
    
# def migrate_users(connection):
#     with open("DATA/users.txt","r") as file:
#         users = file.readlines()

#     for user in users:
#         name, hash, role = user.strip().split(",")
#         add_user(connection, name, hash, role)


# #read data
# def get_all_users(connection):
#     cur = connection.cursor()
#     sql = '''SELECT * FROM users'''
#     cur.execute(sql)
#     users = cur.fetchall()
#     connection.close()
#     return(users)

# def get_user(connection, name):
#     cur   = connection.cursor()
#     sql   = "SELECT * FROM users WHERE username = ?"
#     parametres = (name,)
#     cur.execute(sql, parametres)
#     user = cur.fetchone()
#     connection.close()
#     return(user) 

# def update_user(connection, old_name, new_name):
#     cur   = connection.cursor()
#     sql   = "UPDATE users SET username = ? WHERE username = ?"
#     parametres = (new_name,old_name) 
#     cur.execute(sql, parametres)
#     connection.commit()


# def delete_user(connection, user_name):
#     cur = connection.cursor()
#     sql = 'DELETE FROM users WHERE username = ?'
#     parametres = (user_name,)
#     cur.execute(sql,parametres)
#     connection.commit()

# connection = sqlite3.connect("DATA/project_data.db")
# cur = connection.cursor()
# sql = "UPDATE users SET role = ? WHERE role = ?"
# parametres = ("admin","user")
# cur.execute(sql,parametres)
# connection.commit()
# connection.close()

# def migrate_cyber_incidents(connection):
#     data = pd.read_csv("DATA/cyber_incidents.csv")  
#     data.to_sql("cyber_incidents", connection)

# def migrate_datasets_metadata(connection):
#     data = pd.read_csv("DATA/datasets_metadata.csv")  
#     data.to_sql("datasets_metadata", connection)

# def migrate_it_tickets(connection):
#     data = pd.read_csv("DATA/it_tickets.csv")  
#     data.to_sql("it_tickets", connection)


# def get_all_cyber_incidents(connection):
#     sql = "SELECT * FROM cyber_incidents"
#     data = pd.read_sql(sql,connection)
#     connection.close()
#     return(data)

# def get_all_datasets_metadata(connection):
#     sql = "SELECT * FROM datasets_metadata"
#     data = pd.read_sql(sql,connection)
#     connection.close()
#     return(data)

# def get_all_it_tickets(connection):
#     sql = "SELECT * FROM it_tickets"
#     data = pd.read_sql(sql,connection)
#     connection.close()
#     return(data)

# connection = sqlite3.connect("DATA/project_data.db")
# print(get_all_it_tickets(connection))