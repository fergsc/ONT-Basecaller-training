hifiasmDir="/path/to/hifi"
fastq="/path/to/reads/reads.fastq.gz"
threads=12

${hifiasmDir}/hifiasm -t threads -o $(basename $fastq .fastq.gz) $fastq

awk '/^S/{print ">"$2;print $3}' $(basename $fastq .fastq.gz).bp.hap1.p_ctg.gfa > hap1.fasta
awk '/^S/{print ">"$2;print $3}' $(basename $fastq .fastq.gz).bp.hap2.p_ctg.gfa > hap2.fasta
awk '/^S/{print ">"$2;print $3}' $(basename $fastq .fastq.gz).bp.p_ctg.gfa      > unphased.fasta

cat hap1.fasta hap2.fasta > diploid.fasta