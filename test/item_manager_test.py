try:
    from item_manager import ItemManager
except ImportError as e:
    import sys
    sys.path.append("./src")

from item_manager import ItemManager

itemMan = ItemManager()
print('Adding item')
item = itemMan.add_item('Toaster', '4 slice, with bagel setting', '35', 'www.amazon.com')
print(item)
ind = int(item['ItemID'])
assert((item).empty == 0)



print('Adding item with missing title, error case')
assert(itemMan.add_item('', '4 slice, with bagel setting', '35', 'www.amazon.com') == -1)

print('Reading item')
assert(itemMan.get_item(ind).empty == 0)

print('Reading non-existing item, error case')
assert(itemMan.get_item(ind+100) == -1)

print('Updating item')
assert(itemMan.update_item(ind, title='Toaster Oven', desc= 'An Oven', link= "www.target.com", cost = 230) == 0)

print('Updating nonexisting item, error case')
assert(itemMan.update_item(ind+100, title='Toaster Oven', desc= 'An Oven', link= "www.target.com", cost = 230) == -1)

print('Deleting created item')
assert(itemMan.delete_item(ind) == 0)

print('Deleting nonexisting item, error case')
assert(itemMan.delete_item(ind+100) == -1)
