import psycopg2
from config import config

class ItemManager:
    # def __init__ (self):
    #     try:
    #         self.database = 'data/item_data - Copy.csv'
    #         data = read_csv(self.database)
    #     except: 
    #         self.database = '../data/item_data - Copy.csv'

    def add_item(self, title, desc = '', link = '',  cost = ''):
        if title == '':
            print('Title cannot be empty')
            return -1
        
        query = """Insert Into public."Item" ("Title","Description","Link","Cost") values(%s,%s,%s,%s) returning "ID" """
        conn = None
        ID = None
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execute a statement
            cur.execute(query, (title, desc, link, cost))
            ID = cur.fetchone()[0]
            cur.close()
            conn.commit()
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
                
        return ID


    def get_item(self, ID: int):
        query = """Select "Title","Description","Link","Cost" From "Item" WHERE "ID" = %s;"""
        conn = None
        item_info = None
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execute a statement
            cur.execute(query, (ID,))
            item_info = cur.fetchall()
            cur.close()
            conn.commit()
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
        
        return item_info[0] if item_info else None
        
        
        # data = read_csv(self.database)
        # if data.loc[data['ItemID']==ID].empty:
        #     print("Item does not exist")
        #     return -1
        # return (data.loc[data['ItemID'] == ID])

    def delete_item(self, ID: int):
        
        query = """Delete From "Item" Where "ID" = %s;"""
        conn = None
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execute a statement
            cur.execute(query, (ID,))
            cur.close()
            conn.commit()
            cur.close()        
            print("Item deleted.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
        return 0
    
        # cur.execute(query,(_id,))
        # data = read_csv(self.database)
        # if data.index[data['ItemID'] == ID].empty:
        #     print("Item does not exist")
        #     return -1
        # data = data.drop(data.index[data['ItemID'] == ID], axis = 0)
        # data.to_csv(self.database, mode='w', index=False)
        # print("Item deleted.")
        # return 0

    def update_item(self, ID: int, title, desc = '', link = '', cost = ''):
        
        query = """UPDATE "Item" Set "Title" = %s, "Description" = %s, "Link" = %s, "Cost" = %s  Where "ID" = %s"""
        conn = None
        try:
        # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
        # execute a statement
            cur.execute(query, (title,desc,link,cost,ID))
            cur.close()
            conn.commit()
            cur.close()
            print("Item Updated.")
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
        
        return 0
        
        
        
        # data = read_csv(self.database)
        # item = data.loc[data['ItemID'] == ID]
        # ind = data['ItemID'] == ID
        # if data.loc[data['ItemID'] == ID].empty:
        #     print('Item does not exist.')
        #     return -1
        # data.loc[ind,'Title'] = title
        # data.loc[ind,'Description'] = desc
        # data.loc[ind, 'Link'] = link
        # data.loc[ind, 'Cost'] = cost
        # data.to_csv(self.database, mode='w', index=False)
        # print('Updated item')
        # return 0






