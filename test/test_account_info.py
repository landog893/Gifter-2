try:
    from account_info import AccountInfo, Friends
except ImportError as e:
    import sys
    sys.path.append("./src")
    
from account_info import AccountInfo, Friends


accInfo = AccountInfo()
friendInfo = Friends()

print('Creating new account')
created_acc_id = accInfo.create_account('Ram', 'Bhusal', '12/23/1998', 'RBhusal98', '19981223', '"Eating pizza, Salsa, Ramen"', '"1, 2, 3, 5"', '"2, 3"')
print('Checking returned ID')
assert(created_acc_id)

print('Reading created account')
created_acc_info = accInfo.get_info(created_acc_id)
assert(created_acc_info[0] == 'Ram')
assert(created_acc_info[1] == 'Bhusal')
assert(created_acc_info[2] == '12/23/1998')
assert(created_acc_info[3] == 'RBhusal98')
assert(created_acc_info[4] == '19981223')
assert(created_acc_info[5] == '"Eating pizza, Salsa, Ramen"')
assert(created_acc_info[6] == '"1, 2, 3, 5"')
assert(created_acc_info[7] == '"2, 3"')

print('Updating account')
new_info = accInfo.get_info(created_acc_id)
new_info = list(new_info)
print(new_info)
new_info[5] = '"Eating pizza, Salsa, Ramen, Steak"'
accInfo.update_account(created_acc_id, new_info[0], new_info[1],new_info[2],new_info[3],new_info[4],new_info[5],new_info[6],new_info[7])

updated_info = accInfo.get_info(created_acc_id)
assert(updated_info[5] == '"Eating pizza, Salsa, Ramen, Steak"')


print('Reading non-existing account, error case')
assert(accInfo.get_info(200) == None)

print('Deleting account')
assert(accInfo.delete_account(created_acc_id) == True)

print('Deleting an nonexisting account')
assert(accInfo.delete_account(300) == True)
