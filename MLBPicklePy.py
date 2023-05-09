#setup
import numpy as np
import pandas as pd
import openpyxl as oxl
import sklearn as sklearn
from sklearn import datasets
df = pd.read_excel("MLBPickleRoster.xlsx")
throw = ('L','R')
Bat = ('L','R','S')
Position = ('C','1B','2B','3B','SS','LF','CF','RF','RP','SP')
Division = ('AL West', 'AL Central', 'AL East', 'NL East', 'NL Central', 'NL West')
Division = np.unique(df.Division)
age = np.arange(19, 43)
team = np.unique(df.Team)
#Yellow Division input

#Enter Yellow Info Here
YDIV = 'AL West'

#Yellow Age

YAGE = 26
floor = (YAGE - 2)
ceiling = (YAGE + 2)
#age = np.arange((YAGE-2),(YAGE+2))
#age = pd.DataFrame(age)

if YDIV == 'AL West':
    results = ('AL East', 'AL Central','NL West')
if (YDIV == 'AL Central'):
    results = ('AL East', 'NL Central','AL West')
if (YDIV == 'AL East'):
    results = ('AL West', 'AL Central','NL East')
if (YDIV == 'NL West'):
    results = ('NL East', 'NL Central','AL West')
if (YDIV == 'NL Central'):
    results = ('NL East', 'AL Central','NL West')
if (YDIV == 'NL East'):
    results = ('AL East', 'NL Central','NL West')
Division = results
#WIP
test = df
test = test[test[['Division']].apply(tuple, 1).isin(Division)]


#Green areas
Position = 'SP'
throw = 'L'
Bat = 'R'
#age =
#Division = 'AL West'
#team =



PickleR = df
PickleR = PickleR[PickleR['THW'] == throw]
PickleR = PickleR[PickleR['POS'] == Position]
#workspace



PickleR = PickleR[PickleR['Division'] == Division] 
#Broken when only have Yellow Division
#fails on logic
PickleR = PickleR[PickleR['BAT'] == Bat]
#filter by age and remove YAGE
PickleR = PickleR[PickleR['Age'] > floor]
PickleR = PickleR[PickleR['Age'] < ceiling]
PickleR = PickleR[PickleR['Age'] != YAGE]

PickleR = PickleR[PickleR['Team'] == team]

PickleR.head(5)




