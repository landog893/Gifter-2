import pandas as pd
import sys


class wishlist():
    def __init__(self, items):
        self.items = items
        # print(df['Title'])

    def add_item(self, item):
        self.items.append(item)

    def delete_item(self, itemID):
        for i, item in enumerate(self.items):
            pass

    def option(self):
        print("============================================================")
        print("Enter index number to do follwing function")
        print("0 to View all item; 1 to view specific item; 2 to create item; 3 to delete item; 4 to EXIT CONSOLE")
        input_decision = int(input())

        if input_decision == 0:
            self.view_all_items()
            self.option()

        elif input_decision == 1:
            self.view_item()

        elif input_decision == 2:
            self.create_item()
            print("ITEM HAS BEEN CREATED")
            self.view_all_items()

        elif input_decision == 3:
            print("DELETING ITEM")
            self.delete_item()
            print("ITEM HAS BEEN DELETED")
            self.view_all_items()

        elif input_decision == 4:
            sys.exit()

        else:
            print("INVALID INPUT")
            self.option()

    def view_all_items(self):
        print("============================================================")
        df = pd.read_csv(r'./data/item_data.csv')
        print(df['Title'])
        self.option()

    def view_item(self):

        print("============================================================")
        df = pd.read_csv(r'./data/item_data.csv')
        print("Enter index number of item you want to view")
        input_choice = int(input())
        if input_choice < len(df):
            print("Item:  " + str(df['ItemID'][input_choice]))
            print("Title:  " + str(df['Title'][input_choice]))
            print("Description:  " + str(df['Description'][input_choice]))
            print("Link:  " + str(df['Link'][input_choice]))
            print("Cost:  " + str(df['Cost'][input_choice]))
            self.option()
        else:
            print("=====================================")
            print("INVALID INPUT")
            self.view_item()

    def create_item(self):
        print("======================================================")
        print("INSIDE CREATE ITEM")
        df = pd.read_csv(r'./data/item_data.csv')
        new_item = []
        for i in df.columns:
            print("ENTER NEW " + str(i) + " BELOW:")
            input_element = input()
            new_item.append(input_element)
        df.loc[len(df.index)] = new_item
        df.to_csv(r'./data/item_data.csv', index=False)

    def delete_item(self):
        print("======================================================")
        print("INSIDE DELETE ITEM")
        df = pd.read_csv(r'./data/item_data.csv')
        print("ENTER INDEX OF ITEM YOU WANT TO DELETE: ")
        input_choice = int(input())
        print(len(df.index))
        if input_choice < len(df.index):
            df = df.drop(labels=[input_choice], axis=0, inplace=False)
            df.to_csv(r'./data/item_data.csv', index=False)
        else:
            print("INVALID INPUT")
            self.option()
# obj = wishlist()
# obj.option()
