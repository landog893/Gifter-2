#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS public."itemData"
        (
            "ID" serial NOT NULL,
            "Title" character varying COLLATE pg_catalog."default",
            "Description" character varying COLLATE pg_catalog."default",
            "Link" character varying COLLATE pg_catalog."default",
            "Cost" numeric DEFAULT 0,
            CONSTRAINT "itemData_pkey" PRIMARY KEY ("ID")
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS public."peopleData"
        (
            "ID" serial NOT NULL,
            "Name" character varying COLLATE pg_catalog."default",
            "Surname" character varying COLLATE pg_catalog."default",
            "Interests" character varying COLLATE pg_catalog."default",
            "WishList" character varying COLLATE pg_catalog."default",
            "FriendList" character varying COLLATE pg_catalog."default",
            "Birthday" date,
            CONSTRAINT "peopleData_pkey" PRIMARY KEY ("ID")
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