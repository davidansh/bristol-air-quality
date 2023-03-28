#!/usr/bin/env python
# coding: utf-8

#importing libraries for workspace
import pandas as pd
import datetime

#starting timer
start = datetime.datetime.now()
print("cropping of data started")

#loading data into workspace
mydata = pd.DataFrame(pd.read_csv("bristol-air-quality-data.csv", delimiter = ';', low_memory = False))
print(str(len(mydata)+1), " lines are present in bristol-air-quality-data.csv")

#formatting date values into dattetime for cropping
mydata['Date Time']= pd.to_datetime(mydata['Date Time'])

#cropping data
crop = mydata[(mydata['Date Time'] >= '2010-01-01 00:00:00+00:00')]

#saving cropped data into csv
crop.to_csv('crop.csv', index= False)

#providing attributes about data
print(str(len(crop)+1) + ' lines are written to crop.csv')

end=datetime.datetime.now()
print('crop.py took ' + str(end - start)+ ' seconds to execute')
