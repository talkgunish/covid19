# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re

df = pd.read_csv('/content/forta.csv')

"""## 1 - Top 5 hospitals with the greatest number of COVID-19 admitted cases (i.e. “Hospitalised"?)"""

dfHosp = df[['Name of hospital admitted','Hospitalised/ Discharged/ Deceased']].query('`Hospitalised/ Discharged/ Deceased` == "Hospitalised"')
dfHosp.groupby(['Name of hospital admitted']).size().nlargest(5).reset_index(name = 'Top 5 Count')

"""## 2 - Average time between the date of onset and the report date?"""

dfDate = df[['Report date','Date of onset']].query('`Date of onset`.str.contains("^\d+[/]\d+[/]\d+$", regex=True)', engine='python')
dfDate['Date of onset'] = pd.to_datetime(dfDate['Date of onset'], format='%d/%m/%Y')
dfDate['Report date'] = pd.to_datetime(dfDate['Report date'], format='%d/%m/%Y')
diff = (dfDate['Report date'] - dfDate['Date of onset']).dt.days
diff.mean()

"""## 3 - Sort these cases into 4 age brackets, 20-39, 40-59, 60-79 & 80-99 and identify the ratio of discharged to hospitalised in each?"""

dfAge = df[['Age','Hospitalised/ Discharged/ Deceased']].query('Age.str.contains("^\d+$", regex=True)', engine='python')

dfAge['Age'] = pd.to_numeric(dfAge['Age'])

num = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Discharged" and Age >= 20 and Age <= 39')
den = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Hospitalised" and Age >= 20 and Age <= 39 ')
print("Age 20-39 :"+str(num.shape[0]/den.shape[0]))

num = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Discharged" and Age >= 40 and Age <= 59')
den = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Hospitalised" and Age >= 40 and Age <= 59')
print("Age 40-59 :"+str(num.shape[0]/den.shape[0]))

num = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Discharged" and Age >= 60 and Age <= 79')
den = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Hospitalised" and Age >= 60 and Age <= 79')
print("Age 60-79 :"+str(num.shape[0]/den.shape[0]))

num = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Discharged" and Age >= 80 and Age <= 99')
den = dfAge.query('`Hospitalised/ Discharged/ Deceased` == "Hospitalised" and Age >= 80 and Age <= 99')
print("Age 80-99 :"+str(num.shape[0]/den.shape[0]))
