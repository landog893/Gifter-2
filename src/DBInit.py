#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    
    ### commands for creating tables
    commands = (
        """
        CREATE TABLE IF NOT EXISTS public."Item"
        (
            "ID" serial NOT NULL,
            "Title" character varying COLLATE pg_catalog."default",
            "Description" character varying COLLATE pg_catalog."default",
            "Link" character varying COLLATE pg_catalog."default",
            "Cost" numeric DEFAULT 0,
            CONSTRAINT "Item_pkey" PRIMARY KEY ("ID")
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS public."Account"
        (
            "ID" serial NOT NULL,
            "Name" character varying COLLATE pg_catalog."default",
            "UserName" character varying COLLATE pg_catalog."default",
            "Interests" character varying COLLATE pg_catalog."default",
            "WishList" character varying COLLATE pg_catalog."default",
            "FriendList" character varying COLLATE pg_catalog."default",
            "Birthday" date,
            CONSTRAINT "Account_pkey" PRIMARY KEY ("ID")
        )
        """
        )
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        
        
        ###The following are sample queries
        
        # ###INSERT
        # print("INSERT")
        # test_title = "test_title"
        # test_desc = "test_desc"
        # test_link = "test_link"
        # cost ="21"
        # query = """Insert Into public."Item" ("Title","Description","Link","Cost") values(%s,%s,%s,%s) returning "ID" """
        # cur.execute(query, (test_title,test_desc,test_link,cost))
        # _id  = cur.fetchone()
        # print(_id)
 
        
        # ###CHECK INSERT
        # print("CHECK INSERT")
        # # _id = 13
        # query = """Select * From "Item" WHERE "ID" = %s;"""
        # cur.execute(query,(_id,))
        # res = cur.fetchall()
        # for item in res[0]:
        #     print(item)
        
        # ###UPDATE
        # print("UPDATE")
        # new_title = "new_title"
        # new_description = "new_description"    
        # query = """UPDATE "Item" Set "Title" = %s, "Description" = %s Where "ID" = %s"""
        # cur.execute(query,(new_title,new_description,_id))
        
        # ###CHECK RESULT AFTER UPDATE
        # print("CHECK RESULT AFTER UPDATE")
        # query = """Select * From "Item" Where "ID" = %s;"""
        # cur.execute(query,(_id,))
        # res = cur.fetchall()
        # for item in res[0]:
        #     print(item)
        
        
        # ###DELETE
        # print("DELETE")
        # query = """Delete From "Item" Where "ID" = %s;"""
        # cur.execute(query,(_id,))
        
        # ###CHECK RESULT AFTER DELETE
        # print("CHECK RESULT AFTER DELETE")
        # query = """Select * From "Item";"""
        # cur.execute(query)
        # res = cur.fetchall()
        # for item in res:
        #     print(item)
        
        cur.close()
        # commit the changes
        conn.commit()
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()