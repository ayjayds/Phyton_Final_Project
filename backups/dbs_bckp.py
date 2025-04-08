###====== IT0011 FINAL PROJECT =======### 
####=== TC24 Feel Good BGYO Store ===#### 
#####===============================#####
###==  Agero, Mikhail Gianmarko G.  ==###
####= Flaviano, Angel Gaebrielle N. =####
####======   Gison, Yuan Ira   ======####
####==   Sanchez, Aaron Joshua D.  ==####

import sqlite3 ### - //Used for database management.//

##========== [USER TABLE DATABASE FUNCTIONS] ==========##
def register_user(name, address, username, password):
    #===== Database User Registration =====# - //Registers users to the database//
    conn = sqlite3.connect("schema/store_management.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM User WHERE Username = ?;", (username,))
    result = cursor.fetchone()[0] 

    if result > 0:
        conn.close()
        return "Error: User already, exists. Please pick another username."

    try:
        cursor.execute("INSERT INTO User (Username, Name, Address, Password) VALUES (?, ?, ?, ?);", (username, name, address, password))
        conn.commit()
        conn.close()
        return "User account successfully created."
    except sqlite3.IntegrityError:
        conn.close()
        return "Error: User already, exists. Please pick another username."


def verify_user(username, password):
    #===== Database User Veritication =====# - //Verifies login credentials//
    conn = sqlite3.connect("schema/store_management.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM User WHERE Username=? AND Password=?", (username, password))
    result = cursor.fetchone()

    conn.close()
    return result  

def get_user_by_username(username):
    conn = sqlite3.connect("schema/store_management.db")
    c = conn.cursor()
    c.execute("SELECT * FROM User WHERE Username = ?", (username,))
    return c.fetchone()

##========== [ITEM TABLE DATABASE MANAGEMENT FUNCTION] ==========##
def add_item(item_id, name, stock, price, category, image_path):
    conn = sqlite3.connect("schema/store_management.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Items (ItemID, Name, Stock, Price, Category, Image_Path)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (item_id, name, stock, price, category, image_path))
        conn.commit()
        conn.close()
        return "Item added successfully."
    except sqlite3.IntegrityError:
        conn.close()
        return "Error: Item ID already exists."

def update_item(item_id, name, stock, price, category, image_path):
    conn = sqlite3.connect("schema/store_management.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Items SET Name=?, Stock=?, Price=?, Category=?, Image_Path=? WHERE ItemID=?;", (name, stock, price, category,image_path, item_id))
    conn.commit()
    conn.close()
    return "Item updated successfully."

def delete_item(item_id):
    conn = sqlite3.connect("schema/store_management.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Items WHERE ItemID=?;", (item_id,))
    conn.commit()
    conn.close()
    return "Item deleted successfully."

def get_items():
    conn = sqlite3.connect("schema/store_management.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items;")
    items = cursor.fetchall()
    conn.close()
    return items

def get_item_by_id(item_id):
    conn = sqlite3.connect("schema/store_management.db")
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE ItemID = ?", (item_id,))
    return c.fetchone()

###========== [TABLE INITIALIZATION] ==========### - //Allows the user to create tables automatically if unconfigured.// 
conn = sqlite3.connect("schema/store_management.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS User (Username TEXT PRIMARY KEY, Name TEXT NOT NULL, Address TEXT NOT NULL, Password TEXT NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Items(ItemID TEXT PRIMARY KEY, Name TEXT NOT NULL, Stock INTEGER NOT NULL, Price REAL NOT NULL,Category TEXT NOT NULL, Image_Path TEXT)""")

conn.commit()

conn.close()