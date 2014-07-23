import MySQLdb
import locale
import ConfigParser
import sys
import os
import ConfigParser

Config= ConfigParser.ConfigParser()
Config.read("dbconfig.ini")
Config.sections()

KAYNAK_HOST= Config.get("server",'host')
KAYNAK_USER= Config.get("server",'user')
KAYNAK_PASSWD= Config.get("server",'passwd')
KAYNAK_DB= Config.get("server",'db')

kaynak_files =[]


class mydb():
    def __init__(self):
        self.db = None
        self.cursor = None
        try:
            self.connectdb()
        except Exception,e:
            raise Exception("DB Connection Error %s" % e)
            
               
    def connectdb(self):
        # Open database connection
        self.db = MySQLdb.connect(host=KAYNAK_HOST,db=KAYNAK_DB,user=KAYNAK_USER,passwd=KAYNAK_PASSWD )

        # prepare a cursor object using cursor() method
        self.cursor = self.db.cursor()
   

    def get_max_transaction(self):
        # Prepare SQL query to INSERT a record into the database.
        sql = "SELECT max(id) FROM dbtransaction"

        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            row = self.cursor.fetchone()
        except Exception,e:
            print "Error: unable to fecth data: %s" % e
            raise Exception("SQL: %s error" % sql )

        return row


    def get_list(self):
        result = []
        # FORMAT(rowcount,0) as row_count ,FORMAT(rowsize/(1024*1024),2) as row_size,

        sql = """select server_name,dbname,table_name,table_type,engine,
                 rowcount as row_count ,rowsize/(1024*1024) as row_size,
                 create_options
                 from dbrecords where dbtran_id=%s 
                 and (rowcount> 1000000 or rowsize > 1024*1024*1024) 
                 order by server_name,rowcount desc
             """ % self.get_max_transaction()
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            rows = self.cursor.fetchall()
            # Now print fetched result
            columns = [desc[0] for desc in self.cursor.description]
        except Exception,e:
            raise Exception("Exception: %s -> SQL: %s error" % (e,sql) )
    
        for row in rows:
            row = dict(zip(columns,row))
            result.append(row)

        return result


    def disconnect(self):
        # disconnect from server
        self.db.close()

