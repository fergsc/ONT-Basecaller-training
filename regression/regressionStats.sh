#
#R: The correlation between the observed values of the response variable and the predicted values of the response variable made by the model.
#R2: The proportion of the variance in the response variable that can be explained by the predictor variables in the regression model.
#

import pandas as pd
import numpy as np
from scipy import stats
import sys

# get file names
inFile = sys.argv[1]

#read in data
df = pd.read_csv(inFile)

# print results
print(inFile)
print(len(df))
#print(stats.linregress(combined["iden"],combined["q-score"]))
print(stats.linregress(combined["q-score"],combined["iden"]))
print("\n")