#!/usr/bin/env python
# coding: utf-8

#importig libraries
import pandas as pd
import sqlalchemy
import datetime
import sys

#starting the timer
start = datetime.datetime.now()

#creating a connection to the database
try:
    connection = sqlalchemy.create_engine("mysql://root@localhost/pollution_db2?charset=utf8mb4")

    #creating database
    print('creating database')
    with connection.connect() as con:
        con.execute("DROP DATABASE IF EXISTS pollution_db2;")
        con.execute("CREATE DATABASE pollution_db2")
        con.execute("USE pollution_db2")

    #creating schema table and populating it
        print('creating schema table and populating it')
        schemadf = pd.read_csv("schema.csv")
        schemadf.index = schemadf.index+1
        schemadf.to_sql(con=connection, name='schema', if_exists='append', index=True, index_label='SchemaID')

    #creating stations table and populating it
        print('creating stations table and populating it')
        stationsdf = pd.read_csv('clean.csv', usecols = ['SiteID','Location', 'geo_point_2d']).drop_duplicates(keep = 'first')
        stationsdf.to_sql(con=connection, name='stations', if_exists='append', index= False)

    #creating readings table and populating it
        print('creating readings table and populating it')
        readingsdf = pd.read_csv('clean.csv', low_memory = False)
        readingsdf = readingsdf.drop(['Location', 'geo_point_2d'], axis =1)
        readingsdf.index = readingsdf.index+1
        readingsdf = readingsdf.rename(columns ={'Date Time': 'Datetime'})
        readingsdf.to_sql(con=connection, name='readings', if_exists='append', index=True, index_label='ReadingsID', dtype={'Date Time': sqlalchemy.DateTime(), 'DateStart':sqlalchemy.DateTime(), 'DateEnd':sqlalchemy.DateTime()})

    #adding primary and foreign keys to database
        con.execute('ALTER TABLE `Schema` ADD PRIMARY KEY (`SchemaID`);')
        con.execute('ALTER TABLE `Readings` ADD PRIMARY KEY (`ReadingsID`);')
        con.execute('ALTER TABLE `Stations` ADD PRIMARY KEY (`SiteID`);')
        con.execute('ALTER TABLE `Readings` ADD FOREIGN KEY (`SiteID`) REFERENCES `Stations`(`SiteID`);')

    #closing connection
        con.close()

    connection.dispose()
    
except BaseException as err:
    print(f"An error occured: {err}")
    sys.exit(1)

#insights of code
end = datetime.datetime.now()
print("populate.py took ", str(end-start), " seconds to execute")
