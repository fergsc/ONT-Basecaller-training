import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

maxLength = 150000
maxQ = 35
saveLocation = "/path to save to/plots"
runsPC = ["/data path/spp1.csv",
        "/data path/spp2.csv",
        "/data path/spp3.csv"]

runsPhred = ["/data path/spp1.csv",
        "/data path/spp2.csv",
        "/data path/spp3.csv"]


for currRun in runsPC:
    name = currRun.split("/")[-1].split(".")[0]
    print(name)

    df = pd.read_csv(currRun, header = 0)
    df['length'] = pd.to_numeric(df['length'],errors='coerce')
    df['identity'] = pd.to_numeric(df['identity'],errors='coerce')

    for basecaller in df["basecaller"].unique():
        tmpDf = df.loc[df['basecaller'] == basecaller]['length']
        tmpDf = tmpDf.divide(1000)
        tmpDf = tmpDf[tmpDf < (maxLength/1000)]
        ax = sns.distplot(x = tmpDf, hist = False, kde = True, label=basecaller)

    # guppy 6 is hidden by guppy 5, make guppy 5 a dashed line
    for line in ax.lines:
        if line.get_label() == "Super accurate (Guppy 5)":
            line.set_linestyle("--")

    plt.legend(prop={'size': 9})
    plt.title('Read length')
    plt.xlabel('Length (Kbp)')
    plt.ylabel('Density')
    plt.savefig("{}/{}~length.png".format(saveLocation, name), bbox_inches='tight', dpi=1000)
    plt.clf()

    for basecaller in df["basecaller"].unique():
        tmpDf = df.loc[df['basecaller'] == basecaller]['identity']
        ax = sns.distplot(x = tmpDf, hist = False, kde = True, label=basecaller)

    # guppy 6 is hidden by guppy 5, make guppy 5 a dashed line
    for line in ax.lines:
        if line.get_label() == "Super accurate (Guppy 5)":
            line.set_linestyle("--")

    plt.xlim([70, 100])
    plt.legend(prop={'size': 9})
    plt.title('Read accuracy')
    plt.xlabel('Accuracy (%)')
    plt.ylabel('Density')
    plt.savefig("{}/{}~identity.png".format(saveLocation, name), bbox_inches='tight', dpi=1000)
    plt.clf()

for currRun in runsPhred:
    name = currRun.split("/")[-1].split(".")[0]
    print(name)
    df = pd.read_csv(currRun, header = 0)
    df['length'] = pd.to_numeric(df['Q-score'],errors='coerce')
    for basecaller in df["basecaller"].unique():
        tmpDf = df.loc[df['basecaller'] == basecaller]['Q-score']
        #tmpDf = tmpDf[tmpDf < maxQ]
        ax = sns.distplot(x = tmpDf, hist = False, kde = True, label=basecaller)
    plt.xlim([0, 35])
    plt.legend(prop={'size': 9})
    plt.title('Read Q-scores')
    plt.xlabel('Q-score')
    plt.ylabel('Density')
    plt.savefig("{}/{}.png".format(saveLocation, name), bbox_inches='tight', dpi=1000)
    plt.clf()
