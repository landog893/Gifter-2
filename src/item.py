from item_manager import ItemManager
class item():
    def __init__(self, title = '', desc = '', link = '', cost = '', ID = None):
        if ID != None:
            itemMan = ItemManager()
            info = itemMan.get_item(ID)
            if(info != None):
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
            self.itemID = self.create_item()

    
    def create_item(self):
        itemMan = ItemManager()
        ID = itemMan.add_item(self.title, self.desc, self.link, self.cost)
        return ID
        # item = itemMan.add_item(self.title, self.desc, self.link, self.cost)
        # return item

    def modify_item(self, title, desc, link, cost):
        itemMan = ItemManager()
        self.title = title
        self.desc = desc
        self.link = link
        self.cost = cost
        itemMan.update_item( self.itemID, title, desc, link, cost)
    
    def view_item(self):
        itemMan = ItemManager()
        return itemMan.get_item(self.itemID)

    def delete_item(self):
        itemMan = ItemManager()
        itemMan.delete_item(self.itemID)



# i = item('Football', 'NFL original', 'www.football.com', 50)
# print(i.cost)
# i.modify_item('Football', 'NFL original', 'www.football.com', 65)
# print(i.view_item())
# i.delete_item()