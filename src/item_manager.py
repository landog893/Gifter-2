import psycopg2
from config import config


class ItemManager:

    def add_item(self, title, desc='', link='',  cost=''):
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

    def update_item(self, ID: int, title, desc='', link='', cost=''):

        query = """UPDATE "Item" Set "Title" = %s, "Description" = %s, "Link" = %s, "Cost" = %s  Where "ID" = %s"""
        conn = None
        try:
            # initializing connection
            params = config()
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # execute a statement
            cur.execute(query, (title, desc, link, cost, ID))
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
