from account_info import AccountInfo
import streamlit as st

class Account():
    def __init__(self, name='', surname='', birthday='', username='',password = '', interests='', wishlist='', friendlist='', ID = None):
        if ID != None:
            accountMan = AccountInfo()
            info = accountMan.get_info(ID)
            if info:
                self.name = info[0]
                self.surname = info[1]
                self.birthday = info[2]
                self.username = info[3]
                self.password = info[4]
                self.interests = info[5]
                self.wishlist = info[6]
                self.friendlist = info[7]
                self.ID = ID
            else: 
                raise ValueError
        else: 
            self.name = name
            self.surname = surname
            self.birthday = birthday
            self.username = username
            self.password = password
            self.interests = interests
            self.wishlist = wishlist
            self.friendlist = friendlist
            ID = self.create_account()
            if ID == None:
                st.error("Can not create account, please check the format of information")
            else:
                self.ID = ID
        

        
    def create_account(self):
        accountMan = AccountInfo()
        acc = accountMan.create_account(self.name, self.surname, self.birthday,self.username, self.password,self.interests, self.wishlist, self.friendlist)
        return acc
    
    def view_account(self):
        accountMan = AccountInfo()
        return accountMan.get_info(self.ID)

    def update_account(self, name='', surname='', birthday='', username='',password = '', interests='',wishlist = '', friendlist= ''):
            self.name = name
            self.surname = surname
            self.birthday = birthday
            self.username = username
            self.password = password
            self.interests = interests
            self.wishlist = wishlist
            self.friendlist = friendlist
            accountMan = AccountInfo()
            accountMan.update_account(self.ID, name, surname, birthday,username, password,interests, wishlist, friendlist)



# #acc = Account('Hannah', 'Montana', '05/05/1995', 'Singing, Dancing')
# #acc.view_account()
# acc = Account(ID=1)
# ints = (acc.interests.to_string(index=False)).replace("\"", "")
# ints += ", Ballet"
# # print(ints)
# wishes = (acc.wishlist.to_string(index=False))
# acc.update_account(acc.name.to_string(index=False), acc.surname.to_string(index=False), acc.birthday.to_string(index=False), ints, acc.wishlist.to_string(index=False), acc.friendlist.to_string(index=False))

        