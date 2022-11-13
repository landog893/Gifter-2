try:
    from item_manager import ItemManager
except ImportError as e:
    import sys
    sys.path.append("./src")

from item_manager import ItemManager

itemMan = ItemManager()
print('Adding item')
new_item_id = itemMan.add_item('Toaster', '4 slice, with bagel setting', 'www.amazon.com','35')
print(new_item_id)
assert(new_item_id)



print('Adding item with missing title, error case')
assert(itemMan.add_item('', '4 slice, with bagel setting', '35', 'www.amazon.com') == -1)

print('Reading item')
item_info = itemMan.get_item(new_item_id)
assert(item_info[0] == 'Toaster')
assert(item_info[1] == '4 slice, with bagel setting')
assert(item_info[2] == 'www.amazon.com')
assert(item_info[3] == '35')

print('Reading non-existing item, error case')
assert(itemMan.get_item(new_item_id+100) == None)

print('Updating item')
assert(itemMan.update_item(new_item_id, title='Toaster Oven', desc= 'An Oven', link= "www.target.com", cost = 230) == 0)

print('Updating nonexisting item, error case')
assert(itemMan.update_item(new_item_id+100, title='Toaster Oven', desc= 'An Oven', link= "www.target.com", cost = 230) == 0)

print('Deleting created item')
assert(itemMan.delete_item(new_item_id) == 0)

print('Deleting nonexisting item, error case')
assert(itemMan.delete_item(new_item_id+100) == 0)
