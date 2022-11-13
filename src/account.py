from account_info import AccountInfo

class Account():
    def __init__(self, name='', surname='', birthday='', interests='', wishlist='', friendlist='', ID = None):
        if ID != None:
            accountMan = AccountInfo()
            info = accountMan.get_info(ID)
            if isinstance(info, int):
                raise ValueError
            else: 
                self.name = info['Name']
                self.surname = info['Surname']
                self.birthday = info['Birthday']
                self.interests = info['Interests']
                self.wishlist = info['WishList']
                self.friendlist = info['FriendList']
                self.ID = ID
        else: 
            self.name = name
            self.surname = surname
            self.birthday = birthday
            self.interests = interests
            self.wishlist = wishlist
            self.friendlist = friendlist
            self.ID = self.create_account()['ID']
        

    def create_account(self):
        accountMan = AccountInfo()
        acc = accountMan.create_account(self.name, self.surname, self.birthday, self.interests, self.wishlist, self.friendlist)
        return acc
    
    def view_account(self):
        accountMan = AccountInfo()
        return accountMan.get_info(self.ID)

    def update_account(self, name='', surname='', birthday='', interests='', wishlist='', friendlist=''):
            self.name = name
            self.surname = surname
            self.birthday = birthday
            self.interests = interests
            self.wishlist = wishlist
            self.friendlist = friendlist
            accountMan = AccountInfo()
            accountMan.update_account(self.ID, name, surname, birthday, interests, wishlist, friendlist)



# #acc = Account('Hannah', 'Montana', '05/05/1995', 'Singing, Dancing')
# #acc.view_account()
# acc = Account(ID=1)
# ints = (acc.interests.to_string(index=False)).replace("\"", "")
# ints += ", Ballet"
# # print(ints)
# wishes = (acc.wishlist.to_string(index=False))
# acc.update_account(acc.name.to_string(index=False), acc.surname.to_string(index=False), acc.birthday.to_string(index=False), ints, acc.wishlist.to_string(index=False), acc.friendlist.to_string(index=False))

        