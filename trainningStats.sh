reference="/path/to/reference.reference.fasta"
reads="/path/tobasecalled/reads/reads.fastq.gz"
threads=12

minimap2Dir="/pth/to/minimap2"
samtoolsDir="/path/to/samtools"
promixio="/path/to/promixio"

${minimap2Dir}/minimap2 -t $threads -ax map-ont $reference $reads \
    | ${samtoolsDir}/samtools view -b > mapped_reads.bam

${promixio}/stats_from_bam -t $threads -o $(basename $reference)~$(basename $reads).csv mapped_reads.bam