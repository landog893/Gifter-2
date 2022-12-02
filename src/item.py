from item_manager import ItemManager

# This class represents an item object. This item is a gift that a user can add to their wishlist. 
class item():
    # Initialization of the item object.
    def __init__(self, title = '', desc = '', link = '', cost = '', ID = None):
        if ID != None:
            itemMan = ItemManager()
            info = itemMan.get_item(ID)
            if not info :
                raise ValueError
            else:  
                self.title = info[0]
                self.desc = info[1]
                self.link = info[2]
                self.cost = info[3]
                self.itemID = ID
    
        else:
            self.title = title
            self.desc = desc
            self.link = link
            self.cost = cost
            self.itemID = int(self.create_item())

    # This method creates an item. 
    def create_item(self):
        itemMan = ItemManager()
        item = itemMan.add_item(self.title, self.desc, self.link, self.cost)
        return item

    # This method modifies an item. 
    def modify_item(self, title, desc, link, cost):
        itemMan = ItemManager()
        self.title = title
        self.desc = desc
        self.link = link
        self.cost = cost
        itemMan.update_item( self.itemID, title, desc, link, cost)
    
    # This pulls an item for viewing.
    def view_item(self):
        itemMan = ItemManager()
        return itemMan.get_item(self.itemID)

    # This method deletes an item. 
    def delete_item(self):
        itemMan = ItemManager()
        itemMan.delete_item(self.itemID)



# i = item('Football', 'NFL original', 'www.football.com', 50)
# print(i.cost)
# i.modify_item('Football', 'NFL original', 'www.football.com', 65)
# print(i.view_item())
# i.delete_item()