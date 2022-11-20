import numpy as np
import pandas as pd
import sys
import streamlit as st

class AccountInfo:
    def __init__(self):
        try:
            self.database = 'data/UserInfo.csv'
            self.data = pd.read_csv(self.database)
        except FileNotFoundError:
            self.database = '../data/UserInfo.csv'
            self.data = pd.read_csv(self.database)
        
    def create_account(self, name, surname='', birthday='',username='', password = '',interests='', wishlist='', friendlist=''):
        print("whole data")
        if self.data.empty:
            if name == '':
                print('Name cannot be empty')
                return -1
            
            account_dict = {
                'ID': 0,
                'First Name': name,
                'Last Name': surname,
                'Birthday': birthday,
                'UserName' : username,
                'Password' : password,
                'Interests': interests,
                'WishList': wishlist,
                'FriendList': friendlist
            }
            self.data = self.data.append(account_dict, ignore_index=True)
            self.data.to_csv(self.database, index=False)
            print('Account created successfully!')
            return self.data[self.data['ID']==1]
        else:
            id_list = sorted(self.data.ID.tolist(), reverse=True)
            lastID = id_list[0]
            if name == '':
                print('Name cannot be empty')
                return -1
            elif username in self.data['UserName'].values:
                print('User Name already in use. Please use another one!')
                st.error("User Name already in use. Please use another one!")
                return -2
            else:
                account_dict = {
                    'ID': lastID+1,
                    'First Name': name,
                    'Last Name': surname,
                    'Birthday': birthday,
                    'UserName' : username,
                    'Password' : password,
                    'Interests': interests,
                    'WishList': wishlist,
                    'FriendList': friendlist
                    }
                self.data = self.data.append(account_dict, ignore_index=True)
                self.data.to_csv(self.database, index=False)
                print('Account created successfully!')
                return self.data[self.data['ID']==lastID+1]
    
    def update_account(self, ID, name='', surname='', birthday='',username='',password = '', interests='', wishlist='', friendlist=''):
        id_list = self.data.ID.tolist()
        if ID not in id_list:
            print('User ID:', ID, 'is not in the database!!!')
            return -1
        else:
            data = self.data[self.data['ID']==ID]
            print(data)
            # if name=='':
            #     name = data.Name.values[0]
            # if surname=='':
            #     surname = data.Surname.values[0]
            # if birthday=='':
            #     birthday = data.Birthday.values[0]
            # if interests=='':
            #     interests = data.Interests.values[0]
            # if wishlist=='':
            #     wishlist = data.WishList.values[0]
            #     print(wishlist)
            # if friendlist=='':
            #     friendlist = data.FriendList.values[0]
            account_dict = {
                'ID': ID,
                'Fist Name': name,
                'Last Name': surname,
                'Birthday': birthday,
                'UserName' : username,
                'Password' : password,
                'Interests': interests,
                'WishList': wishlist,
                'FriendList': friendlist
            }
            print(account_dict)
            
            index = self.data[self.data['ID']==ID].index[0]
            print(index)
            #self.data.at[index, 'WishList'] = account_dict
            self.data.loc[index,'ID'] = ID
            self.data.loc[index,'First Name'] = name
            self.data.loc[index, 'Last Name'] = surname
            self.data.loc[index, 'Birthday'] = birthday
            self.data.loc[index, 'UserName'] = birthday
            self.data.loc[index, 'Password'] = password
            self.data.loc[index, 'Interests'] = interests
            self.data.loc[index, 'WishList'] = wishlist
            print(type(wishlist))
            self.data.loc[index, 'FriendList'] = friendlist
            self.data.to_csv(self.database, index=False)
            print('Account updated successfully!')
        return self.data[self.data['ID']==ID]
    
    def get_database(self):
        return self.data
    
    def delete_account(self, ID):
        id_list = self.data.ID.tolist()
        if ID not in id_list:
            print('Invalid ID, please enter valid ID.')
            return -1
        else:
            matched_data = self.data[self.data['ID']==ID]
            self.data = self.data.drop(matched_data.index)
            print('Account deleted successfully!')
            self.data.to_csv(self.database, index=False)
        return matched_data
    
    def get_info(self, ID):
        id_list = self.data.ID.tolist()
        if ID not in id_list:
            return -1
        else:
            return self.data[self.data['ID']==ID]
    
    def get_account(self, username,password):
        uname_list = self.data.UserName.tolist()
        if username not in uname_list:
            print('Invalid ID, please enter valid ID.')
            return -1
        else:
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
    
