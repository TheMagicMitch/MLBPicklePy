#setup
import numpy as np
import pandas as pd
import openpyxl as oxl
df = pd.read_excel("MLBPickleRoster.xlsx")
throw = ('L','R')
Bat = ('L','R','S')
Position = ('C','1B','2B','3B','SS','LF','CF','RF','RP','SP')
Division = ('AL West', 'AL Central', 'AL East', 'NL East', 'NL Central', 'NL West')
age = np.arange(19, 43)
team = df.Team

#Yellow Division input

#Enter Yellow Info Here
#YDIV =

#Yellow Age

#YAGE = 
#age = np.arrange((YAGE-2),(YAGE+2))

if (YDIV == 'AL West') 
    results = ('AL East', 'AL Central','NL West')
  if (YDIV == 'AL Central') 
    results = ('AL East', 'NL Central','AL West')
  if (YDIV == 'AL East') 
    results = ('AL West', 'AL Central','NL East')
  if (YDIV == 'NL West') 
    results = ('NL East', 'NL Central','AL West')
  if (YDIV == 'NL Central') 
    results = ('NL East', 'AL Central','NL West')
  if (YDIV == 'NL East') 
    results = ('AL East', 'NL Central','NL West')
Division = results
