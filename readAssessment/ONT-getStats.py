# Calculate average read quality scores from an ONT fastq.
# Also outputs read name and length.

#
# The functions errs_tab and ave_qual were obtained from https://github.com/wdecoster/nanopack
#


import sys
import gzip
from Bio import SeqIO
from math import log

def errs_tab(n):
    """Generate list of error rates for qualities less than equal than n."""
    return [10**(q / -10) for q in range(n+1)]

def ave_qual(quals, qround=False, tab=errs_tab(128)):
    """Calculate average basecall quality of a read and produce ONT style q-scores."""
    if quals:
        mq = -10 * log(sum([tab[q] for q in quals]) / len(quals), 10)
        if qround:
            return round(mq)
        else:
            return mq
    else:
        return None

##########
### check that we have input file
if len(sys.argv) != 2:
    print("require a fastq.gz file")
    exit()

fq = sys.argv[1]
saveFile = "{}.csv".format(fq.split("/")[-1].split(".")[0])
print("{} -> {}".format(fq, saveFile))

with gzip.open(fq, "rt") as handle, open(saveFile, "w") as save:
    save.write("name,phred-score,length\n")
    for record in SeqIO.parse(handle, "fastq"):
        save.write("{},{},{}\n".format(record.name, ave_qual(record.letter_annotations["phred_quality"]), len(record.seq)))
