# Take a given set of read identity and q-scores and combine into a single csv file.
# Will produce a phred scored csv and a percent.
#

import pandas as pd
import numpy as np
import sys


##########
### check that we have input file
if len(sys.argv) != 4:
    print("require: read_identity.csv read_Qscore.csv saveFileName")
    exit()



##########
### get file names
identity = sys.argv[1]  # name,read_length,iden
qScore = sys.argv[2]    # name,phred-score,length
saveName = sys.argv[3]

##########
###read in data
identity = pd.read_csv(identity, sep="\t")
identity = identity[["name", "iden"]]
qScore = pd.read_csv(qScore)

##########
### merge data, only keep reads that exist in common
combined = identity.merge(qScore, on='name')

##########
## save as percent
# currently idenitiy = % and Q-scores = Phred

tmp = combined["phred-score"].copy()

combined["phred-score"] = (1-10**(-combined["phred-score"]/10))*100

saveDf = combined[["length", "iden", "phred-score"]].copy()
saveDf["basecaller"] = saveName
saveDf["iden"] = round(saveDf["iden"], 2)
saveDf["phred-score"] = round(saveDf["phred-score"], 2)

saveDf = saveDf.rename({"basecaller": "basecaller", "iden": "iden", "phred-score": "q-score"}, axis=1)
saveDf.to_csv("{}~PC.csv".format(saveName), index=False)


##########
## save as phred 

combined["phred-score"] = tmp
combined["iden"] = round(-10* np.log10(1-(combined["iden"]/100)),2)
combined["iden"].replace([np.inf, -np.inf], 50, inplace=True)

saveDf = combined[["length", "iden", "phred-score"]].copy()
saveDf["basecaller"] = saveName
saveDf["iden"] = round(saveDf["iden"], 2)
saveDf["phred-score"] = round(saveDf["phred-score"], 2)

saveDf = saveDf.rename({"basecaller": "basecaller", "iden": "iden", "phred-score": "q-score"}, axis=1)
saveDf.to_csv("{}~phred.csv".format(saveName), index=False)
