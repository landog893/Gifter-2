try:
    from account_info import AccountInfo, Friends
except ImportError as e:
    import sys
    sys.path.append("./src")
    
from account_info import AccountInfo, Friends


accInfo = AccountInfo()
friendInfo = Friends()

print('Tests to be added...')
# created_acc = accInfo.create_account('Ram', 'Bhusal', '12/23/1998', '"Eating pizza, Salsa, Ramen"', '"1, 2, 3, 5"', '"2, 3"')
# _id = created_acc.ID.values[0]
# created_row = created_acc[created_acc['ID']==_id]
# assert(created_row.Name.values[0] == 'Ram')
# assert(created_row.Surname.values[0] == 'Bhusal')
# assert(created_row.Birthday.values[0] == '12/23/1998')
# assert(created_row.FriendList.values[0] == '"2, 3"')

# print('Reading account')
# assert(accInfo.get_info(2).all()[0] == 1)

# print('Reading non-existing account, error case')
# assert(accInfo.get_info(200) == -1)

# print('Deleting account')
# assert(accInfo.delete_account(_id).all()[0] == 1)

# print('Deleting an nonexisting account')
# assert(accInfo.delete_account(300) == -1)

# print('Getting friend names....')
# assert(friendInfo.get_friend_names(9)==['David Beckham'])
# assert(friendInfo.get_friend_names(4)==['Jane Doe', 'David Beckham'])

# print('Adding some friends......')
# assert(friendInfo.add_friend(9, [2, 3]).FriendList.values[0].replace('"', '').split(', ')[-2:]==['2', '3'])

# print('Adding some wishlist items.....')
# assert(accInfo.add_wishlist(9, [4, 9, 10]).WishList.values[0].replace('"', '').split(', ')[-3:]==['4', '9', '10'])
