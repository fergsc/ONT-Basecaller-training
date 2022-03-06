bonitoDir="/path/to/bonito"
model="dna_r9.4.1"
cudaDevice="cuda:0"
reference="/path/to/reference/reference.fasta"
fast5Dir="/path/to/fast5"


mkdir $(basename $reference .fasta)~$(basename $fast5Dir)

${bonitoDir}/bonito basecaller $model --device $cudaDevice --save-ctc --reference $reference $fast5Dir > $(basename $reference .fasta)~$(basename $fast5Dir)/basecalls.sam
