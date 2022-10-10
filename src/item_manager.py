from pandas import *
class ItemManager:
    def __init__ (self):
        try:
            self.database = 'data/item_data - Copy.csv'
            data = read_csv(self.database)
        except: 
            self.database = '../data/item_data - Copy.csv'

    def add_item(self, title, desc = '', link = '',  cost = ''):
        if title == '':
            print('Title cannot be empty')
            return -1
        data = read_csv(self.database)
        lastElement = data['ItemID'].tolist()[-1]+1
        new_data = {'ItemID': lastElement, 'Title': title, 'Description': desc,'Link': link, 'Cost': [cost]}
        df = DataFrame(new_data)
        df.to_csv(self.database, mode='a', index=False, header=False)
        print("Data appended successfully.")
        return df


    def get_item(self, ID: int):
        data = read_csv(self.database)
        if data.loc[data['ItemID']==ID].empty:
            print("Item does not exist")
            return -1
        return (data.loc[data['ItemID'] == ID])

    def delete_item(self, ID: int):
        data = read_csv(self.database)
        if data.index[data['ItemID'] == ID].empty:
            print("Item does not exist")
            return -1
        data = data.drop(data.index[data['ItemID'] == ID], axis = 0)
        data.to_csv(self.database, mode='w', index=False)
        print("Item deleted.")
        return 0

    def update_item(self, ID: int, title, desc = '', link = '', cost = ''):
        data = read_csv(self.database)
        item = data.loc[data['ItemID'] == ID]
        ind = data['ItemID'] == ID
        if data.loc[data['ItemID'] == ID].empty:
            print('Item does not exist.')
            return -1
        data.loc[ind,'Title'] = title
        data.loc[ind,'Description'] = desc
        data.loc[ind, 'Link'] = link
        data.loc[ind, 'Cost'] = cost
        data.to_csv(self.database, mode='w', index=False)
        print('Updated item')
        return 0





