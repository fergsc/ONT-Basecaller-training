import nanoget

fnq="/path to/reads.fastq.gz"

df=nanoget.get_input("fastq", [fnq])
df.to_csv("{}.csv".format(fnq), index = False)
