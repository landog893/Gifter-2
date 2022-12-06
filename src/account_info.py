import psycopg2
from config import config
import numpy as np
import pandas as pd
import sys
import streamlit as st


class AccountInfo:
    def create_account(
        self,
        name,
        surname="",
        birthday="",
        email="",
        notifications="",
        username="",
        password="",
        interests="",
        wishlist="",
        friendlist="",
    ):

        query = """Insert Into public."Account" ("Name","Surname","Birthday","Email","Notifications","UserName","Password","Interests","WishList","FriendList")
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) returning "ID" """
        conn = None
        Checkquery = """Select * From "Account" WHERE "UserName" = %s;"""
        acc = None
        try:
            # initializing connection
            params = config()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # check name field
            if name == "":
                return -1
            # execute userName check
            cur.execute(Checkquery, (username,))
            rows = cur.fetchall()
            print(len(rows))
            if len(rows) > 0:
                print("User Name already in use. Please use another one!")
                st.error("User Name already in use. Please use another one!")
                return -2
            else:
                cur.execute(
                    query,
                    (
                        name,
                        surname,
                        birthday,
                        email,
                        notifications,
                        username,
                        password,
                        interests,
                        wishlist,
                        friendlist,
                    ),
                )
                acc = cur.fetchall()[0]
            cur.close()
            # execute a statement
            cur.close()
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

        return acc

    def update_account(
        self,
        ID,
        name="",
        surname="",
        birthday="",
        email="",
        notifications="",
        username="",
        password="",
        interests="",
        wishlist="",
        friendlist="",
    ):
        query = """UPDATE "Account" Set "Name" = %s, "Surname" = %s, "Birthday" = %s, "Email" = %s, "Notifications" = %s, "UserName" = %s, "Password" = %s, "Interests" = %s, "WishList" = %s, "FriendList" = %s
                Where "ID" = %s"""
        conn = None
        success = True
        try:
            # initializing connection
            params = config()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute a statement
            cur.execute(
                query,
                (
                    name,
                    surname,
                    birthday,
                    email,
                    notifications,
                    username,
                    password,
                    interests,
                    wishlist,
                    friendlist,
                    ID,
                ),
            )
            cur.close()
            conn.commit()
            cur.close()
            print("Item Updated.")

        except (Exception, psycopg2.DatabaseError) as error:
            success = False
            raise Exception(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")
            return success

    def delete_account(self, ID):
        query = """Delete From "Account" Where "ID" = %s;"""
        conn = None
        success = True
        try:
            # initializing connection
            params = config()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute a statement
            cur.execute(query, (ID,))
            cur.close()
            conn.commit()
            cur.close()
            print("Item deleted.")
        except (Exception, psycopg2.DatabaseError) as error:
            st.error(error)
            success = False
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")
            return success

    def get_info(self, ID):
        query = """Select "Name","Surname","Birthday","Email","Notifications","UserName","Password","Interests","WishList","FriendList"
                 From "Account" WHERE "ID" = %s;"""
        conn = None
        user_info = None
        try:
            # initializing connection
            params = config()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute a statement
            cur.execute(query, (ID,))
            user_info = cur.fetchall()
            cur.close()
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

        return user_info[0] if user_info else None

    def get_account(self, username, password):
        query = """Select "ID", "Name","Surname","Birthday","Email","Notifications","UserName","Password","Interests","WishList","FriendList"
                 From "Account" WHERE "UserName" = %s;"""
        conn = None
        user_info = None
        try:
            # initializing connection
            params = config()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute a statement
            cur.execute(query, (username,))
            user_info = cur.fetchall()
            cur.close()
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

        if user_info:
            user_info = user_info[0]
            if user_info[7] == password:
                return user_info
            else:
                return -2
        else:
            return -1

    def find_id(self, ID):
        query = """Select "Name","Surname","Birthday","UserName","Password","Interests","WishList","FriendList"
                 From "Account" WHERE "ID" = %s;"""
        conn = None
        user_info = None
        try:
            # initializing connection
            params = config()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute a statement
            cur.execute(query, (ID,))
            user_info = cur.fetchall()
            cur.close()
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")

        return user_info[0].ID if user_info else 0

    def find_friend(self, str_tomatch):
        query = """Select "ID","Name","Surname","Birthday","UserName","Password","Interests","WishList","FriendList" From "Account";"""
        conn = None
        user_info = None
        user_list = []
        try:
            # initializing connection
            params = config()
            print("Connecting to the PostgreSQL database...")
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute a statement
            cur.execute(query)
            user_info = cur.fetchall()
            cur.close()
            conn.commit()
            cur.close()
            for i in range(len(user_info)):
                # print(user_info[i])
                Name = user_info[i][1] + " " + user_info[i][2]
                if str_tomatch.lower() in Name.lower():
                    user_list.append(user_info[i])
                print(Name)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed.")
        return user_list
