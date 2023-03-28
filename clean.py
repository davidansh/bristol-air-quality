#!/usr/bin/env python
# coding: utf-8

#importing libraries
import pandas as pd
import datetime

#starting counter
start = datetime.datetime.now()
print("cleaning of data started")

#loading data into workspace
df = pd.DataFrame(pd.read_csv('crop.csv', low_memory=False))
print(str(len(df)+1), " lines are present in crop.csv")

#creating dictionary of stations
stations = {
                188 : 'AURN Bristol Centre',
                203 : 'Brislington Depot',
                206 : 'Rupert Street',
                209 : 'IKEA M32',
                213 : 'Old Market',
                215 : 'Parson Street School',
                228 : 'Temple Meads Station',
                270 : 'Wells Road',
                271 : 'Trailer Portway P&R',
                375 : 'Newfoundland Road Police Station',
                395 : "Shiner's Garage",
                452 : 'AURN St Pauls',
                447 : 'Bath Road',
                459 : 'Cheltenham Road \ Station Road',
                463 : 'Fishponds Road',
                481 : 'CREATE Centre Roof',
                500 : 'Temple Way',
                501 : 'Colston Avenue'
            }

written=1
deleted=0

#filtering data that are not matching with stations dictionary
for index, row in df.iterrows():
    if (row['SiteID'],row['Location']) not in stations.items():
        deleted+=1
        df = df.drop(index)
    else:
        written+=1
        
#saving clean data in csv file
df.to_csv('clean.csv', index= False)

#providing insights of data
print(str(deleted)+ ' mismatch lines are removed')
print(str(written)+ ' lines are written to clean.csv')

end =datetime.datetime.now()
print('clean.py took ' + str(end - start)+ ' seconds to execute')
