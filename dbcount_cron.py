#!/usr/bin/env python
import MySQLdb
import logging
import ConfigParser
import sys
log = logging.getLogger(__name__)
CONFIG_FILE= 'dbconfig.ini'


def get_schemas(db):
    schemas = []
    db_query = "show databases"
    cursor = db.cursor()

    try:
        # Execute the SQL command
        cursor.execute(db_query)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            # Now print fetched result
            schemas.append(row[0]);
    except Exception, e:
        print "Error: unable to fecth data %s", e
        return null
    return schemas

def read_config(configfile):

    conf = ConfigParser.ConfigParser()
    conf.read(configfile)
    dblist=[]
    for option in conf.items('monitor'):
        dbname = option[0]
        (host,user,passwd) = option[1].split(',')
        dblist.append((dbname,host,user,passwd))

    return dblist

def connect_db(host, user,pw):
    db='INFORMATION_SCHEMA'
    try:
        # Open database connection
        db = MySQLdb.connect(host, user, pw, db)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
    except Exception,e:
        print ("Unable to open database %s" % e)
        return
    return db

def get_schema_info(schema,db,servername,tran_id):
    datalist = []
    db_query = "show table status in %s" % schema
    cursor = db.cursor(MySQLdb.cursors.DictCursor) 

    table_statuses =['Engine', 'Row_format', 'Update_time', 'Rows', 
                     'Checksum', 'Name', 'Check_time', 'Index_length', 
                     'Auto_increment', 'Data_length', 'Create_options', 
                     'Avg_row_length', 'Data_free', 'Version', 
                     'Create_time', 'Collation', 'Comment', 
                     'Max_data_length']

    try:
        # Execute the SQL command
        cursor.execute(db_query)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        
        for row in results:
            # Now print fetched result
            # for item in table_statuses:
            #     print "%s\t%s:\t%s" % (schema,item, row[item]) 
            # print
            datalist.append((
                         tran_id,
                         servername,
                         schema,
                         row['Name'],
                         row['Version'],
                         row['Engine'],
                         row['Rows'],
                         row['Data_length'],
                         row['Avg_row_length'],
                         row['Create_options'],
                    
                     ))

    except Exception, e:
        print "Error: unable to fecth data %s" % e
        return null

    return datalist

def get_transaction():
    id = ""
    try:
        db = MySQLdb.connect('localhost','root','', 'dbmon')
        cursor = db.cursor()
        sql = "insert into dbtransaction values ()"
        cursor.execute(sql)
        id = db.insert_id()
        db.commit()
    except Exception,e:
        print "Exception: %s" % e
        return
    return id


def insert_records(records):
    mondb = MySQLdb.connect('localhost','root','', 'dbmon')
    cursor = mondb.cursor()
    sql = """insert into dbrecords
            (dbtran_id, server_name, dbname , table_name , table_type , 
             engine, rowcount, rowsize,avg_rowlength,create_options) 
            values (%s , %s, %s, %s, %s, %s, %s, %s, %s, %s )"""
    try:
        cursor.executemany(sql,records)
    except Exception,e:
        print "Exception: %s" % e
    #print "Sql: %s" % sql
    #print "Records: %s" % records
    mondb.commit()


if __name__ == "__main__":
    configfile = 'dbconfig.ini'
    if len(sys.argv) < 2:
	    sys.exit("Unable to open config file")
    else:
	    configfile=sys.argv[1]
	
    dblist = read_config(configfile)
    mondb = MySQLdb.connect('localhost','root','', 'dbmon')
    tran_id = get_transaction()

    default_schemas = ['backup_information',
                       'information_schema',
                       'performance_schema',
                       'test',
                       'mysql',
                      ]

    for dbitem in dblist:

        db = connect_db(dbitem[1],dbitem[2],dbitem[3])

        if db:
            schemas = [schema for schema in get_schemas(db) if schema not in default_schemas]
            for schema in schemas:
                records = get_schema_info(schema=schema,db=db,servername=dbitem[1],tran_id=tran_id)
                insert_records(records)
        else:
            print "Unable to connect db: %s" % dbitem[1]

