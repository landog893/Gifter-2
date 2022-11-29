import psycopg2
from config import config
import numpy as np
import pandas as pd
import sys
import streamlit as st

class AccountInfo:
        
    def create_account(self, name, surname='', birthday='',username='', password = '',interests='', wishlist='', friendlist=''):
        
        query = """Insert Into public."Account" ("Name","Surname","Birthday","UserName","Password","Interests","WishList","FriendList") 
                values(%s,%s,%s,%s,%s,%s,%s,%s) returning "ID" """
        conn = None
        Checkquery =  """Select * From "Account" WHERE "UserName" = %s;"""
        ID = None
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # check name field
            if name == '':
                return -1
        #execute userName check
            cur.execute(Checkquery,(username,))
            rows = cur.fetchall()
            print(len(rows))
            if len(rows) > 0:
                print('User Name already in use. Please use another one!')
                st.error("User Name already in use. Please use another one!")
                return -2
            cur.close()
        # execute a statement
            cur = conn.cursor()
            cur.execute(query, (name, surname, birthday, username,password,interests,wishlist,friendlist))
            acc = cur.fetchone()
            print("create ID")
            print(acc)
            cur.close()
            conn.commit()
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
                
        return acc
    
    def update_account(self, ID, name='', surname='', birthday='',username='',password = '', interests='', wishlist = '', friendlist= ''):
        query = """UPDATE "Account" Set "Name" = %s, "Surname" = %s, "Birthday" = %s, "UserName" = %s, "Password" = %s, "Interests" = %s, "WishList" = %s, "FriendList" = %s
                Where "ID" = %s"""
        conn = None
        success = True
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execute a statement
            cur.execute(query, (name,surname,birthday,username,password,interests, wishlist, friendlist,ID))
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
                print('Database connection closed.')
            return success
    
    def delete_account(self, ID):
        query = """Delete From "Account" Where "ID" = %s;"""
        conn = None
        success = True
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
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
                print('Database connection closed.')
            return success
                
        
    
    def get_info(self, ID):
        query = """Select "Name","Surname","Birthday","UserName","Password","Interests","WishList","FriendList" 
                    From "Account" WHERE "ID" = %s;"""
        conn = None
        user_info = None
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
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
                print('Database connection closed.')
        
        return user_info[0] if user_info else None
    
    def get_account(self, username,password):
        query = """Select "ID", "Name","Surname","Birthday","UserName","Password","Interests","WishList","FriendList" 
                    From "Account" WHERE "UserName" = %s;"""
        conn = None
        user_info = None
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
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
                print('Database connection closed.')
        
        if user_info:
            user_info = user_info[0]
            if user_info[5] == password:
                return user_info
            else:
                return -2
        else:
            return -1
        

            info = self.data[self.data['UserName']==username]
            print("information of user")
            print(info.Password.values[0])
            if info.Password.values[0] == password:
                return self.data[self.data['UserName']==username]
            return -2 

    def search_ID(self, ID):
        if ID == None:
            print("ID cannot be empty!!!")
            return [0], -1
        ID_result = self.data[self.data['ID']==ID]
        if ID_result.values.size == 0:
            print("ID not found! Try ID ranges from 0 to 10.")
            return [0], -1
        return ID_result, True
        
    def get_name(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][1]
    
    def get_surname(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][2]
        
    def get_birthday(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][3]
    
    def get_interests(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][4]
        
    def get_wishlist(self, ID):
        result, flag = self.search_ID(ID)
        if flag == -1:
            return -1
        else:
            result_dict = result.values
            return result_dict[0][5]
        
    def add_wishlist(self, ID, items):
        flag = 1
        wl_str = self.get_wishlist(ID)
        if str(wl_str)=='nan':
            wl_str = []
        else:
            wl_str = wl_str.replace('"','')
            wl_str = wl_str.split(', ')
        for _item in items:
            if str(_item) in wl_str:
                print('Item ID:', _item, 'is already in the wishlist!!!')
                flag = 0
            else:
                wl_str.append(str(_item))
                print('Item ID:', _item, 'is added successfully!!!')
        wl_str = ', '.join(i for i in wl_str)
        wl_str = '"' + wl_str + '"'
        index = self.data[self.data['ID']==ID].index[0]
        self.data.at[index, 'WishList'] = wl_str
        self.data.to_csv(self.database, index=False)
        return self.data[self.data['ID']==ID]
    
    def delete_wishlist(self, ID, items):
        flag = 1
        wl_str = self.get_wishlist(ID)
        if str(wl_str)=='nan':
            wl_str = []
        else:
            wl_str = wl_str.replace('"','')
            wl_str = wl_str.split(', ')
        for _item in items:
            if str(_item) in wl_str:
                if len(wl_str):
                    print('There are no items in the wishlist!!!')
                    flag = 0
                else:
                    wl_str.remove(str(_item))
                    print('Item ID:', _item, 'is removed successfully!!!')
            else:
                print('Item ID:', _item, 'is not found in the wishlist!!!')
        wl_str = ', '.join(i for i in wl_str)
        wl_str = '"' + wl_str + '"'
        index = self.data[self.data['ID']==ID].index[0]
        self.data.at[index, 'WishList'] = wl_str
        self.data.to_csv(self.database, index=False)
        return self.data[self.data['ID']==ID]
        
    def get_friendlist(self, ID):
        result, flag = self.search_ID(ID)
        if flag == False:
            return False
        else:
            result_dict = result.values
            return result_dict[0][6]


class Friends(AccountInfo):
    def __init__(self):
        super().__init__()
    
    def get_friend_names(self,ID):
        friend_names = []
        friend_ids = self.get_friendlist(ID)
        for c in friend_ids:
            try:
                if int(c):
                    friend_id = int(c)
                    fname = self.get_name(friend_id)
                    sname = self.get_surname(friend_id)
                    aname = fname + " " + sname 
                    friend_names.append(aname)
            except:
                pass
            
        return friend_names
    
    def add_friend(self, ID: int, friend_IDs: list):
        fl_str = self.get_friendlist(ID)
        if str(fl_str)=='nan':
            fl_str = []
        else:
            fl_str = fl_str.replace('"','')
            fl_str = fl_str.split(', ')
        for _id in friend_IDs:
            if str(_id) in fl_str:
                print('ID:', _id, 'is Already friend!!!')
            else:
                fl_str.append(str(_id))
        fl_str = ', '.join(i for i in fl_str)
        fl_str = '"' + fl_str + '"'
        index = self.data[self.data['ID']==ID].index[0]
        self.data.at[index, 'FriendList'] = fl_str
        return self.data[self.data['ID']==ID]
    
    def delete_friend(self, ID: int, friend_IDs: list):
        fl_str = self.get_friendlist(ID)
        fl_str = fl_str.replace('"','')
        fl_str = fl_str.split(', ')
        for _id in friend_IDs:
            if str(_id) in fl_str:
                fl_str.remove(str(_id))
            else:
                print('ID:', _id, 'not found in the friend list!!')
        fl_str = ', '.join(i for i in fl_str)
        fl_str = '"' + fl_str + '"'
        index = self.data[self.data['ID']==ID].index[0]
        self.data.at[index, 'FriendList'] = fl_str
        return self.data[self.data['ID']==ID]
    
