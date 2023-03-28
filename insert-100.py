#!/usr/bin/env python
# coding: utf-8

#importing required libraries
import datetime
import pandas as pd
import csv

#starting counter
start = datetime.datetime.now()
print("starting insertion for 100 tuples")

#reading data into memory
df = pd.read_csv('clean.csv', nrows=100)

#dropping 'Location' & 'SiteID' for readings table
df = df.drop(['Location', 'geo_point_2d'], axis=1)

#formatting date values into time
df['Date Time'] =  pd.to_datetime(df['Date Time'])
df['Date Time']= df['Date Time'].dt.strftime('%Y-%m-%d %H:%M:%S')

df['DateStart'] =  pd.to_datetime(df['DateStart'])
df['DateStart']= df['DateStart'].dt.strftime('%Y-%m-%d %H:%M:%S')

df['DateEnd'] =  pd.to_datetime(df['DateEnd'])
df['DateEnd']= df['DateEnd'].dt.strftime('%Y-%m-%d %H:%M:%S')

#creating list and inserting data in it
sql = "INSERT INTO readings VALUES \n"
count = 1
readings = []

for index,row in df.iterrows():
    readings = ["'" + str(x)+ "'" for x in row.values]
    readings = ",".join(readings)
    readings = readings.replace("''", "NULL")
    readings = readings.replace("'True'", "True")
    readings = readings.replace("'False'", "False")
    
    sql+= '(' + str(count) +','+ readings+ '),'+ '\n'
    
    count+=1


sql2 = sql[:-2] + ';'

#storing 100 tuples in csv file
insert = open('insert-100.csv', 'w')
insert.write(sql2 + '\n')

#printing thge list of 100 values
print(sql2)


print('\n')
end = datetime.datetime.now()
print('insert-100 took ' , str(end -start), ' seconds to execute')
