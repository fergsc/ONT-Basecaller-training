import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# get file names
inFile = sys.argv[1]
saveName = sys.argv[2]

#read in data
df = pd.read_csv(inFile, sep="\t")

#convert indentity % to phred score
df["iden"] = round(-10* np.log10(1-(df["iden"]/100)),2)
df["iden"].replace([np.inf, -np.inf], 50, inplace=True)

# fix column headings
df = df.rename({"iden": "Read Identity", "q-score": "Read Q-score"}, axis=1)

# plot
g = sns.jointplot(data = df, y="Read Identity", x="Read Q-score", kind='hist', xlim=(5, 35), ylim=(5, 35))
xx = np.linspace(df["Read Q-score"].min(), df["Read Q-score"].max(), 200)
fit = np.polyfit(df["Read Q-score"].to_numpy().flat, df["Read Identity"].to_numpy().flat, 1)
g.ax_joint.plot(xx, np.poly1d(fit)(xx), color="r")

#save plot
#plt.title(saveName, fontsize = 15)
plt.savefig("{}~phred.png".format(saveName), bbox_inches='tight', dpi=500)
