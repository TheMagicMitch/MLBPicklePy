#setup
import numpy as np
import pandas as pd
import openpyxl as oxl
df = pd.read_excel("MLBPickleRoster.xlsx")
throw = ('L','R')
Bat = ('L','R','S')
Position = ('C','1B','2B','3B','SS','LF','CF','RF','RP','SP')
#Division = ('AL West', 'AL Central', 'AL East', 'NL East', 'NL Central', 'NL West')
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
agecol = df.Age
agecol = agecol.drop(364)
agecol = agecol.drop(391)
agecol = agecol.drop(580)
agecol = agecol.drop(798)
df.Age = agecol
df.Age = pd.to_numeric(df.Age)

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
PickleR = PickleR[PickleR['Division'].isin(Division)]
PickleR = PickleR[PickleR['BAT'] == Bat]
#filter by age and remove YAGE
PickleR = PickleR[PickleR['Age'] > floor]
PickleR = PickleR[PickleR['Age'] < ceiling]
PickleR = PickleR[PickleR['Age'] != YAGE]

PickleR = PickleR[PickleR['Team'] == team]

PickleR.head(5)

